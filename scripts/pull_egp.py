#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pull_egp.py — ดึงข้อมูลสัญญาภาครัฐจาก data.go.th (CKAN) → map เข้า schema seed_bids → ออกเป็น CSV ให้ OPY

⚠️ ต้องรันบนเครื่อง PC ในไทยเท่านั้น — API บล็อก IP คลาวด์ (ยืนยันโดย DB 2026-08-25)
⚠️ สคริปต์นี้ **ไม่แก้ seed_bids.js** — ออกเป็น CSV handoff ให้ OPY เอาไปใส่ (Core Rule 22)
⚠️ API key อ่านจากไฟล์นอก repo เท่านั้น — ห้าม hardcode ห้าม commit (repo นี้ public)

วิธีใช้
  1) เก็บ key ไว้ที่   %USERPROFILE%\\.rmn_datagoth_key      (บรรทัดเดียว)
  2) python pull_egp.py --dataset <dataset-id-or-name>
     หรือ  python pull_egp.py --resources <id1,id2,...>
  3) ผลลัพธ์ →  _handoff_OPY_egp_pull_<YYYYMMDD>.csv  +  _handoff_OPY_egp_pull_<YYYYMMDD>_report.txt

หมายเหตุออกแบบ (ต่างจากที่ DB เสนอ 1 จุด — ตั้งใจ)
  DB เจอ column shift +7 ในไฟล์ที่ทดสอบ → สคริปต์นี้ **ไม่ hardcode +7**
  แต่ auto-detect ต่อ resource ด้วยการดูรูปร่างค่าจริง (รหัส 11 หลัก / TIN 13 หลัก / วันที่ พ.ศ. / จำนวนเงิน)
  เหตุผล: offset เป็นความผิดพลาดตอนผู้เผยแพร่ทำ CSV → แต่ละไฟล์/แต่ละปีอาจเลื่อนไม่เท่ากัน
  ถ้า detect ไม่ได้ สคริปต์จะ **หยุดและรายงาน** ไม่เดาต่อ
"""

import argparse, csv, json, os, re, sys, time, urllib.parse, urllib.request
from collections import Counter, defaultdict

BASE = "https://opend.data.go.th/get-ckan"
KEYFILE = os.path.join(os.path.expanduser("~"), ".rmn_datagoth_key")

# คำค้นสั้นๆ ที่ทนการสะกดผิดของฝั่งรัฐ (เช่น "กิจการร่ามค้า") — ค้น substring ไม่ค้นชื่อเต็ม
QUERIES = ["อาร์เอ็มเอ็น", "ตักสิลา", "รักดี"]

# ชื่อผู้ชนะที่ยอมรับ → entity ใน seed_bids
ENTITY_MAP = {
    "ห้างหุ้นส่วนจำกัด อาร์เอ็มเอ็น เอ็นเตอร์ไพส์": "ห้างหุ้นส่วน RMN",
    "กิจการร่วมค้า อาร์เอ็มเอ็น": "กิจการร่วมค้า RMN",
    "กิจการร่ามค้า อาร์เอ็มเอ็น": "กิจการร่วมค้า RMN",   # รัฐพิมพ์ผิด
    "กิจการร่วมค้า ตักสิลา": "กิจการร่วมค้า ตักสิลา",
    "กิจการร่วมค้า รักดี": "กิจการร่วมค้า รักดี",
    "ห้างหุ้นส่วนจำกัด รักดี การโยธา": "หจก.รักดี การโยธา",
    "หจก.รักดี การโยธา": "หจก.รักดี การโยธา",
}
OUR_TINS = {"0443561001307", "0993000469275"}   # หจก. RMN · กิจการร่วมค้า อาร์เอ็มเอ็น

TH_MONTH = {"ม.ค.":1,"ก.พ.":2,"มี.ค.":3,"เม.ย.":4,"พ.ค.":5,"มิ.ย.":6,
            "ก.ค.":7,"ส.ค.":8,"ก.ย.":9,"ต.ค.":10,"พ.ย.":11,"ธ.ค.":12}

RE_PROJ  = re.compile(r"^\d{11}$")
RE_TIN   = re.compile(r"^\d{13}$")
RE_THDATE= re.compile(r"^\d{1,2}\s+(ม\.ค\.|ก\.พ\.|มี\.ค\.|เม\.ย\.|พ\.ค\.|มิ\.ย\.|ก\.ค\.|ส\.ค\.|ก\.ย\.|ต\.ค\.|พ\.ย\.|ธ\.ค\.)\s+\d{2}$")
RE_MONEY = re.compile(r"^\d+(\.\d+)?$")


def api_key():
    k = os.environ.get("DATAGOTH_KEY")
    if k:
        return k.strip()
    if os.path.exists(KEYFILE):
        return open(KEYFILE, encoding="utf-8").read().strip()
    sys.exit("❌ ไม่พบ API key — วางไว้ที่ %s หรือ set DATAGOTH_KEY" % KEYFILE)


def call(path, params, key, tries=3):
    url = BASE + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"api-key": key, "accept": "application/json"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(3 * (i + 1))


def th_to_iso(t):
    """'14 ม.ค. 68' → '2568-01-14'"""
    t = (t or "").strip()
    if not RE_THDATE.match(t):
        return ""
    d, m, y = t.split()
    return "25%s-%02d-%02d" % (y, TH_MONTH[m], int(d))


def detect_layout(records):
    """
    หา field ที่ค่าจริงเป็นอะไร โดยดูรูปร่างค่า ไม่เชื่อชื่อคอลัมน์
    คืน dict role -> field name  (role: proj, tin, winner, contractNo, signedOn, endsOn, status, money*)
    """
    fields = list(records[0].keys())
    prof = {}
    for f in fields:
        vals = [str(r.get(f, "") or "").strip() for r in records]
        nz = [v for v in vals if v]
        if not nz:
            prof[f] = "empty"; continue
        def frac(rx): return sum(1 for v in nz if rx.match(v)) / len(nz)
        if frac(RE_PROJ) > .8:   prof[f] = "proj"
        elif frac(RE_TIN) > .8:  prof[f] = "tin"
        elif frac(RE_THDATE) > .8: prof[f] = "date"
        elif frac(RE_MONEY) > .8: prof[f] = "money"
        else:                    prof[f] = "text"

    roles = {}
    for f, p in prof.items():
        if p == "proj" and "proj" not in roles: roles["proj"] = f
        if p == "tin" and "tin" not in roles:   roles["tin"] = f

    dates = [f for f in fields if prof[f] == "date"]
    monies = [f for f in fields if prof[f] == "money"]
    texts = [f for f in fields if prof[f] == "text"]

    # ผู้ชนะ = field ข้อความที่มีชื่อห้างของเราโผล่
    for f in texts:
        joined = " ".join(str(r.get(f, "") or "") for r in records)
        if any(q in joined for q in QUERIES):
            roles["winner"] = f; break

    # เลขที่สัญญา = ข้อความสั้นมี "/" เยอะ
    for f in texts:
        nz = [str(r.get(f, "") or "") for r in records if r.get(f)]
        if nz and sum(1 for v in nz if "/" in v and len(v) <= 20) / len(nz) > .6:
            roles["contractNo"] = f; break

    # สถานะ = ข้อความซ้ำๆ ไม่กี่ค่า
    for f in texts:
        vals = [str(r.get(f, "") or "") for r in records if r.get(f)]
        if vals and len(set(vals)) <= 6 and max(len(v) for v in vals) <= 40:
            roles["status"] = f; break

    if dates: roles["date_fields"] = dates
    if monies: roles["money_fields"] = monies
    roles["_profile"] = prof
    return roles


def harvest(resource_ids, key, limit=1000):
    hits, reports = [], []
    for rid in resource_ids:
        seen_ids = set()
        rows = []
        for q in QUERIES:
            offset = 0
            while True:
                res = call("/datastore_search", {"resource_id": rid, "q": q,
                                                 "limit": limit, "offset": offset}, key)
                recs = (res.get("result") or {}).get("records") or []
                if not recs:
                    break
                rows.extend(recs)
                if len(recs) < limit:
                    break
                offset += limit
        if not rows:
            reports.append("resource %s → 0 rows" % rid)
            continue

        roles = detect_layout(rows)
        if "proj" not in roles or "winner" not in roles:
            reports.append("🔴 resource %s → detect layout ไม่ได้ (proj=%s winner=%s) ข้ามไฟล์นี้"
                           % (rid, roles.get("proj"), roles.get("winner")))
            continue

        kept = 0
        for r in rows:
            w = str(r.get(roles["winner"], "") or "").strip()
            tin = str(r.get(roles.get("tin", ""), "") or "").strip()
            if w not in ENTITY_MAP and tin not in OUR_TINS:
                continue
            pid = str(r.get(roles["proj"], "") or "").strip()
            if not pid or pid in seen_ids:
                continue
            seen_ids.add(pid)
            r["__resource"] = rid
            r["__roles"] = roles
            hits.append(r)
            kept += 1
        reports.append("resource %s → rows %d · เก็บ %d · layout proj=%s winner=%s tin=%s"
                       % (rid, len(rows), kept, roles["proj"], roles["winner"], roles.get("tin")))
    return hits, reports


def to_seed_rows(hits, existing_ids, seq_start):
    out, skipped = [], 0
    for h in hits:
        roles = h["__roles"]
        pid = str(h[roles["proj"]]).strip()
        if pid in existing_ids:
            skipped += 1
            continue
        w = str(h.get(roles["winner"], "") or "").strip()
        dates = sorted({th_to_iso(str(h.get(f, "") or "")) for f in roles.get("date_fields", [])} - {""})
        monies = sorted({float(h[f]) for f in roles.get("money_fields", []) if RE_MONEY.match(str(h.get(f, "") or ""))})
        out.append({
            "id": pid,
            "name": "",                       # ต้องดึงจาก field ข้อความยาว — ตรวจมือ
            "date": dates[0] if dates else "",
            "agency": "",                     # ต้องตรวจมือ (ชื่อหน่วยงานสลับช่องบ่อย)
            "province": "",
            "budget": "",                     # ❌ ชุดข้อมูลนี้ไม่มี งบประมาณ
            "midPrice": monies[-1] if len(monies) >= 2 else "",
            "bid": monies[0] if monies else "",
            "pct": "",                        # ❌ ต้องมี budget ก่อน  pct=(1-bid/budget)*100
            "entity": ENTITY_MAP.get(w, ""),
            "entity_raw": w,
            "status": "",
            "status_raw": str(h.get(roles.get("status", ""), "") or ""),
            "plant": "",                      # ❌ ไม่มีในข้อมูลรัฐ
            "workType": "",                   # ❌ ไม่มีในข้อมูลรัฐ
            "fiscalYear": "",
            "contractNo": str(h.get(roles.get("contractNo", ""), "") or ""),
            "signedOn": dates[0] if dates else "",
            "endsOn": dates[-1] if len(dates) > 1 else "",
            "resource": h["__resource"],
        })
    out.sort(key=lambda r: (r["signedOn"] or "9999", r["id"]))
    for i, r in enumerate(out):
        r["seq_suggest"] = seq_start + i
        y = (r["signedOn"] or r["date"] or "")[:7]
        if y:
            yy, mm = y.split("-")
            r["fiscalYear"] = int(yy) + 1 if int(mm) >= 10 else int(yy)
    return out, skipped


def load_existing_ids(seed_path):
    if not os.path.exists(seed_path):
        return set(), 0
    s = open(seed_path, encoding="utf-8").read()
    arr = json.loads(s[s.index("["):s.rindex("]") + 1])
    return {str(r.get("id")) for r in arr}, max((r.get("seq") or 0) for r in arr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", help="dataset id/name → enumerate resources ให้เอง")
    ap.add_argument("--resources", help="resource_id คั่นด้วย comma")
    ap.add_argument("--seed", default="seed_bids.js")
    ap.add_argument("--out-prefix", default="_handoff_OPY_egp_pull")
    ap.add_argument("--stamp", required=True, help="YYYYMMDD ใส่เอง (กัน timezone เพี้ยน)")
    a = ap.parse_args()

    key = api_key()
    if a.resources:
        rids = [x.strip() for x in a.resources.split(",") if x.strip()]
    elif a.dataset:
        res = call("/package_show", {"id": a.dataset}, key)
        rids = [r["id"] for r in (res.get("result") or {}).get("resources", [])]
        print("พบ resource %d ไฟล์" % len(rids))
    else:
        sys.exit("❌ ต้องระบุ --dataset หรือ --resources")

    existing, maxseq = load_existing_ids(a.seed)
    print("seed_bids: %d records · seq สูงสุด %d" % (len(existing), maxseq))

    hits, reports = harvest(rids, key)
    rows, dup = to_seed_rows(hits, existing, maxseq + 1)

    out_csv = "%s_%s.csv" % (a.out_prefix, a.stamp)
    out_txt = "%s_%s_report.txt" % (a.out_prefix, a.stamp)
    if rows:
        with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)

    lines = reports + [
        "",
        "ตรงกับห้างเรา (unique project) : %d" % len(hits),
        "มีใน seed_bids แล้ว (ข้าม)      : %d" % dup,
        "ของใหม่ที่ต้องเพิ่ม            : %d" % len(rows),
        "seq ที่เสนอ                    : %d - %d" % ((rows[0]["seq_suggest"], rows[-1]["seq_suggest"]) if rows else (0, 0)),
        "",
        "❌ ช่องที่ชุดข้อมูลนี้ไม่มี ต้องเติมมือ: budget · pct · plant · workType",
        "⚠️ name / agency / province เว้นว่างไว้ตั้งใจ — ชื่อคอลัมน์ฝั่งรัฐเลื่อน ต้องตรวจตาก่อนใส่",
        "⚠️ สคริปต์นี้ไม่แก้ seed_bids.js — insert เป็นงาน OPY",
    ]
    open(out_txt, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("\n→ %s\n→ %s" % (out_csv, out_txt))


if __name__ == "__main__":
    main()
