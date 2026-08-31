# 🎨 UI/UX Customize Agent
> เรียกสั้นว่า "UI" (แจ้งจาก DP 2569-07-27)

## 🎯 Role
Senior UI/UX Designer — ปรับ UI/UX ของ `rmn_ebidding_tracker_2.html` เท่านั้น
ไม่ยุ่งกับ data/logic/API/seed_bids

## 📋 My Tasks (this session)
### ✅ Done (prev sessions)
- เพิ่ม widget "โครงการที่อัพเดทสถานะล่าสุด" (Dashboard + Records)
  - Layout: Timeline style · Badge: prevStatus→curStatus
  - Container: max-height 284px + scrollbar
  - Filter: decided-only (ชนะ/มีสัญญา/แพ้/ยกเลิก) — ไม่แสดงรอผล
- Fix card border: `rgba(255,255,255,.09)` → `var(--card-border)` (su widget + bid timeline)
- Fix file truncation (restore 2515→2680 lines)

### ✅ Done (2026-06-17)
- SME card: เปลี่ยนจาก "วงเงิน SME / 300M" → "ยอดงานที่ชนะต่อห้าง"
  - filter: WINNER | CONTRACT เท่านั้น · bar: relative to max winner · สีเขียว
  - line 648 (title) + line 1838-1862 (logic)
- Fix date typo: `seed_bids.js` line 178 seq45 อบต.ภารแอ่น
  - `"5667-05-10"` → `"2567-05-10"` (timeline header แสดง "5667" ผิด)

### ✅ Done (2026-07-15)
- Verified: light mode toggle + timeline load-more were already implemented (stale pending items, no code change needed)
- FIX 7 phase 2 — one-off structural styles (3 fixes):
  - Added `--tag-bg` var (root L21 / dark L34): light `rgba(0,0,0,.04)`, dark `rgba(255,255,255,.06)`
  - L1142: `color:#155724` → `var(--green)` (sum_price_agree cell, was illegible in dark mode)
  - Entity-tag pills L1479,1532,1540,1666: `rgba(255,255,255,.06/.04/.09)` → `var(--tag-bg)` (was invisible in light mode)
  - L1821-1822 kpi-label: `#7a7872`/`#8a8880` → `var(--muted)`

### ✅ Done (2569-08-09)
- ซ่อน UI เช็ค/ส่ง email ทั้งหมด (workflow เปลี่ยน: จ่ายค่าเอกสารพร้อมยื่นประมูลเลย ไม่ต้องส่ง email ยืนยันอีก) — ไม่แตะ emailSent field ใน doc_fees.json/DOC_FEES array
  - renderDashDocFee (Dashboard widget): ลบปุ่ม toggle email + chip "รอส่ง", ยุบเหลือ filter เดียว (unpaid), ลบ dead var `_dashDocFeeFilter`, `unsentEmail`
  - renderDocFeeTab (Doc Fee tab): ลบ stat box "รอส่ง email" + ปุ่ม toggle email ต่อการ์ด
  - renderDocFeeBlock (project detail modal): ลบปุ่ม toggle email
  - `toggleDocFeeEmail()` function ยังอยู่ (ไม่มีปุ่มเรียกแล้ว — เก็บไว้เผื่อย้อนกลับ ไม่ลบเพื่อลด risk)
- (ต่อ) ซ่อนที่เหลือเพิ่ม: Add Bid form dropdown "สถานะ Email ยืนยัน" (L831) + emailTo display ใน Doc Fee tab (L2024) — ใช้ `style="display:none"` ไม่ลบโค้ด เพื่อ unhide ได้ทันทีถ้า workflow เปลี่ยนกลับ (ตามคำสั่ง user)

### ✅ Done (2026-08-25)
- เพิ่ม tab "🏗️ Assets" (read-only) — L656(button), L806-822(section+filters), L1164-1167(ASSETS const), L1215(TABS), L1229-1234(navigate), L2062-2160(renderAssets + helpers), L2447(expose), L2627-2639(fetch assets.json sync, pattern เดียวกับ doc_fees.json, 404-safe, filter pii:true ที่ ingestion)
- ไม่แตะ assets.json/personnel.json/seed_bids.js/doc_fees.json ตาม scope · commit 344fbb8 pushed เอง (user อนุญาตรอบนี้)
- 🐛 fix (968de1f): DA generate assets.json มาเป็น `{meta, assets:[]}` envelope ไม่ใช่ bare array ตามที่คุยกันตอนแรก — เจอตอนตรวจ data จริงหลัง DA push (0bda2ab) เลยแก้ fetch handler ให้รองรับทั้งสองแบบ (`Array.isArray(data) ? data : data?.assets`)

### ⏳ Pending UI tasks
- (none currently open — Assets tab live, verified working end-to-end against real assets.json)

### 🗒️ Context carried over (not a UI task, FYI for continuity)
- Mark กำลังคิดสถาปัตยกรรมใหญ่: แยกเป็น 2 BASE — "E-BIDDING BASE" (ของเดิม, public) vs "RMN DATABASE" (Employees/Stats-KPI/Asset+expiry/เอกสารสแกนจริง, ต้อง login ID/Pass, มี PII)
- แนะนำ Supabase ไปแล้ว (Postgres+Auth+Storage, free tier พอใช้ตอนนี้, Pro $25/mo ถ้าโต) — ยังไม่ตัดสินใจ/ยังไม่เริ่มสร้าง
- ถ้า session หน้าคุยเรื่องนี้ต่อ: นี่เป็น infra decision ข้าม repo (พาดพิง PII → ต้องเป็น DA เป็นคน design schema ก่อน ไม่ใช่ UI agent ทำเอง)

## 🚫 Out of Scope
- seed_bids.js / data logic / API calls
- assets.json / personnel.json / doc_fees.json (ข้อมูล — DA/Fee Payment Agent ดูแล)
- TaskCreate / AskUserQuestion

## 📁 Files I touch
- `rmn_ebidding_tracker_2.html` (primary)
- `seed_bids.js` (data typo fixes only)
- `WRK_AGENTS/WRK_UIUX.md` (session log — ตัวนี้)

## 📂 Working folder ที่ต้อง connect
- `RMN-eBidding-Workflow` (OneDrive) — repo หลัก มี tracker + WRK_AGENTS/ + seed_bids.js + assets.json/doc_fees.json (fetched, read-only ฝั่งฉัน)
- ไม่ต้องใช้ `RMN-eBidding-KB` (private repo, personnel.json) — UI agent ไม่ควรแตะ PII เลย

## ⚙️ My Rules
- Diff/changelog only — ห้าม output full file
- grep/Read หา section ก่อน — ห้าม Read ทั้งไฟล์รวด
- คำนวณ context ก่อน Edit — ถ้าไม่พอ แจ้ง user
- Verify end-of-file + line count หลัง Edit ทุกครั้ง (ป้องกัน truncation)
- Git commit+push เองผ่าน Windows-MCP PowerShell (ลบ .git/HEAD.lock, .git/index.lock ก่อนทุกครั้ง) — ห้ามส่ง git command ให้ user รัน [[feedback_git_push_format]]
- ก่อน commit เช็ค `git status` เสมอ — ถ้ามีไฟล์อื่นค้าง (ไม่ใช่ไฟล์ที่ฉันแก้) ห้ามแตะ/commit รวม เดี๋ยว agent อื่นเสียงาน (พบเคสจริง 2026-08-25: `.gitignore` + `WRK_MAPMAKER.md` ค้างจาก Mapmaker agent ระหว่าง session นี้ — ข้ามไป ไม่ยุ่ง)
