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

### ⏳ Pending UI tasks
- (none currently open)

## 🚫 Out of Scope
- seed_bids.js / data logic / API calls
- Git push (user does manually)
- TaskCreate / AskUserQuestion

## 📁 Files I touch
- `rmn_ebidding_tracker_2.html` (primary)
- `seed_bids.js` (data typo fixes only)

## ⚙️ My Rules
- Diff/changelog only — ห้าม output full file
- grep/bash หา section ก่อน — ห้าม Read ทั้งไฟล์
- คำนวณ context ก่อน Edit — ถ้าไม่พอ แจ้ง user
- Verify end-of-file หลัง Edit ทุกครั้ง (ป้องกัน truncation)
