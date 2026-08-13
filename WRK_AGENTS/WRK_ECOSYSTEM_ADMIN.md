# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB

## 🔄 Session State (2026-07-01)
### ✅ Done
- สร้าง KB/WRK pointer pair (slug: ECOSYSTEM_ADMIN)
  - KB: `M4RX-B4SE\RMN_Enterprise\E-Bidding\agents\KB_ECOSYSTEM_ADMIN.md`
  - WRK: `RMN-eBidding-Workflow\WRK_AGENTS\WRK_ECOSYSTEM_ADMIN.md`

### ⏳ Pending
- (none)

## 🔄 Session State (2026-07-01, cont.)
### ✅ Done
- ศึกษา workflow ครบ 5 sub-agent (API Status / Fee Payment / Mapmaker / Operating / UI-UX) — scope + ห้ามทำ บันทึกใน KB_ECOSYSTEM_ADMIN.md
- พบ discrepancy: EBIDDING.md (repo เก่า) vs WRK_AGENTS/CLAUDE.md (repo ปัจจุบัน, canonical)
- นิยาม scope ตัวเอง 2 ส่วน: (1) KB — สร้าง/manage KB ทุก agent (2) WRK — แก้ไข/อัพเดทข้อมูลเก่าในระบบ + sync ให้ทุก agent ฐานข้อมูลเดียวกัน (ต่างจาก Operating ที่เพิ่มเฉพาะโครงการใหม่+push git)

## 🔄 Session State (2026-07-02 — WRK Data Correction: ห้างหุ้นส่วน RMN FY2565-68)
### ✅ Done
- Cross-check `seed_bids.js` (entity="ห้างหุ้นส่วน RMN", FY2565-68, 206 records) กับรายงานจัดซื้อจัดจ้าง e-GP จริง 4 ไฟล์ (342 unique id)
- Match by `id` (รหัสโครงการ) → overlap 195 records
- **Patched 184 records** ใน seed_bids.js (backup: `/tmp/work/seed_bids_backup.js` ใน sandbox — หมดตอนจบ session):
  - เติม `province` ที่ขาด: 158 records
  - แก้ `bid` ให้ตรงราคาที่ตกลงจ้างจริง: 21 records
  - แก้ `budget` ผิด: 4 records
  - แก้ id พิมพ์ผิด `57059022139` → `67059022139` (อบต.แกดำ, budget 0→820,000)

### ⏳ Pending — รอ user ตัดสินใจ
- **10 records ใน seed_bids ไม่พบใน e-GP report เลย** (ไม่ใช่ typo ธรรมดา) — ต้องตรวจสอบทีละตัว: 65107138294(อบต.หนองทุ่ม) 67039272259(ทต.หนองหาน) 67039415159(ทต.เขาพระนอน) 67069444218/67069446273(ทต.ทุ่งฝน) 67079652295(ทต.เชียงคาน) 67099119350(ทต.ร่องคำ) 67119300266(แขวงทางหลวงชนบทขอนแก่น) 68019418330(ทต.ขามเรียง) 67029268868(ทต.อูบมุง)
- **146 records ใน e-GP report ไม่มีใน tracker**: 85 จ้างก่อสร้าง (in-scope e-bidding — อาจต้องเพิ่ม) / 44 จ้างทำของ-จ้างเหมาบริการ / 17 ซื้อ (2 ประเภทหลังน่าจะนอก scope tracker) — รอ user ยืนยันว่าจะเพิ่มหรือไม่
- ยังไม่ push git (รอ user คอนเฟิร์ม)

### ✅ Done (2026-07-15 — 10 orphan records decision)
- ลบ 3 records ที่ user สั่ง [ลบ]: `67029268868`(ทต.อูบมุง) `67079652295`(ทต.เชียงคาน) `67099119350`(ทต.ร่องคำ)
- Total records: 395 → 392 (พบว่ามี 18 records ใหม่ถูกเพิ่มโดย Operating Agent ระหว่างช่วงที่รอ — ของเดิม 377 + typo id fix ไม่กระทบ)
- 7 records [เพิ่ม] = user เช็ค id ที่เว็บ e-GP โดยตรงแล้ว ยืนยันเป็นงานจริงของ หจก.RMN → **เก็บไว้ ไม่แก้ไข** (id ต่างจาก report ที่ user มี แต่ตรงกับ e-GP จริง — report ที่ user ให้มาอาจไม่ครบ 100%)
- 3 records [ลบ] = user ยืนยันไม่ใช่งานของ RMN — ลบถูกต้องแล้ว ✅ (ที่มาว่าทำไมเคยอยู่ใน tracker ยังไม่ทราบสาเหตุ — ตั้งข้อสังเกตไว้ เผื่อ Operating Agent เคย entity ผิดตอนบันทึก)
- **สรุป 10 orphans: ปิดเคสแล้ว** (7 keep + 3 deleted)

### ✅ Done (2026-07-15 — เพิ่ม 145 missing records)
- สร้าง HTML review list (sidebar filter type/FY) ให้ user ดูก่อน
- user: "บันทึกทั้งหมด" + "in scope บันทึกปกติ ส่วนอีก 2 ประเภทระบุ category ชัดเจน"
- เพิ่ม 145 records: 84 จ้างก่อสร้าง (schema ปกติ) + 44 จ้างทำของ/จ้างเหมาบริการ + 17 ซื้อวัสดุ (ทั้ง 2 ประเภทหลังมี field `"category"` กำกับ)
- seq ต่อจาก max เดิมของแต่ละ fiscalYear (scoped ต่อปี ไม่ใช่ global)
- **บักที่เจอ**: duplicate id 2 ตัว (66099063322, 66089543671) ของเดิมในไฟล์ — ลบตัวที่ stale (ไม่มี province/bid ผิด) ทิ้งแล้ว
- Total: 392 → 535 records (unique id ครบ, JSON valid)

### ✅ Done (2026-07-15 — full-file seq audit หลัง Operating Agent flag concern)
- Operating Agent ถามว่างานซ้ำซ้อนมั้ย → เช็คแล้ว: ไม่ทับกัน, คนละ scope (เขา=โครงการใหม่/push รายวัน, ผม=แก้/sync ข้อมูลเก่า)
- ตรวจ seq scheme: **seq scoped ต่อ fiscalYear เดิมอยู่แล้ว** (min=1 ทุกปีตั้งแต่ก่อนผมแตะ) — ไม่ใช่ inconsistency ใหม่ที่ผมสร้าง ตัว unique key จริงคือ `id` (รหัส e-GP) ไม่ใช่ seq
- Audit ทั้งไฟล์ (535 records ทุก entity) เจอบัค**ไม่เกี่ยวกับ RMN**: seq=30 ซ้ำใน FY2568 entity "กิจการร่วมค้า รักดี" (id 68029214741 กับ 68049301316) — renumber ตัวหลัง → seq 57 แล้ว
- Verify: ไม่มี duplicate seq ซ้ำใน fiscalYear ไหนแล้ว ทั้งไฟล์ 535 records

### ✅ Confirmed pushed
- `4adb66e` fix RMN FY2565-68 (province/bid/budget + 145 records + dedupe id)
- `3f75d24` fix dedupe seq=30 FY2568
- verified origin/main ตรงกับ local, seed_bids.js clean

### ⏳ Pending
- (none) — user confirm: ห้างอื่น (กิจการร่วมค้า RMN/รักดี/ตักสิลา) เพิ่งเริ่มใช้ระบบปีนี้ (FY2569) ไม่มีข้อมูลย้อนหลังให้แก้ → **ปิด task data-correction ทั้งชุดสมบูรณ์** ไม่ต้องรอ excel เพิ่มเติมสำหรับห้างอื่น

## 🔄 Session State (2026-07-16 — เอกสาร RAKDEE + ตราประทับ)
### ✅ Done
- สร้าง PDF "บัญชีรายชื่อผู้มีอำนาจควบคุม" หจก.รักดีการโยธา ตาม format RMN.pdf reference
  - ใช้ weasyprint (ไม่ใช้ reportlab — เจอบัค วรรณยุกต์ทับซ้อนกันตอนแรก, แก้แล้วเปลี่ยน engine)
  - เว้นลายเซ็น/ตราประทับว่าง, เลขอาราบิก, วันที่ 15 กรกฎาคม 2569, เลขบัตร ปชช. [REDACTED — ดู repo private RMN-eBidding-KB]
  - label=bold, ข้อมูลกรอก=regular ทั้งหมด, line-height 2.8
  - Final file: `[EGP]_E-BIDDING - [R.M.N_GROUP]_DATABASE\[ RAKDEE CIVIL ]\RMN\ผู้มีอำนาจควบคุม RAKDEE.pdf`
- Enhance ตราประทับ (stamp) หจก.รักดีการโยธา จากรูป screenshot → PNG หัวกระดาษ
  - Upscale 4x + denoise + sharpen + saturation boost, ทำพื้นหลังโปร่งใส (alpha)
  - แก้ tilt: หมุน -13.1° (คำนวณจาก diamond marker ซ้าย-ขวาให้ระดับเดียวกัน — วิธี: หา centroid ของ diamond ทั้ง 2 ฝั่งเทียบมุมกับจุดศูนย์กลางวงกลม)
  - ซ่อมจุดเส้นวงแหวนนอกที่บาง/ขาดใกล้ข้อความ "PARTNERSHIP" ล่าง — ใช้ polar unwrap (cv2.warpPolar, **columns=radius axis, rows=angle axis** — จุดสำคัญที่พลาดตอนแรกจนแก้ผิดตำแหน่ง ต้อง calibrate ด้วย marker point ก่อนเสมอ) แล้ว cross-fade เนื้อผ้า/สีจาก donor segment ข้างเคียงแทนที่ patch สีเรียบ (ให้คงลาย texture หมึกธรรมชาติ)
  - Final files (ทับของเดิม): `[EGP]_E-BIDDING - [R.M.N_GROUP]_DATABASE\[ RAKDEE CIVIL ]\RMN\RAKDEE_stamp_transparent.png` และ `RAKDEE_stamp_whitebg.png`

### 📌 Technique note (สำหรับใช้ครั้งหน้า — stamp/ตราประทับ อื่นๆ)
- Thai text ที่มีวรรณยุกต์ซ้อน → ต้องใช้ weasyprint (HTML/CSS→PDF ผ่าน Pango) ไม่ใช้ reportlab canvas
- แก้เส้นวงกลมที่ขาด/tilt บนตราประทับ → polar unwrap ด้วย cv2.warpPolar(dsize=(width,height)) โดย **width=รัศมี-axis, height=มุม-axis** (ทดสอบ calibrate ด้วยจุด marker เทียบตำแหน่งก่อนแก้จริงทุกครั้ง กันพลาดแกน)

### ⏳ Pending
- (none) — รอ user สั่งงานถัดไป (เอกสารนิติบุคคลอื่น หรือ entity อื่น)

## 🔄 Session State (2026-08-09 — nickname "DA", BOQ, RAKDEE docx, Khon Kaen checklist, cloud project migration)
### ✅ Done
- User สั่ง: เรียก agent นี้ว่า **"DA"** แทน "Ecosystem & Datacenter Admin Agent" เต็มๆ (บันทึกลง memory แล้ว [[feedback_da_nickname]])
- BOQ_1.xlsx: restructure column E-I ตามรูปที่ user ส่ง (ค่างานต้นทุน/Factor F/ราคากลาง/ราคาที่ปรับลด/ราคาต่อหน่วย) — verify ผ่าน LibreOffice render ตรงกับรูปเกือบ 100% (คลาดเคลื่อน 1 สตางค์ 2 จุดจาก rounding ปกติของ Excel)
- สร้าง "รายชื่อหุ้นส่วนผู้จัดการ RAKDEE.docx" ตาม format RMN.pdf + ข้อมูลจาก DBD #06-08-2569 (หุ้นส่วนผู้จัดการ 1 คน: นางอนุรักษ์ บารพรม, ทุนจดทะเบียนรวม 10,000,000)
  - **บั๊กเจอ**: floating image (ตราประทับทับลายเซ็น) ใช้ `relativeFrom: HorizontalPositionAlign.CENTER` ผิด — enum นี้ใช้ไม่ได้กับ `relativeFrom` (ต้องเป็น `page`/`paragraph`/`margin` ฯลฯ) ทำให้ Word เปิดไฟล์ไม่ได้ (แต่ LibreOffice ยังพอเปิดได้แบบ error-tolerant) แก้เป็น `HorizontalPositionRelativeFrom.PAGE` / `VerticalPositionRelativeFrom.PARAGRAPH` แล้ว validate ผ่าน (บันทึกเป็น technique note ด้านล่าง)
- สร้างเช็คลิสต์เตรียมตัว 2 งานอบรมขอนแก่น (Digital Construction Bootcamp + กรมทางหลวง DCS) ทั้ง docx และ interactive HTML widget
  - แก้ภาษาไทยหลายจุดตามที่ user สั่ง "ดูภาษาซิ" — เจอบั๊กจริง: cross-reference ผิดหมวด ("ดูหมวด 4" ที่จริงต้องเป็น "หมวด 2.2")
  - **แก้ความเข้าใจผิดสำคัญ**: เดิมสันนิษฐานว่าทะเบียนประเภท 4/6 เป็นของ ทช. — ตรวจจาก PDF ต้นฉบับจริงแล้วพบว่าเป็นของ **กรมทางหลวง (DOH)** ต่างหาก (บันทึกลง WRK_DOC_EXPIRY.md แล้ว) มีแค่บัตร Recycling บร.1-617/2567 เท่านั้นที่เป็น ทช. จริง
  - ยืนยันเลขทะเบียนนิติบุคคล RMN ที่ถูกต้อง: **0443561001307** (เอกสารเก่า 044361001307 ขาดเลข "5" ผิด) — บันทึกใน WRK_DOC_EXPIRY.md แล้ว
  - ทั้ง 2 งานลงทะเบียนสำเร็จแล้ว (Bootcamp + DCS ผ่านการตรวจสอบ 5 ส.ค. 69 โดยนายศุภกฤต บารพรม)
- **Cloud Project migration ปิดเคสแล้ว**: ปัญหาเดิม "ไม่เห็น RMN e-Bidding Workflow บนโน้ตบุ๊ก" ที่แท้จริงคือ**ไม่เคยเป็น cloud Project เลยทั้งคู่** (ทั้งที่ PC และ laptop เห็น path-pin local) → สร้าง Project ใหม่ชื่อ "RMN e-Bidding WorkFlow" ผ่านหน้า Projects สำเร็จแล้วบน PC (เห็นแชท Datacenter Admin/UI./OPY/MM./DOC. ครบ), ลบ pin เก่าที่ laptop ทิ้งแล้ว — เหลือรอ sync ขึ้น laptop (คนละบัญชีไม่ใช่สาเหตุ ทั้งคู่ login "Mark" เหมือนกัน) แนะนำให้ restart แอปที่ laptop ถ้ายังไม่ขึ้น
- สำรอง memory ทั้งหมด + scheduled tasks (2 ตัว: morning-agent-context-check, rmn-doc-expiry-check) ไว้ที่ `WRK_AGENTS\MEMORY_BACKUP_2026-08-09.md` และร่าง Project Instructions ไว้ที่ `WRK_AGENTS\PROJECT_INSTRUCTIONS_DRAFT.md`

### 📌 Technique note (docx-js floating image — stamp/ตราประทับทับลายเซ็น)
- ใช้ `floating.horizontalPosition.relative` / `verticalPosition.relative` ต้องเป็น `HorizontalPositionRelativeFrom` / `VerticalPositionRelativeFrom` enum (ค่าเช่น `page`, `paragraph`, `margin`) **ห้ามใช้ `HorizontalPositionAlign`/`VerticalPositionAlign`** (นั่นคือ enum สำหรับ `align` ไม่ใช่ `relative` — ใส่ผิดที่ทำให้ Word เปิดไฟล์ไม่ได้เงียบๆ โดย LibreOffice ยังพอ render ได้ ต้องรัน `validate.py` เช็ค XSD ก่อนส่งทุกครั้งที่มี floating image)

### ⏳ Pending
- ~~ยืนยัน project sync ขึ้น laptop~~ / ~~เชื่อมโฟลเดอร์ที่ laptop~~ → **ปิดเคสแล้ว** ดู correction ด้านล่าง (project ไม่ sync โดยธรรมชาติ ต้องสร้างเองที่ laptop ซึ่งทำเสร็จแล้ว)

## 🔄 Session State (2026-08-09 cont. — ❌ CORRECTION: cloud project migration ไม่จริง)
### ❌ แก้บันทึกที่ผิดของรอบก่อน
- บันทึกเดิมว่า "สร้าง Project ใหม่ชื่อ RMN e-Bidding WorkFlow ผ่านหน้า Projects สำเร็จแล้วบน PC" — **ไม่จริง**
- ตรวจสอบจริงผ่าน browser (claude.ai/projects, login บัญชี Suphakrit Barap… Pro plan) → มี project เดียวคือ **"MY PERSONAL TOOLS"** เท่านั้น ไม่มี RMN e-Bidding WorkFlow
- สิ่งที่มีอยู่จริงคือ **Cowork project** (คนละระบบกับ claude.ai Projects — Cowork เป็นเมนูแยกใน sidebar) → **local ต่อเครื่อง ไม่ sync ข้ามเครื่อง** จึงไม่มีวันขึ้นที่ laptop เอง
- ระหว่างตรวจ: user เผลอกด logout ทุกเครื่อง (ไม่เกี่ยวกับปัญหานี้)

### 📌 ข้อสรุป/นโยบายที่ตัดสินใจแล้ว — เลือก A: คง Cowork ไม่สร้าง cloud Project
เหตุผล:
1. State จริงอยู่ในไฟล์ (WRK_*.md / CLAUDE.md / seed_bids.js บน OneDrive) ซึ่ง sync ข้ามเครื่องอยู่แล้ว — เปิด session ใหม่สั่ง "DA — resume" ได้ context ครบ สิ่งที่ขาดคือประวัติแชทเท่านั้น
2. cloud Project **ต่อโฟลเดอร์ local ไม่ได้** — งาน 90% ของ ecosystem (git push / seed_bids / PDF) ต้องใช้ folder access
3. สร้างทั้ง 2 อย่าง = context แตก 2 ที่ ขัดหลัก single source of truth

### 📋 ขั้นตอนที่ต้องทำที่ laptop (ยังไม่ทำ)
1. เปิดแอป Claude → เมนู **Cowork**
2. สร้าง Cowork project ใหม่ ชื่อ `RMN e-Bidding WorkFlow` (ต้องสร้างเองที่เครื่อง — ไม่ sync มาจาก PC)
3. วาง Project Instructions จาก `WRK_AGENTS\PROJECT_INSTRUCTIONS_DRAFT.md`
4. Connect 3 โฟลเดอร์: `RMN-eBidding-Workflow` / `[EGP]_E-BIDDING - [R.M.N_GROUP]_DATABASE` / `M4RX-B4SE`
   - ⚠️ เช็ค OneDrive sync ให้เป็น ✅ เขียว (ไม่ใช่ ☁️ cloud-only) ก่อน connect

### ⚠️ Known limitation (จำไว้ กันเสียเวลาซ้ำ)
- **Cowork project ไม่ sync ข้ามเครื่อง** — ต้อง set up แยกทุกเครื่องเสมอ อย่าไปรอ sync อีก
- ส่วนขยาย Claude in Chrome **อ่านหน้า claude.ai เองไม่ได้** (script injection timeout ทุกครั้ง) → ต้องให้ user ส่ง screenshot แทน

### ✅ Done (2026-08-09 — PC: Project Instructions + KB registry แก้แล้ว)
- ตรวจไฟล์จริง (ls ทั้ง 2 โฟลเดอร์) พบว่า agent registry เดิม**ผิด 3 จุด**:
  1. OPY KB ไม่ได้อยู่ใน `agents\` — ตัวจริงคือ `E-Bidding\OPERATING.md` (ไฟล์เดียวในระบบที่ไม่มี prefix KB_)
  2. **Doc Expiry เป็น agent เอกเทศ** (KB_DOC_EXPIRY + WRK_DOC_EXPIRY ครบคู่) เดิมตกหล่นจาก registry → รวมเป็น **7 agent** ไม่ใช่ 6
  3. KB folder มี 6 ไฟล์ / WRK folder มี 7 ไฟล์ — ไม่สมมาตรเพราะข้อ 1
- นิยาม nickname ครบชุด: **DA · OPY · DOC · EXP · MM · UI · API** (บันทึกใน KB_ECOSYSTEM_ADMIN.md)
- Rewrite `PROJECT_INSTRUCTIONS_DRAFT.md` เป็น **router 7 agent + Core Rules 15 ข้อ** (เดิมเขียนแบบ single-agent = DA เท่านั้น ซึ่งเป็นบั๊ก: instructions ใช้กับทุกแชทในโปรเจกต์ agent อื่นจะสับสน identity)
- user วาง instructions ใหม่ลงโปรเจกต์ทั้ง PC และ Laptop แล้ว

### ✅ Done (2026-08-09 — Laptop: set up สำเร็จ)
- สร้าง project `RMN-eBidding-Workflow` (ชื่อต่างจาก PC เล็กน้อย ไม่กระทบการทำงาน — ตกลงกันว่า**ไม่ต้องกำกับ (Laptop) ในชื่อ** ให้ระบุเครื่องใน session state แทน = Core Rule 15)
- Connect ครบ 3 โฟลเดอร์: RMN-eBidding-Workflow / M4RX-B4SE / [EGP]_E-BIDDING
- Instructions วางแล้ว

### ✅ Done (Laptop — ปิดครบทุกข้อ)
- **VM service** — แก้แล้ว ใช้งานได้ปกติ
- **Memory restore** — สำเร็จ 16 ไฟล์จาก backup + เพิ่มมือ 2 ตัวที่ backup ไม่มี (da-nickname, checklist-as-widget) → **18 รายการ เท่ากับ PC**
  - ⚠️ laptop ตั้งชื่อไฟล์ด้วย**ขีดกลาง** (`feedback-git-push-format.md`) / PC ใช้ **underscore** (`feedback_git_push_format.md`) — ไม่กระทบการทำงาน ปล่อยไว้ตามนี้
- **Scheduled task** — ยืนยันไม่สร้างที่ laptop ให้ PC เป็นเจ้าของตัวเดียว กันแจ้งเตือนซ้ำ (บันทึกเป็น memory `project_rmn_scheduled_tasks` ทั้ง 2 เครื่องแล้ว)
- **MEMORY_BACKUP_2026-08-09.md อัปเดตแล้ว** → ครบ 18 รายการ (index + full section) restore รอบหน้าจะไม่ขาด

### 🖱️ Mouse Without Borders (นอก scope งาน)
- ย้ายรายละเอียด (IP เครื่อง / คำสั่ง firewall) ไป repo private `RMN-eBidding-KB` → `NETWORK_NOTES.md`
- สรุป: เชื่อม PC ↔ Laptop สำเร็จ · สาเหตุอาการหน่วงคือ network profile เป็น Public → เปลี่ยนเป็น Private แก้ได้

### ⏳ Pending
- (none) — ระบบพร้อมใช้งานครบทั้ง 2 เครื่อง

## 🔄 Session State (2026-08-13 — PC: iOS workflow + security remediation)
> เครื่องที่ใช้: **PC (MARX)** · commit `5d5c026`

### ✅ Done — iOS workflow (scope: OPY บันทึกผลประมูล + DA อ่าน state เท่านั้น)
- ทดสอบจริงจากมือถือ → ยืนยัน **ไม่มี bridge ไป PC** (bridge ผูกกับ session ที่เปิด ไม่ใช่บัญชี) → เปิดแอปเดสก์ท็อปค้างไว้ก็ไม่ช่วย → ปิดข้อสงสัยนี้ถาวร
- มือถือรันใน cloud container → เห็น OneDrive/PC ไม่ได้เลย → **git เป็นช่องทางเดียว**
- แอป GitHub บน iPhone **แก้ไฟล์ + commit ได้** (Edit File · Go to line · Find in File) → **ตัด PAT ออกจากแผนทั้งหมด** (auth ของแอปอยู่ในเครื่อง container ใช้ไม่ได้ แต่ให้ user commit เองแทน)
- ยก KB เข้า repo แบบ minimal 2 ไฟล์: `KB/OPERATING.md` (OPY) + `KB/agents/KB_ECOSYSTEM_ADMIN.md` (DA) — ไม่ยกทั้ง 6 ไฟล์ เพื่อลด drift
- สร้าง `BOOTSTRAP_IOS.md` = คำสั่งเปิด session มือถือ + ข้อห้าม
- track `WRK_ECOSYSTEM_ADMIN.md` เข้า git ครั้งแรก (เดิม untracked = ไม่มี backup เลย)
- `.gitignore` 1 → 9 บรรทัด (กัน xlsx/docx/pdf/skill/pycache/backup)

### 🔴 บั๊กใหญ่ที่เจอ+แก้: repo มี 2 branch ข้อมูลไม่ตรงกัน
- default branch บน GitHub เป็น **master** (ค้างที่ seq 103 / 105 บรรทัด) ขณะ **main** มี 553 records
- ถ้า commit จากแอปมือถือตอนนั้น = ลงผิด branch ข้อมูลหาย 454 บรรทัด
- แก้: เปลี่ยน default → `main` · ลบ `master` + `claude/pull-latest-changes-XmNZQ` · `git fetch --prune` · `git remote set-head origin -a`
- อธิบายเรื่องค้างเก่าได้ด้วย: iOS เคยรายงาน HEAD `7deb2ca` ≠ PC `8f12d04` เพราะ ls-remote ชี้ไป master

### 🔒 Security remediation (สำคัญที่สุดของ session นี้)
- ตรวจพบ repo **public** มีข้อมูลส่วนบุคคลอยู่แล้ว (ไม่ใช่กำลังจะรั่ว — รั่วไปแล้ว)
- แยก repo ใหม่ **`RMN-eBidding-KB` (private)** → ย้าย `WRK_DOC_EXPIRY.md` (เลขบัตร ปชช. + เบอร์ส่วนตัว), `MEMORY_BACKUP_2026-08-09.md`, `NETWORK_NOTES.md` (IP บ้าน + คำสั่ง firewall)
- redact ใน `WRK_ECOSYSTEM_ADMIN.md`: เลขบัตร ปชช. → `[REDACTED]` · บล็อก MWB/IP → ย้ายไป private
- **ไม่แก้** `WRK_FEE_PAYMENT.md` — ชื่อ/เบอร์ในนั้นเป็น template ใบแจ้งชำระที่ส่งหน่วยงานราชการอยู่แล้ว = contact สาธารณะ
- สแกนแล้ว **ไม่พบ** API key / token / password ใดๆ
- ⚠️ **ยังไม่ทำ**: ล้าง git history (91 commits เก่ายังค้นเจอเลขบัตรได้) — เลือก D1 "หยุดเลือดก่อน" ไว้ก่อน

### 📋 Core Rules ใหม่ (ยังไม่ได้เขียนลง CLAUDE.md — pending)
| # | กฎ |
|---|---|
| 16 | PC ต้อง `git pull` ก่อนเริ่มงานทุกครั้ง (กัน split-brain กับมือถือ) |
| 17 | มือถือ = OPY + DA(read-only) เท่านั้น · DOC/MM/UI/EXP/API = PC |
| 18 | เช็ค branch = `main` ก่อน commit จากแอป GitHub ทุกครั้ง |
| 19 | ข้อมูลส่วนบุคคล (เลขบัตร/เบอร์ส่วนตัว/IP) → repo private เท่านั้น |
| 20 | แก้ KB ที่ต้นฉบับ M4RX-B4SE เสมอ → copy ทับ `KB/` ก่อน push |

### ⏳ Pending
- ~~เขียน Core Rule 16-20 ลง `WRK_AGENTS/CLAUDE.md`~~ ✅ เสร็จ (section `## 🔀 Multi-Device Rules`)
- ~~ทดสอบจริงบนมือถือ~~ ✅ **ผ่าน 100%** (2026-08-13) — clone `main` สำเร็จ · อ่าน 4 ไฟล์ครบ · รายงานตรงเฉลยทุกข้อ (553 records · FY2569 max seq 177 · missing fy 0 · Core Rule 16-20)
  - มือถือยังตรวจเจอบั๊กเพิ่มเอง: `KB/OPERATING.md` มีตาราง seq 94-102 hardcode ค้าง → DA ลบแล้ว (`921413f`)
  - ยังไม่ได้ทดสอบขั้น commit จริงผ่านแอป GitHub (รอมีผลประมูลจริงค่อยทำ)
- ~~ตัดสินใจเรื่อง git history~~ ✅ **ปิดเคส — เลือก D1 (ปล่อย history ไว้)**
  - เหตุผล user: ต่อให้ป้องกันดีแค่ไหน ข้อมูลจากหน่วยงานรัฐก็รั่วอยู่แล้วทั้งประเทศ — ต้นทุน D2/D3 (เว็บดับ / เสีย 91 commits) ไม่คุ้มกับความเสี่ยงส่วนเพิ่มที่ลดได้
  - สิ่งที่ได้ผลจริงคือหยุดรั่วเพิ่ม: Core Rule 19 + repo private แล้ว → commit เก่าเป็น snapshot ตายตัว ไม่โตขึ้น
  - ⚠️ ถ้าอนาคตมีเหตุให้ต้องล้างจริง (เช่น audit/ลูกค้าร้องขอ) ให้กลับมาทำ D2 `git filter-repo` — บันทึกไว้เป็นทางเลือกสำรอง

### ✅ Done (2026-08-13 — data fix: fiscalYear)
- **backfill 143 records** ที่ไม่มี `fiscalYear` → 2569 (commit `e9dd329`)
  - ต้นตอ: template ที่ OPY ใช้บันทึกรายวัน**ไม่มี field นี้** → OPY แก้ schema แล้ว (`6d1d909`)
- **แก้ 26 records** ที่ `fiscalYear` ผิด — ยึด **วันประกาศ (field `date`)** ตามที่ user สั่ง
  - กฎ: เดือน ≥ ต.ค. → ปีงบ +1 (ปีงบไทยเริ่ม 1 ต.ค.)
  - 2565 92→71 · 2566 92→110 · 2567 135→138 · 2568 57 · 2569 177
  - verify: mismatch เหลือ 0 · 553 records · JSON valid
- 📌 **กฎที่ยึดต่อไป: FY คำนวณจาก `date` ไม่ใช่จากเลข id** (id เข้ารหัสเดือนที่ขึ้นระบบ e-GP ซึ่งอาจต่างจากวันประกาศจริง)
- DA อ่าน state บนมือถือ = อ่านจาก public repo ได้แล้ว (redact เรียบร้อย) — ยังไม่ทดสอบ

## 🔄 Session State (2026-08-13 #2 — PC: repo hygiene + iOS entry point)
> เครื่อง: **PC (MARX)** · resume จาก session #1 วันเดียวกัน

### ✅ Done
- commit WRK ที่ค้างจาก session ก่อน (`aa8e560`) — mark iOS mobile test ผ่าน 100% + note บั๊ก `KB/OPERATING.md` hardcode seq 94-102
- `.gitignore` +2 บรรทัด: `SKILL_*.md`, `PROJECT_INSTRUCTIONS_DRAFT.md` (`0cab528`) → working tree clean
- **ยืนยัน entry point มือถือ: Cowork tab เท่านั้น** (`c67c339` → `BOOTSTRAP_IOS.md` section `## 📍 เปิดที่ไหน`)
  - Project chat ธรรมดา **ไม่มี shell** → clone ไม่ได้ → ทำงาน OPY/DA ไม่ได้เลย
  - Cowork `+ New task` **ผูก project ไม่ได้** (Add context มีแค่ Camera/Photos/Add files/Connectors) → prompt ต้อง **self-contained** ทุกครั้ง
  - โปรเจกต์ `RMN-eBidding-Workflow` ที่สร้างบนมือถือ = ไม่ใช้ ลบทิ้งได้
  - session ที่รันบน PC **มองเห็นได้จาก Cowork tab บนมือถือ** (แต่ยังไม่มี bridge ไป PC ตามเดิม)
- ร่าง prompt เปิด session มือถือ 2 ก้อน (OPY / DA) — แนะนำเก็บใน Notes บน iPhone
- checklist iPhone workflow: interactive widget + `iPhone_Workflow_Checklist_RMN.docx` (Core Rule 10) — docx อยู่ใน repo folder แต่ถูก gitignore
- memory ใหม่: `project_ios_cowork_entry_point.md` + index

### ⚠️ ข้อจำกัดที่เจอใน session นี้
- **device_bash (VM ในเครื่อง user) ไม่มี network** → `git pull/push` ทำเองไม่ได้ (HTTP 403 from proxy) → **user ต้องรันใน PowerShell เสมอ**
- device_bash ลบ `HEAD.lock` / `index.lock` ไม่ได้ (Operation not permitted) → user ต้อง `del` เอง

### ⏳ Pending
- **push 3 commits: `aa8e560` · `0cab528` · `c67c339`** (ต้อง pull ก่อน — Core Rule 16)
- ยังไม่ทดสอบ commit จริงผ่านแอป GitHub บนมือถือ (รอมีผลประมูลจริง)
- ยังไม่ทดสอบ iOS Text Replacement ว่ารองรับ prompt หลายบรรทัดยาวๆ ไหม
