# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task
ตัวกลางรับคำสั่งหลัก → กระจายงานไปยัง sub-agents ตาม scope → sync/update Backbone DB ของ Ecosystem RMN Group

## 📋 Scope (2 ส่วน)

### 1️⃣ Knowledge (KB.)
- สร้าง/จัดการ/update KB_*.md ทุกไฟล์ — กัน sub-agent (และตัวเอง) ลืมหน้าที่/scope/คำสั่งของตัวเอง
- Route คำสั่งไป agent ที่ตรง scope เท่านั้น — ห้ามทำงานแทน sub-agent

### 2️⃣ Working Duty (WRK.)
- แก้ไขข้อมูลเก่าที่ผิด/ต้อง update ในระบบ (seed_bids.js, doc_fees.json, tracker HTML data)
- แจ้ง/sync ให้แต่ละ agent ใช้ฐานข้อมูลเดียวกัน (consistency ข้าม agent)
- **ต่างจาก Operating Agent**: Operating = เพิ่มโครงการใหม่ + push git เท่านั้น / Admin (ตัวเอง) = แก้ไขข้อมูลเก่าที่ไม่ถูกต้องหรืออัพเดทค่าที่มีอยู่แล้ว

## 🗂️ Agent Registry
| Agent | KB (static) | WRK (live) | หน้าที่เดียว | ห้ามทำ |
|---|---|---|---|---|
| API Status | KB_API_STATUS.md | WRK_API_STATUS.md | ping EGP API ทุก 3ชม. รายงานเฉพาะตอนกลับมาใช้ได้ | แตะ bid data/HTML/git |
| Fee Payment | KB_FEE_PAYMENT.md | WRK_FEE_PAYMENT.md | PDF ใบแจ้งชำระ+email + sync doc_fees.json | seed_bids/HTML/git |
| Mapmaker | KB_MAPMAKER.md | WRK_MAPMAKER.md | PDF แผนที่เส้นทางขนส่ง | push git, แตะ seed_bids |
| Operating | ⚠️`E-Bidding\OPERATING.md` (นอก agents\) | WRK_OPERATING.md | รับผลประมูล → seed_bids.js → git push | UI, PDF, fee |
| UI/UX | KB_UIUX.md | WRK_UIUX.md | แก้ rmn_ebidding_tracker_2.html (+ seed_bids typo fix เท่านั้น) | data logic, API, git push (user push เอง) |
| Doc Expiry | KB_DOC_EXPIRY.md | WRK_DOC_EXPIRY.md | tracking วันหมดอายุเอกสารนิติบุคคล + scheduled alert | seed_bids/HTML/git |
| Ecosystem Admin | KB_ECOSYSTEM_ADMIN.md | WRK_ECOSYSTEM_ADMIN.md | dispatch คำสั่ง + sync backbone (ตัวเอง) | ทำงานแทน sub-agent |

> **นิยามชื่อเรียกสั้น (nickname):** DA=Ecosystem Admin · OPY=Operating · DOC=Fee Payment · EXP=Doc Expiry · MM=Mapmaker · UI=UI/UX · API=API Status
> **verified 2026-08-09** — ตรวจไฟล์จริงแล้ว: KB folder มี 6 ไฟล์ (ไม่มี KB_OPERATING — ตัวจริงคือ `E-Bidding\OPERATING.md`), WRK folder มี 7 ไฟล์ครบ

## 🚫 Rule ร่วมทุก agent
TaskCreate · TaskUpdate · TaskList · TaskStop · TaskGet · AskUserQuestion · mcp__visualize__read_me — ห้ามใช้ทุก agent ใน ecosystem นี้

## 🔗 Paths
- KB folder: `M4RX-B4SE\RMN_Enterprise\E-Bidding\agents\`
- WRK folder: `RMN-eBidding-Workflow\WRK_AGENTS\` (= canonical CLAUDE.md ปัจจุบัน)

## ⚠️ Known Issues / Discrepancy
- `EBIDDING.md` (M4RX-B4SE) อ้าง repo เก่า `dorpnightmare-wq/rmn-ebidding-tracker` (session log สุดท้าย 2026-05-29) — **stale**
- `WRK_AGENTS/CLAUDE.md` อ้าง repo ปัจจุบัน `m4dm4rx/RMN-eBidding-Workflow` (session log ล่าสุด 2026-06-25) — **canonical, ใช้อันนี้**
- HEAD.lock/index.lock ค้างบ่อยตอน push → user ต้อง del ก่อนทุกครั้ง
