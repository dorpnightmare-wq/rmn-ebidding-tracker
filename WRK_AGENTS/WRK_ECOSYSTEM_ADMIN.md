# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-08-24 #3 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 🔄 Session State (2026-09-04 — DA: แก้ scheduled task ที่รายงานผิด)
> user ส่งรายงาน CONTEXT USAGE CHECKER ที่บอก "ตรวจไม่ได้ — ไม่พบ session ของ agent ทั้ง 7 ตัว" → สั่ง `Update ให้หน่อย`

### 🔎 หาต้นตอได้ ไม่ใช่ระบบพัง
- `list_triggers` (MCP) = **ว่างเปล่า** → scheduled task ไม่ได้อยู่ฝั่ง MCP · อยู่ local ที่ `%USERPROFILE%\Documents\Claude\Scheduled\` **4 ตัว**
- อ่าน `morning-agent-context-check\SKILL.md` (3,474 B) → **pattern จับชื่อ session ล้าสมัยทั้งชุด**
  - หา `DOC.` (ปลดแล้ว) · `session ที่มีคำว่า API status` (disabled) · `Datacenter Admin` · เขียน "fuzzy กับ agent ทั้ง 7 ตัว"
  - แต่ชื่อ session จริงตอนนี้เป็น **ชั้นยศ**: `[ Sir. OPY ]` · `[ DA ]` · prefix `RMN e-Bidding WorkFlow /`
  → **จับไม่ตรงเลยแม้แต่ตัวเดียว** = สาเหตุจริงที่รายงานว่า "ตรวจไม่ได้" · ตัว checker ทำถูกที่ไม่เดาตัวเลข

### ✅ แก้แล้ว (3,474 → 6,119 B · backup `SKILL.md.bak_20260904`)
- **5 agent** (DA·OPY·EXP·MM·UI) + ประกาศชัดว่า DOC/API/DB ยกเลิก **ห้ามหา ห้ามรายงาน**
- pattern ใหม่รับทั้งชั้นยศและชื่อเก่า: `[ Sir. XX ]` · `[ XX ]` · `[ Lord DA ]` · `Datacenter Admin` · ตัด prefix ก่อนเทียบ
- skip list เติม `Rmn_documentation expire_date checker` · `context check` · ชื่อที่มี `DOC.`/`API status`/`DB`
- **เพิ่มขั้นที่ 5:** ถ้าไม่เจอ session เลย → รายงาน "ตรวจไม่ได้" + **แนบรายชื่อ session ที่เจอจริง** เพื่อให้ DA แก้ pattern ได้ทันที · ห้ามสรุปว่าระบบพัง ห้ามสั่ง Restart
- ตรวจอีก 3 ตัว: `gmail-bid-auto-update` สะอาด · `doc-fee-morning-alert` + `rmn_documentation-expire_date-checker` คำว่า DOC เป็นชื่อไฟล์/`document` **ไม่ใช่ agent ที่ปลด** → ไม่ต้องแก้

### 📌 บทเรียนเชิงโครงสร้าง
SKILL.md อยู่นอก git → เปลี่ยน registry 3 รอบ (DB·DOC·ชั้นยศ) ไม่มีใครไล่แก้ → ระบบเตือนรายงานผิดเงียบๆ
→ เพิ่มตาราง scheduled tasks เข้า **File Ownership Matrix** (เจ้าของ = Lord DA) + กฎ **เปลี่ยน registry ต้องไล่ตรวจ SKILL.md ทั้ง 4 ตัวในรอบเดียว**
→ วิธีแก้ไฟล์ที่ใช้ได้จริง: **PowerShell + base64 decode + backup ก่อนเขียน** (ส่ง Thai ตรงๆ ใน command = เพี้ยน)
⏸️ **ยังค้าง:** จะ copy SKILL.md ทั้ง 4 เข้า git เป็นสำเนาอ่านอย่างเดียวไหม (คำถามค้างจาก `DESIGN_PRINCIPLES.md` — ยังไม่ตัดสิน)

### ✅ บันทึก 2026-09-04 #2 — checker → Work Health (Lord Commander รับรอง)
- `SKILL.md` **6,119 → 8,108 B** · backup `SKILL.md.bak_20260904` (3,474 ต้นฉบับ) + `.bak_20260904b` (6,119 รอบก่อน)
- **เลิกทั้งหมด:** `list_sessions` · `read_transcript` · นับ turn/context · สั่ง Restart agent
- **read-only 100%:** อนุญาต `git status` · เทียบ HEAD/origin จาก local · ขนาด/mtime/grep · ⛔ ห้าม commit/push/pull/fetch/แก้ไฟล์ · เฉพาะ 3 repo ใน registry
- วัด ①git status ②HEAD vs origin ③ขนาด WRK vs 20 KB (เตือนที่ 80% ก่อนชน) ④mtime (14 วัน 🟠 / 30 วัน 🔴 ตายเงียบ) ⑤grep pending ทั้งระบบ
- ฝัง **Owner map** ลงใน skill → รายงานบอก owner ได้เองโดยไม่ต้องเปิด matrix
- ชื่อโฟลเดอร์/`name:` **คงเดิม** `morning-agent-context-check` — เป็น identity ที่ scheduler ผูก · ยังไม่ยืนยันว่า rename ปลอดภัย · ชื่อในเอกสารทุกที่ = **Work Health Check**
- ตรวจหลังเขียน: `Work Health Check ✓` `read-only 100% ✓` `ห้าม list_sessions ✓` `Owner map ✓` `ไม่มี turn threshold เดิม ✓`

### ✅ ปิดคำถามค้างตั้งแต่ 08-25
**จะ copy SKILL.md เข้า git ไหม → ไม่** (มติ Lord Commander) เพราะสร้าง source of truth ซ้ำ
✅ แนวทางที่รับรอง: **git = canonical → deploy ทางเดียวมา `Documents\`** + hash check + rollback
⏸️ **ยังไม่ทำ** — ต้องเสนอเป็นงานระบบแยกพร้อมวิธี deploy/ตรวจ hash/rollback ก่อนลงมือ

