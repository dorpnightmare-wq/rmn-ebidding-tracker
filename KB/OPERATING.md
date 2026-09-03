# E-bidding Operating Assistance

## 🎯 Task Scope
รับข้อมูลการประมูล → เพิ่ม/แก้ไข `seed_bids.js` → git push

---

## 📋 Current Seq Status
> ❌ ห้าม hardcode ตาราง seq ที่นี่ (เคยมีตารางค้างที่ seq 94-102 ล้าหลัง 75 รายการ — ลบแล้ว 2026-08-13)
> ✅ อ่านจาก `seed_bids.js` เสมอ = source of truth
> หา seq ถัดไป: กรอง `fiscalYear` ล่าสุด → `max(seq) + 1`
> `fiscalYear` คำนวณจาก field `date` (วันประกาศ) — เดือน ≥ ต.ค. → ปี+1


---

## ⏳ Pending
- ไม่มี

## ✅ Done This Session
- seq 94–95 added (26 พค.69)
- seq 96–98 fixed road codes + midPrice/lowest (28 พค.69)
- seq 99–100 fixed name/status + midPrice/lowest (29 พค.69)
- seq 101 added (29 พค.69 บ่าย)
- seq 102 added + lowest confirmed (2 มิ.ย.69 บ่าย)

---

## 🔀 Data Entry Rules
- pct = `round((budget - bid) / budget * 10000) / 100`
- ต่ำสุด → `"รอผลพิจารณา [ เป็นผู้เสนอต่ำที่สุด ]"`
- ไม่ต่ำสุด → `"รอผลพิจารณา [ ไม่ได้เป็นผู้เสนอต่ำที่สุด ]"`
- ผลเช้า → 12:01 · ผลบ่าย → 16:01

## 🧬 Entry Schema — template บังคับ (เพิ่ม 2569-08-13 ตามที่ DA แจ้ง)
ทุก record ที่เพิ่มใหม่ **ต้องมี `fiscalYear` เสมอ** (เดิม template ไม่มี field นี้ → เกิด record ขาด 143 ตัว DA ต้องมาไล่เติมย้อนหลัง)

```js
{"seq": N, "id": "69XXXXXXXXX", "name": "...", "agency": "...", "province": "...",
 "budget": 0, "bid": 0, "pct": 0.00, "entity": "หจก.รักดี การโยธา",
 "status": "รอผลพิจารณา", "date": "2569-MM-DD", "midPrice": 0.00,
 "workType": "เสริมผิว", "plant": "มหาสารคาม", "fiscalYear": 2569}
```

**กฎคำนวณ `fiscalYear`** (ปีงบไทยเริ่ม 1 ต.ค.) — คำนวณจาก field **`date` (วันประกาศ)** เท่านั้น:
- เดือนของ `date` ≥ 10 (ต.ค.–ธ.ค.) → `fiscalYear = ปีของ date + 1` (เช่น `2568-10-15` → **2569**)
- เดือนของ `date` 01–09 → `fiscalYear = ปีของ date` (เช่น `2569-08-07` → **2569**)

> ⚠️ **แก้ไข 2569-08-13 (override กฎเดิม):** ห้ามคำนวณจากเลข `id` — id เข้ารหัส **เดือนที่ขึ้นระบบ e-GP** ซึ่งไม่ตรงกับวันประกาศจริงใน 26 records (DA ตรวจพบ) ยึด `date` เป็น source of truth เสมอ

- ห้ามละ field นี้แม้เพิ่ม record เดียว — ตรวจก่อน commit ทุกครั้ง

---

## 🔄 Doc Fee — Full Workflow (STRICT ORDER)
> 🔁 **เปลี่ยนเจ้าของ 2026-09-02: OPY ทำเองทั้งเส้น** ผ่าน skill `fee-payment` — ไม่ต้อง dispatch ไป DOC ไม่ต้องรอ agent อื่นปิด entry
> เหตุผล: DOC ไม่มีคนเปิด session ให้เลย (WRK_FEE_PAYMENT.md แก้ครั้งสุดท้าย 04-08-69) · OPY มี skill + push ได้เอง → queue ค้างที่ขั้น "รอ DOC ปิด" ตายเงียบ
> OPY อ่าน PDF → เขียน `doc_fee_queue.json` → จ่าย/ตรวจสลิป → **ปิด entry เข้า `doc_fees.json` เอง** → push เอง

**เปิด session ทุกครั้ง → อ่าน queue ก่อน:**
```python
import json, os
queue_path = "doc_fee_queue.json"  # ใน RMN-eBidding-Workflow/
queue = json.load(open(queue_path)) if os.path.exists(queue_path) else []
pending = [x for x in queue if x.get("status") == "pending"]
print(f"Queue: {len(pending)} pending")
for p in pending:
    print(f"  {p['id']} {p['agency']} {p['amount']}บ window={p['payWindowStart']}~{p['payWindowEnd']}")
```
เสร็จแต่ละรายการ → mark `"status": "done"` + save + แจ้ง user push

```
1. อ่าน doc_fee_queue.json → แสดง pending ทั้งหมด
2. อ่าน entity จาก seed_bids.js (local — ไม่ต้องรอ git push)
3. รอ user ส่งสลิป
4. Slip Verification (ห้ามข้าม — แสดงตารางผล match ให้ user ยืนยันก่อน)
   ✅ ธนาคาร / ✅ เลขบัญชี / ✅ ชื่อบัญชีผู้รับ
   ✅ ยอดเงิน / ✅ วันที่ (อยู่ใน payWindow) / ✅ ชื่อผู้ฝาก = entity
   └─ มีจุดใด ❌ → หยุด แจ้ง user ทันที
5. User ยืนยัน → output: 📄 **PDF ใบแจ้งชำระเงิน**
   ช่องทางส่งหลักฐาน default = **แนบเข้า e-GP** (ยืนยันจาก user 2569-09-02 "No email from now on")
   └─ Email text + Email Check Box widget → ทำเฉพาะเมื่อหน่วยงาน**ระบุให้ส่งอีเมล** เท่านั้น
6. รอ user แจ้ง "ส่งแล้ว"
7. หลัง user confirm → **OPY อัป doc_fees.json เอง** (paidDate + submitMethod) → **push เอง**
```
**⚠️ ห้าม output PDF/Email ก่อน user ยืนยัน slip verification**
**⚠️ ห้าม อัป doc_fees.json ก่อน user แจ้ง "ส่งแล้ว"**
**⚠️ ถ้าหน่วยงานระบุให้ส่งอีเมล → Email Check Box ต้องมาพร้อม PDF + Email text เสมอ (interactive widget ห้ามใช้ markdown ☐)**

## 🔍 Slip Verification (MANDATORY — ก่อน generate PDF ทุกครั้ง)
ต้อง output ตารางนี้และรอ user ยืนยันก่อนเสมอ — ห้าม generate PDF โดยไม่ผ่านขั้นตอนนี้

| จุดตรวจ | ค่าจากสลิป | ค่าจากประกาศ | ✅/❌ |
|---|---|---|---|
| ธนาคาร | | | |
| เลขบัญชี | | | |
| ชื่อบัญชีผู้รับ | | | |
| ยอดเงิน | | | |
| วันที่โอน | | อยู่ในช่วง payWindow? | |
| ชื่อผู้ฝาก/entity | | ถูก entity ที่ยื่นงาน? | |

**⚠️ ชื่อผู้จ่ายในสลิป ต้องตรงกับห้างที่ยื่นงาน (ดูจาก seed_bids entity)**
- ถ้าไม่ตรง → แจ้ง user ทันที: "ผู้จ่ายในสลิป (X) ≠ ห้างที่ยื่นงาน (Y) — หน่วยงานอาจปฏิเสธ ดำเนินการต่อ?"
- ห้าม generate PDF โดยไม่ได้รับการยืนยัน

**ถ้ามีจุดไหน ❌ → ห้าม generate PDF แจ้ง user ทันที**
เพราะถ้าผิดตรงไหนซักจุด = email ผิด = ถือว่าไม่ได้จ่าย

## ✍️ Email Signature Rules
| นิติบุคคล | ชื่อ | ตำแหน่ง |
|---|---|---|
| ห้างหุ้นส่วนทุกห้าง (RMN, รักดี, ร่วมค้า ฯลฯ) | นางอนุรักษ์ บารพรม | หุ้นส่วนผู้จัดการ |
| บจก. ตักสิลา RMN | นางอนุรักษ์ บารพรม | กรรมการผู้จัดการ |

โทร. 087-223-5093 (ทุกกรณี)
