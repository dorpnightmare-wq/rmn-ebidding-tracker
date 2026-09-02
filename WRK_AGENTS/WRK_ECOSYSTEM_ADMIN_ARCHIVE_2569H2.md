# 📦 ARCHIVE — WRK_ECOSYSTEM_ADMIN (DA) · 2569 H2

> session log เก่าที่ย้ายออกจาก `WRK_ECOSYSTEM_ADMIN.md` เมื่อ 2026-08-24 ตามกฎเพดาน 20 KB
> ครอบคลุม 2026-07-01 → 2026-08-24 #2 (11 sessions)
> ⚠️ ไฟล์นี้ **ไม่ต้องอ่านตอนเปิด session** — เปิดเฉพาะตอนต้องสืบย้อนว่าเคยตัดสินใจอะไรไว้
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

### 🔁 ต่อท้าย session #2 — เปลี่ยนโมเดล multi-device (สำคัญที่สุดของวัน)
- **iPhone = remote control ของ PC** — เปิด **session เดิม** ใน Cowork tab แล้วพิมพ์สั่ง งาน execute บน MARX จริง (ทดสอบจาก iPhone → `HOST=MARX`) → ใช้ได้ **ครบทุก agent**
- **task ใหม่ที่สร้างจากมือถือ = ไม่มี bridge** — bridge ติดตอน "แนบ folder เข้า Cowork task" และมือถือ Add context ไม่มีตัวเลือก folder → **restart ต้องทำจาก PC เท่านั้น** (Core Rule 21)
- **git ต้องรันผ่าน `Windows-MCP → PowerShell`** (Windows host จริง มี network + ลบ `.lock` ได้) · ⛔ ห้ามใช้ `device_bash` รัน git (Linux VM ไม่มี network + ลบ lock ไม่ได้) — Core Rule 18 rev.2
- workflow เก่า (clone + commit ผ่านแอป GitHub) → **ON HOLD** ที่ `BOOTSTRAP_IOS.md` · Core Rule 17-18 เดิมถูกแทนแล้ว
- **Core Rule 22**: หนึ่งงาน = หนึ่ง agent session · DA ทำได้แค่ route / read-only check / แก้ข้อมูลเก่าข้าม agent / git ให้ทุก agent
- **Core Rule 21 rev**: user รับได้ว่า context เต็มนอกบ้าน → **ไม่ต้องเช็ค/เตือนล่วงหน้า** ชดเชยด้วยการเขียน WRK state **ระหว่างทาง** ทุกก้อนงาน
- bridge หลุดชั่วคราวได้เมื่อเน็ตตก → **กลับมาเอง** ไม่ต้อง restart แค่ลองใหม่
- commits: `bbbac0e` (rev.2) · `485f652` (Rule 21-22) · `4f4091a` (Rule 21 rev)

### ⏳ Pending (ท้าย session)
- ยังไม่ทดสอบ: PC หลับ/ปิดจอ แล้ว bridge ยังอยู่ไหม
- ยังไม่ทดสอบ: resume session ที่ context เต็มแล้ว ยังอ่านย้อนได้ไหม

## 🔄 Session State (2026-08-24 — DA: ขึ้นทะเบียนผู้ประกอบการ ชั้น 3)

### 📌 บริบทงาน
- คำขอ **หลักเกณฑ์ทั่วไป** เลขที่ `013690700012` ยื่นแล้ว 24/08/2569 10:37 · ครบ 3 หัวข้อ · **ส่งคืนแก้ไข 1 ครั้ง**
- คำขอ **หลักเกณฑ์เฉพาะอื่นๆ** ยังเป็น "บันทึกแบบ" ว่างทั้ง 5 หัวข้อ (1-3 ซ้ำ + 4 บุคลากร + 5 เครื่องจักร)
- สาขา: งานก่อสร้างทาง ชั้น 3 · เดิมถือทะเบียน **ชั้น 4** อยู่แล้ว (แนบเป็นเอกสารข้อ 4)

### ✅ Done
- **สร้าง KB ใหม่** `M4RX-B4SE\RMN_Enterprise\Company-Assets\` — เดิมไม่มีข้อมูลบริษัทใน backbone เลย
  - `EQUIPMENT.md` — ทะเบียนเครื่องจักร 21 คันครบทุกฟิลด์ที่ฟอร์ม e-GP ต้องการ (ทะเบียน/จังหวัด/คัสซี/เลขเครื่อง/ยี่ห้อ/รุ่น/ขนาด/วันจดทะเบียน/วันครอบครอง/วิธีได้มา/ผู้ถือกรรมสิทธิ์)
  - `เครื่องจักร_ขึ้นชั้น3_RMN.docx` + interactive widget (Core Rule 10)
- อ่านใบคู่มือจดทะเบียนต้นฉบับครบ **21/21 คัน** (OCR tesseract ไม่แม่นพอ → ใช้อ่านภาพโดยตรง)
- ถอดสาเหตุที่ถูกส่งคืนแก้ไข: **แนบผลงานร่วมค้าใต้ข้อ 1 แทนข้อ 2** (เทียบ TRARSummary รอบ1↔รอบ2)

### 🔴 ประเด็นค้าง (ต้องให้ user ตัดสิน)
1. **ถข 6540 / ถข 6541** (Self-Propelled Vibratory Roller 2 คัน) — กรรมสิทธิ์ = บ.กรุงไทย มิซูโฮ ลีสซิ่ง · **ผู้ครอบครองตามทะเบียน = บ.ลีดเวย์ เฮฟวี่ แมชชีนเนอรี่** ไม่ใช่ RMN → e-GP ดึงจากกรมขนส่งจะไม่ตรง ต้องมีสัญญาเช่า RMN↔ลีดเวย์ · **ความเสี่ยงสูงสุดของคำขอ**
2. ผลงาน **สทช.15 นภ.5025 (34.4 ล้าน)** ที่ใช้ผ่านเกณฑ์ "หนึ่งสัญญา ≥ 30 ล." **ไม่มีใน** `ฝากไฟล์\ผลงาน` (มีแค่ 3 จาก 4) — ต้นฉบับอยู่ `ขึ้นชั้น 3\ผลงานชั้น3\`
3. ไฟล์ `12.2 กระบะบรรทุก 82-5996 มค.pdf` — ทะเบียนจริงคือ **82-5886**
4. รถบรรทุกน้ำ 4 คัน — ทะเบียนไม่ระบุความจุลิตร (ระบุแต่ น.น.บรรทุก) หากถูกขอหลักฐาน 6,000 ล. ต้องใช้ใบเสร็จ/สเปคถัง
5. ใบอนุญาตขนส่ง **ค.ข. 272/2562** ในเล่ม Dump Truck ระบุสิ้นอายุ 2 พ.ค. 2567 — ต้องเช็คว่าต่อแล้วหรือยัง

### ⏳ ยังไม่ทำ
- ข้อ 4 บุคลากร (7 คน: สามัญวิศวกร มานพ · ภาคี นฤสรณ์+จักรทิพย์ · ช่าง พัฒนพงษ์/พิมลพรรณ/ณัฎฐพล/ธีรภัทร) → ยังไม่ได้อ่าน PDF ใบ กว.
- แผนเดิม `ขึ้นชั้น 4\รถขึ้นชั้น 3 งานก่อสร้างทาง.pdf` ล้าสมัย 5 จุด — ยังไม่ได้ปรับให้ตรงของจริง
- scheduled task DOC EXPIRY CHECKER: แก้ path เป็น `RMN-eBidding-KB\WRK_DOC_EXPIRY.md` แล้วแต่ save ไม่ผ่าน + ต้องเพิ่มโฟลเดอร์ `RMN-eBidding-KB` เข้าโปรเจกต์


### ✅ User ยืนยันปิดประเด็น (ท้าย session 2026-08-24)
- ผลงาน สทช.15 นภ.5025 (34.4 ล.) → ใช้ต่อ · สมบูรณ์แล้วไม่ต้องแก้รอบ 2
- สัญญาเช่า ถข 6540/6541 → **อยู่หน้าที่ 2 ในไฟล์ PDF ของรถเอง** ไม่ต้องหาเพิ่ม (ลดความเสี่ยงข้อ 1 ลง)
- ยึดไฟล์สแกนใหม่ใน `ฝากไฟล์\เอกสารขึ้นชั้น3` เป็นหลัก · `ขึ้นชั้น 4\รถขึ้นชั้น 3 งานก่อสร้างทาง.pdf` = ล้าสมัย
- **งานถัดไป: ข้อ 4 บุคลากร 7 คน** (อ่าน PDF ใบ กว. ใน `ฝากไฟล์\เอกสารขึ้นชั้น3\บุคคล`)

## 🔄 Session State (2026-08-24 #2 — DA: ข้อ 4 บุคลากร + จัดโครงสร้างเอกสาร)
> เครื่อง: **PC (MARX)** · resume จาก session #1 วันเดียวกัน

### ✅ Done — ข้อ 4 บุคลากร (อ่านต้นฉบับครบ 11 ไฟล์)
- สร้าง `RMN-eBidding-KB\PERSONNEL.md` (private, PII) — 7 คน ครบทุกฟิลด์ที่ e-GP ขอ (`082f8db`)
- cross-check **ภงด.1 มี.ค.–มิ.ย. 2569** — เลขบัตร ปชช. ตรง 7/7 คน (`a19151f`)
  - ปิดเคสสะกดชื่อ: ภงด.1 ทุกเดือน = **มานพ วิยาสิงห์** ตรงใบ กว. → สัญญาจ้างที่พิมพ์ "วิทยาสิงห์" คือฝั่งผิด
  - ธีรภัทร เข้าบัญชีค่าจ้างครั้งแรก **เม.ย. 2569** · นฤสรณ์ **มิ.ย. 2569** → ใช้เป็นวันเริ่มจ้างโดยประมาณ
  - ณัฏฐพล ภักดี ได้ 18,000/ด. = เรตวิศวกร (ช่างได้ 10,000) + ถือใบ กว. **ภย.48245 ภาคีวิศวกร** → ควรย้ายจากกลุ่มช่างขึ้นข้อ 2
- 🔴 ยังขาด: ทก.6-1/6-3 + สัญญาจ้าง 3 คน (นฤสรณ์ · ณัฏฐพล · ธีรภัทร) · ช่างขาด 1 คนถ้าย้ายณัฏฐพล

### ✅ Done — จัดโครงสร้าง `ฝากไฟล์\เอกสารขึ้นชั้น3` ใหม่ทั้งหมด (51 ไฟล์)
- โครงสร้างใหม่ตรงหัวข้อฟอร์ม: `00_นิติบุคคล` / `01_ผลงาน` / `04_บุคลากร{4-1..4-9}` / `05_เครื่องจักร{5-1..5-8}`
- ชื่อไฟล์ = `<เลขหัวข้อ>_<ตัวระบุ>_<ประเภทเอกสาร>.pdf` · ไฟล์ที่เอกสารไม่ครบต่อท้าย `_ขาดทก6-1/6-3`
- แก้ชื่อไฟล์ผิด `82-5996` → `82-5886`
- มี `_RENAME_MAP.csv` + `_UNDO.ps1` ย้อนกลับได้ 100%
- ⚠️ PowerShell 5.1 ต้องเขียนสคริปต์เป็น **UTF-8 with BOM** ไม่งั้นภาษาไทยเพี้ยน parse error

### ✅ Done — `RMN-eBidding-KB\COMPANY.md` (ใหม่)
- คุณสมบัติทั่วไป + ฐานการเงิน + ผลงาน จากหน้าจอคำขอ 013690700012 (`139878d`)
- รายละเอียดผลงาน 4 ฉบับจากหนังสือรับรองต้นฉบับ (`0bb94c0`)

### 🔑 ข้อมูลผลงานที่แก้ความเข้าใจเดิม (สำคัญ)
- "สทช.15 นภ.5025 = 34.4 ล." **ผิด** → นภ.5025 = **ร่วมค้า 25.99 ล.** (RMN 49% = 12.73 ล.)
- ตัวที่ผ่านเกณฑ์หนึ่งสัญญา ≥30 ล. คือ **นภ.5042 ผลงานเดี่ยว 34,444,000** (`ขทช.นภ./004/2568`)
  - ต้นเหตุ: ไฟล์ชื่อ `รับรองผลงาน สทช.15 - สายนภ.5025` แต่เนื้อในเป็น นภ.5042
- ✅ **user ยืนยัน 2026-08-24: 34 ล. ได้แน่ ไม่ต้องกังวลเรื่องผลงานอีก** · ผลงานใช้ได้ทั้ง 4 ตัวใน `ผลงานชั้น3\`
- ⚠️ รายการ 1 กรอกวันแล้วเสร็จ 13/07/2568 · หนังสือรับรองเขียน 27/06/2568 (ยังไม่แก้)

### ✅ ปิดเคส — ใบอนุญาตประกอบการขนส่ง
- `ค.ข. 272/2562` (สิ้นอายุ 2 พ.ค. 2567) ที่พิมพ์ในเล่ม Dump Truck 6 คัน = **ข้อมูล ณ วันจดทะเบียนรถ ปี 2566** เล่มไม่อัปเดตเมื่อต่ออายุ
- ใบปัจจุบัน = **มค.บ. 417/2567 สิ้นอายุ 30 ก.ค. 2572** (ยืนยันจากเล่ม 82-7166 จดทะเบียน 6 พ.ค. 2569)
- บันทึกหมายเหตุลง `EQUIPMENT.md` แล้ว

### 🔴 ความเสี่ยงอายุเอกสารที่ยังเปิดอยู่
1. **หนังสือรับรองวงเงินสินเชื่อ ธพว.2499/2569** ออก 26/05/2569 อายุ 90 วัน → ครบ ~24/08/2569 (วันที่ยื่นพอดี) · ถ้าโดนส่งคืนแก้ไขต้องขอใหม่
2. **หนังสือรับรองห้างที่แนบ** = ฉบับ 28/05/2569 (ใกล้หมด) ทั้งที่มีฉบับ 10/07/2569 หมด 08/10/2569 อยู่แล้ว → **ควรสลับไฟล์**
3. **ภาษีรถ 20/21 คันยังไม่ตรวจ** (ตรวจแล้วเฉพาะ ตฆ 8672: ชำระ 18/06/2569 ครบ 31/01/2570)
4. **สัญญาเช่า ถข 6540/6541** ยังไม่ได้อ่านวันสิ้นสุด

### 🛠️ บทเรียนเครื่องมือ (รอบนี้)
- **device_bash ใช้ได้ดีมากกับ PDF ก้อนใหญ่** — มี pdftoppm/pdftotext/qpdf/python3 ครบ · render หน้าที่ต้องการลงโฟลเดอร์ที่ connect แล้วค่อย stage เฉพาะ .jpg = เร็วกว่า stage PDF 68MB มาก
- เขียนไฟล์ลง `ฝากไฟล์` (ไม่ได้ connect) ต้องผ่าน PowerShell เท่านั้น — ยืนยันซ้ำอีกครั้ง
- Windows-MCP ส่งคีย์ไป TUI (Claude Code /usage) **คีย์ตกหาย ~2 ใน 3** เพราะโฟกัสสลับ — อย่าใช้วิธีนี้กับ TUI อีก
- **PYTHONHOME ที่ตั้งค้างในเครื่อง ทำ python พังทั้งระบบ** (sqlite3 DLL) — ลบออกแล้ว 2026-08-24

### ⏳ Pending
- ทำ ทก.6-1/6-3 + สัญญาจ้าง 3 คน · หาช่างคนที่ 4
- กรอกเครื่องจักรข้อ 1-8 ใน e-GP (user กรอกเอง · DA แสดงข้อมูลเป็น widget ทีละข้อ)
- ยังขาด 3 ฟิลด์/คัน: วันเสียภาษี (20 คัน) · เลขที่สัญญาเช่าซื้อ · ลำดับใน งด.50
- scheduled task DOC EXPIRY CHECKER ยัง save ไม่ผ่าน

### 🔁 ต่อท้าย session 2026-08-24 #2 (ก่อน restart 18:xx)

**เพิ่มจากที่บันทึกไว้ตอน `647ca0c`:**
- ✅ **ภาษีรถครบ 21/21 คัน** → บันทึกใน `EQUIPMENT.md` (ตาราง "ภาษีรถประจำปี")
  - 🔴 1ตข 7104 ครบ 4 ก.ย. 69 (เร็วสุด) · 🟠 รถบรรทุก 10 ล้อ 6 คันครบพร้อมกัน 30 ก.ย. 69 · ถข 138 31 ต.ค. 69 · 82-7155 31 ธ.ค. 69
  - ตฆ 4069 (14/05/69→23/01/70) และ ถข 121 (30/04/69→08/06/70) = user เปิดเล่มให้เอง
- ✅ **ผลงาน 4 ฉบับ อ่านครบ + ได้เลข e-GP ทั้ง 8 เลข** → `COMPANY.md` (`0bb94c0` + `1995159`)
  - โครงการ 11 หลัก / คุมสัญญา 12 หลัก: นภ.5042 `67109200008`/`680122011247` · กส.3007 `67119112184`/`680122005829` · ทล.2346 `68109269796`/`681222003899` · นภ.5025 `67059265416`/`670622041290`
  - ⚠️ ร่วมค้า 2 รายการ: ระบบจะดึงวงเงินเต็มสัญญามา ต้องแก้ช่องวงเงินที่ยื่นเป็นส่วน RMN เอง
- ✅ **จัดโฟลเดอร์ `01_ผลงาน` ใหม่** — user ดึงไฟล์ที่ 4 เข้ามาแล้ว · เรียง 01-1 = นภ.5042 (34.44 ล. ตัวผ่านเกณฑ์ 30 ล.)
- ✅ **สร้างใบสั่งงานต่อภาษี** — PNG + txt ที่ `Downloads\` (แบ่ง 4 ลำดับความเร่งด่วน ส่ง LINE ให้พนักงานได้)
- ✅ **ทะเบียนเอกสารใกล้หมดอายุ (ทุกหมวด)** — 3 แดง / 9 ส้ม
  - 🔴 DBD ฉบับที่แนบ (28/05/69) หมด 26 ส.ค. → **สลับเป็นฉบับ E10091220726785 (10/07/69) ที่มีอยู่แล้ว**
  - 🔴 วงเงินสินเชื่อ ธพว.2499/2569 ครบ 24 ส.ค. 69 (วันที่ยื่นพอดี)
  - ⚠️ ยังไม่รู้: พ.ร.บ. 21 คัน · วันสิ้นสุดสัญญาเช่า ถข6540/6541 · อายุทะเบียนชั้น 4 เดิม · ลำดับ งด.50

**บทเรียนเครื่องมือเพิ่ม:**
- `device_bash` **ล่มกลาง session** ("Workspace unavailable") → fallback = copy ไฟล์ไป `Downloads` ด้วย PowerShell แล้ว stage มา render ที่ container
- render PDF สแกน: `pdftoppm -r 100~150 -jpeg` + crop ครึ่งบน + montage 2 หน้า = ประหยัดโควตา ~4 เท่าเทียบกับอ่านเต็มหน้า
- ทำภาพส่ง LINE: เขียน HTML → `chromium --headless --screenshot --force-device-scale-factor=2` ใน container ได้ภาพคมกว่าให้ user แคปหน้าจอ widget

**⏳ Pending (เรียงตามความคุ้ม):**
1. ~~widget เครื่องจักรข้อ 2-8~~ ✅ ปิดแล้ว session #3
2. ร่าง ทก.6-1/6-3 + สัญญาจ้าง 3 คน (นฤสรณ์ · ณัฏฐพล · ธีรภัทร) + หาช่างคนที่ 4
3. ~~สลับไฟล์ DBD ในคำขอ~~ ✅ ปิดแล้ว session #3
4. [กินโควตา] อ่านสัญญาเช่า ถข6540/6541 · หาลำดับ งด.50 ในงบ 2568 · เลขสัญญาเช่าซื้อ 17 คัน (ต้องมีไฟล์สัญญาก่อน)
5. [แนวคิด ยังไม่เริ่ม] sector database ใน webapp — ติดเรื่อง PII: repo public ห้ามมีเลขบัตร ปชช. ต้องเลือกก่อนว่าจะตัด/mask/ไม่ทำ

## 🔄 Session State (2026-08-24 #3 — DA: widget เครื่องจักร 2-8 + ปิดเคส DBD)
> เครื่อง: **PC (MARX)** · resume จาก session #2 · เริ่มที่ WRK `9b4a029` / KB `1995159` (sync ทั้งคู่)

### ✅ Done
- **widget เครื่องจักรข้อ 2-8** — 20 คัน ครบ 14 ช่องตามฟอร์ม e-GP · คลิกค่า = copy ช่องเดียว · ปุ่ม = copy ทั้งคัน · tab ข้อ 6 สีส้มเตือน + กล่องแดงเรื่องลีดเวย์ · แนบวันครบภาษีต่อคันในการ์ด
- 🔴→✅ **สลับไฟล์ DBD ในคำขอแล้ว** (user ยืนยัน `3.done` 2026-08-24) → ฉบับ 28/05/2569 ที่หมด 26 ส.ค. **ไม่ใช่ความเสี่ยงอีกต่อไป** · ตัวที่แนบตอนนี้ = `E10091220726785` (10/07/2569 หมด 08/10/2569)

### 🛠️ บทเรียนเครื่องมือ (รอบนี้)
- ❌ `device_bash` **ยังล่มต่อจาก session #2** — "Workspace unavailable. The isolated Linux environment on this device failed to start." → ใช้ `device_stage_files` + Windows-MCP PowerShell แทนตลอด session
- ⚠️ **PowerShell อ่านไฟล์ .md ภาษาไทยออกมาเป็น mojibake** (`Get-Content` ผ่าน MCP response) → อ่าน MD ต้องใช้ `device_stage_files` เท่านั้น · PowerShell เหมาะกับ git/สั่งงานไฟล์ ไม่เหมาะอ่านเนื้อไทย
- ✅ `device_request_folder_access` ขอ `RMN-eBidding-Workflow` เพิ่มได้ทันที (user อนุมัติในเครื่อง) → หลังจากนั้น stage/commit ได้ตรง ไม่ต้องผ่าน Downloads

### ✅ Done — ทก.6-1/6-3 มอบให้ฝ่ายออฟฟิศทำ (user ตัดสิน 2026-08-24)
- 📌 **นิยาม "ออฟฟิศ" ในบริบท RMN = พนักงานบัญชี · เสมียน · เลขา** (ไม่ใช่ทีม agent/ไม่ใช่ DA)
- DA ไม่ร่างตัวเอกสารเอง → ออก **ใบสั่งงาน** ให้ออฟฟิศแทน: `ขึ้นชั้น 3\ใบสั่งงาน_เอกสารบุคลากร_ชั้น3.docx` + interactive checklist widget (Core Rule 10)
- 4 รายการในใบสั่งงาน: ทก.6-1 นฤสรณ์ (1 มิ.ย. 69) · ทก.6-1 ณัฏฐพล (**วันเริ่มจ้างต้องยืนยัน** — อยู่ใน ภงด.1 ตั้งแต่ มี.ค. 69) · ทก.6-3 ธีรภัทร (1 เม.ย. 69) · แก้ ทก.6-3 พิมลพรรณ ให้ตรงสัญญา 1 ต.ค. 67
- ⚠️ ใบสั่งงานมีเลขบัตร ปชช. → **local เท่านั้น ห้ามเข้า repo public** (Core Rule 19) · ระบุคำเตือนไว้บนหัวเอกสารแล้ว

### ✅ Done — ปิดความเสี่ยงวงเงินสินเชื่อ
- user **สั่งหนังสือรับรองวงเงินสินเชื่อฉบับใหม่จาก ธพว. แล้ว 2026-08-24** → ฉบับเดิม `ธพว.2499/2569` (ครบ 90 วันวันนี้) ไม่ใช่ความเสี่ยงค้างอีก · รอไฟล์ฉบับใหม่มาแทน

### ⏳ Pending (update ท้าย session #3)
1. **หาช่างคนที่ 4** — เกณฑ์ต้องมี 4 · ปัจจุบัน พัฒนพงษ์/พิมลพรรณ/ธีรภัทร = 3 (ณัฏฐพลย้ายเป็นวิศวกร) → ออฟฟิศเสนอชื่อ วุฒิ ปวช.+ สายช่าง ที่อยู่ใน ภงด.1 แล้ว
2. รอออฟฟิศส่ง ทก.6-1/6-3 + สัญญาจ้าง 4 รายการกลับ → แล้วค่อยกรอก e-GP ข้อ 4
3. ยืนยันวันเริ่มจ้าง **ณัฏฐพล** จากทะเบียนลูกจ้าง/บัญชีเงินเดือน
4. รอหนังสือรับรองวงเงินสินเชื่อฉบับใหม่จาก ธพว. → เปลี่ยนไฟล์แนบในคำขอ
5. [กินโควตา] อ่านสัญญาเช่า ถข6540/6541 (หน้า 2 ในไฟล์รถ) · ลำดับ งด.50 ในงบ 2568 · เลขสัญญาเช่าซื้อ 17 คัน
6. scheduled task DOC EXPIRY CHECKER ยัง save ไม่ผ่าน
7. รายการ 1 (นภ.5042) วันแล้วเสร็จในคำขอ 13/07/2568 vs หนังสือรับรอง 27/06/2568 — ยังไม่แก้
8. [แนวคิด] sector database ใน webapp — ติด PII

### 🔴 ความเสี่ยงอายุเอกสารที่เหลือ (หลังปิด DBD + วงเงินสินเชื่อ)
1. **1ตข 7104** ภาษีครบ 04/09/2569 (เร็วสุด) · รถบรรทุก 10 ล้อ 6 คัน 30/09/2569 · ถข 138 31/10/2569
2. ยังไม่รู้: พ.ร.บ. 21 คัน · วันสิ้นสุดสัญญาเช่า ถข6540/6541 · อายุทะเบียนชั้น 4 เดิม

### 🔧 ต่อท้าย session #3 — ตามที่ DB ตรวจเจอ (2026-08-24)
- DB ตรวจไฟล์จริงแล้วชี้ว่า **ต้นเหตุ context บวมคือ WRK file ไม่มีเพดาน** ไม่ใช่ scope ของ DA กว้าง
  - `WRK_ECOSYSTEM_ADMIN.md` 59,501 B · `WRK_OPERATING.md` 59,707 B → DA/OPY กิน ~58 KB ก่อนเริ่มงานจริงทุกครั้ง
- ✅ **DA แก้แล้ว**: ตัด session log เก่า (2026-07-01 → 2026-08-24 #2 · 11 sessions) ออกไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md`
  - `59,501 B → 6,546 B` (−89%) · ไฟล์ live เหลือแค่ state ปัจจุบัน + pending ตามกฎ
- ✅ แก้ 3 จุดที่ DB ตรวจเจอผิดใน `KB_ECOSYSTEM_ADMIN.md` — verified line (WRK 7→6 ไฟล์) · API Status mark disabled · nickname line ตัด API
- 🔴 **ยังไม่แก้ — ไม่ใช่ scope DA (Core Rule 22):** `WRK_OPERATING.md` 59,707 B ต้องให้ **OPY** archive ในเซสชันของตัวเอง
  - วิธีเดียวกัน: เก็บ state ปัจจุบัน + pending · ที่เหลือ → `WRK_OPERATING_ARCHIVE_2569H2.md`

### ✅ ปิดวง — เพดาน 20 KB ทำครบทุกไฟล์แล้ว (2026-08-24 ท้าย session)
| ไฟล์ที่ agent อ่านทุก session | ก่อน | หลัง | สถานะ |
|---|---|---|---|
| WRK_ECOSYSTEM_ADMIN.md (DA) | 59,501 | **7,921** | ✅ archive → `_ARCHIVE_2569H2` 53,827 |
| WRK_OPERATING.md (OPY) | 59,707 | **14,923** | ✅ OPY ทำเอง → `_ARCHIVE_2569H2` 60,350 · commit `8659e25` |
| WRK_FEE_PAYMENT.md | 16,066 | 16,066 | ✅ ใต้เพดาน |
| WRK_MAPMAKER.md | 12,555 | 12,555 | ✅ ใต้เพดาน |
| WRK_UIUX.md | 4,891 | 4,891 | ✅ ใต้เพดาน |
| WRK_API_STATUS.md | 1,235 | 1,235 | 🚫 agent disabled |

**🔴 ไฟล์ที่ยังเกินเพดาน และทุก agent อ่านทุก session:**
- `WRK_AGENTS\CLAUDE.md` = **21,353 B** — ไม่ใช่ session log ตัดเข้า archive ไม่ได้ตรงๆ ต้องรีไรต์/แยกส่วน
  → **เรื่องออกแบบ ส่งไป DB** ไม่ใช่งานที่ DA แก้เองได้ (กระทบทุก agent)
- `seed_bids.js` = **473,873 B** — เป็นข้อมูล ไม่ใช่ log · ถ้าจะลดต้องเปลี่ยนวิธีโหลด (แยกตามปี) → **DB**

### 🔁 ผลจาก UI session เดียวกัน (บันทึกไว้กันลืม)
- UI ทำ tab `🏗️ Assets` (read-only) ใน tracker แล้ว — commit `344fbb8` · fetch assets.json แบบ 404-safe · filter `pii:true` ตอน ingestion ✅ ไม่แตะไฟล์ data
- 🐛 **ความผิดของ DA**: บล็อก guide ที่ผมส่งให้ UI เขียนว่า `const ASSETS = []` + fetch assets.json แต่**ไม่ได้ระบุรูปร่างข้อมูล** — ของจริงผม generate เป็น `{meta, assets:[...]}` envelope ไม่ใช่ bare array
  → UI ต้องแก้ handler เอง (`968de1f`) ให้รับทั้งสองแบบ
  → **บทเรียน: guide ที่ส่งข้าม agent ต้องแนบ shape ของข้อมูลจริง ไม่ใช่แค่ชื่อไฟล์+URL**
- ⚠️ tab Assets อยู่ใน tracker (public) ตอนนี้ — ตามแผน 2 BASE มันควรย้ายไป RMN DATABASE · **ยังไม่ต้องรื้อ** รอ DB ตัดสินเรื่อง 2 BASE ให้จบก่อน

## 🔄 Session State (2026-08-25 — DA: verify ชุดข้อมูล e-GP 53 โครงการที่หายจาก tracker)
> ต้นเรื่อง: พบชุดข้อมูลสัญญาภาครัฐใน `Downloads\2569-egp-contract\` (6 ไฟล์ 2.9 GB · โหลดไว้ 13 มิ.ย. 69)
> กรองชื่อห้าง → ชนะ 81 โครงการ ~374 ล. · มีใน tracker 28 · **ขาด 53 โครงการ 297,708,493 บาท**

### ✅ DA ตรวจยืนยันเองแล้ว (ไม่ได้เชื่อรายงาน)
- stage `seed_bids.js` (474,959 B · **558 records** · seq สูงสุด **182**) มาเทียบตรง
- `seed_bids` ใช้ `id` = **รหัสโครงการ 11 หลัก** = axis เดียวกับข้อมูลรัฐ (ยืนยันด้วย `67109200008` ที่รู้ว่ามีอยู่ → เจอ) → เทียบได้จริง ไม่ใช่ false positive
- **53/53 รหัสโครงการ ไม่มีใน seed_bids** · **53/53 เลขที่สัญญา ก็ไม่มี** → ข้ออ้าง "ขาดหาย" **จริง**

### 🔴 แก้ 3 จุดในรายงานต้นทาง
1. **"CSV มีครบทุกฟิลด์ที่ tracker ต้องใช้" — ไม่จริง** ขาด 4 ช่องที่ข้อมูลรัฐไม่มี:
   `budget` · `pct` · `plant` · `workType`
   - ⚠️ `pct` คำนวณจาก **`(1 − bid/budget)×100`** (ตรวจกับ 48 records จริง: ตรง 44) → **ไม่มี budget = ไม่มี pct** · ราคากลางแทนไม่ได้
2. **ทั้ง 53 โครงการสถานะ "ระหว่างดำเนินการ" ทุกตัว** → **ใช้เป็นผลงานขึ้นชั้น 3 ไม่ได้** (ต้องแล้วเสร็จ + มีหนังสือรับรอง)
   - และ **ไม่มีโครงการไหน ≥ 30 ล้าน** → ไม่ช่วยเกณฑ์ "หนึ่งสัญญา ≥ 30 ล." เลย · บัฟเฟอร์ผลงาน 2.95 ล. ยังบางเท่าเดิม
3. **entity ใส่ตรงๆ ไม่ได้** ต้อง map — seed_bids ใช้ชื่อ normalized:

| ชื่อในข้อมูลรัฐ | → seed_bids `entity` | จำนวน |
|---|---|---|
| ห้างหุ้นส่วนจำกัด อาร์เอ็มเอ็น เอ็นเตอร์ไพส์ | `ห้างหุ้นส่วน RMN` | 27 |
| **กิจการร่ามค้า อาร์เอ็มเอ็น** (รัฐพิมพ์ผิด) | `กิจการร่วมค้า RMN` | 9 |
| กิจการร่วมค้า ตักสิลา | `กิจการร่วมค้า ตักสิลา` | 14 |
| กิจการร่วมค้า รักดี | `กิจการร่วมค้า รักดี` | 3 |

### ⚠️ ผลกระทบที่ต้องตรวจ — การ์ด SME 300M
297.7 ล. ของงาน **ที่อยู่ในมือ (ระหว่างดำเนินการ)** ไม่อยู่ใน tracker · การ์ด SME ใน Dashboard วัดวงเงินสะสมเทียบเพดาน 300 ล.
- **ผมไม่รู้สูตรที่การ์ดใช้แน่** (นับสถานะไหน / ปีงบไหน) → ห้ามสรุปว่าผิดเท่าไรจนกว่าจะตรวจสูตรจริงในไฟล์ tracker
- แต่ขนาด 297.7 ล. เทียบเพดาน 300 ล. = **มีนัยสำคัญแน่นอน** ต้องตรวจก่อนใช้ตัวเลขการ์ดนี้ตัดสินใจยื่นซอง

### 📤 ส่งต่อ OPY (insert = scope OPY ไม่ใช่ DA · Core Rule 22)
- สร้าง `_handoff_OPY_missing53_MAPPED.csv` (43,640 B) — map เข้า schema seed_bids ให้แล้ว
  - `entity` map ตามตารางบน · `status` → `จัดทำสัญญาแล้ว` · วันที่แปลง พ.ศ. → ISO
  - `fiscalYear` = **2569 ทั้ง 53 รายการ** (คำนวณจากวันลงนาม เกณฑ์ ≥ ต.ค. = ปีงบถัดไป)
  - `seq_suggest` = **183–235** เรียงตามวันลงนาม (OPY ตัดสินเลขจริง)
  - เว้นว่าง 4 ช่องที่ต้องเติมมือ: `budget` `pct` `plant` `workType`
- ⚠️ ข้อมูลชุดนี้ถึงแค่ ~มี.ค.–เม.ย. 69 (ไฟล์โหลด 13 มิ.ย.) → โหลดชุดใหม่จาก data.go.th จะได้เพิ่ม
- 🧹 ลบไฟล์ temp `_tmp_rmn_missing_53.csv` ออกจาก repo แล้ว

### 🛠️ บทเรียน
- **ข้อมูลรัฐสะกดชื่อห้างผิดได้** (`ร่ามค้า`) → การค้นหาชื่อบริษัทในชุดข้อมูลภาครัฐต้องค้นหลายรูปแบบเสมอ ไม่ใช่แค่ชื่อที่ถูก
- ก่อนเชื่อรายงาน "ขาด N รายการ" ต้องเช็คก่อนว่า **field ที่ใช้จับคู่มีอยู่ในทั้งสองฝั่งจริง** — ถ้า seed_bids ไม่เก็บรหัสโครงการ ผลลัพธ์ 0 matches จะไม่มีความหมายเลย

---

> 📦 ย้ายเข้ามา 2026-09-02 (WRK_DA เกินเพดาน 20 KB) — เนื้อหาเดิมครบ ไม่ตัด

## 🔄 Session State (2026-08-26 — DA: backfill 28 e-bidding FY2569 ลง seed_bids)
> ต่อจาก session 08-25 · DB ส่ง dataset id + กับดักมาให้ (memory `project_egp_open_data.md`)
> ⚖️ **user มอบงานเติมข้อมูลนี้ให้ DA โดยตรง** (ทับ note เก่า 2026-07-14 ที่ให้ seed_bids เป็น read-only สำหรับ agent อื่น)

### ✅ เจอ budget แล้ว — ปลดล็อกที่ค้างเมื่อวาน
- `Downloads\2569-egp-contract\*.csv` มี **28 คอลัมน์** · คอลัมน์ 9 = `วงเงินงบประมาณ (บาท)`
- 🔑 **CSV ในเครื่องไม่มี column shift** (shift +7 เป็นปัญหาของ **API** เท่านั้น) → ใช้ชื่อคอลัมน์ได้ตรงๆ
- สแกน 2,745,560 บรรทัด (6 ไฟล์ 2.9 GB) ด้วย StreamReader + pre-filter keyword → 272 แถว → กรองแม่น 81 โครงการ

### ✅ พิสูจน์วิธีดึงด้วยของจริงก่อนเขียน
- เอา **28 โครงการที่มีใน tracker แล้ว** มาเทียบ: `budget` `bid` `midPrice` **ตรงเป๊ะ 28/28**
- cross-check ด้วย **TIN 6 ห้าง** ได้ผลเท่ากับกรองด้วยชื่อทุกตัว (49/18/11/3 = 81) → ไม่มีตกหล่นจากชื่อสะกดผิด
- `pct = (1 − bid/budget)×100` = สูตรมาตรฐาน (306 records ใช้สูตรนี้)
  - 🟠 **หนี้ข้อมูลเก่า**: เจอ 10 records ที่ pct คิดจาก `midPrice` ไม่ใช่ `budget` → ยังไม่แก้ บันทึกไว้

### 🔴 "ขาด 53" ไม่ใช่ 53 สำหรับ tracker นี้ — แยก 2 กอง
| กอง | n | มูลค่า | ตัดสิน |
|---|---|---|---|
| **e-bidding** | **28** | **292,336,000** | ✅ เติมแล้ว |
| เฉพาะเจาะจง | 25 | 5,372,493 (7,500–491,400) | ⏸️ ไม่เติม — ซื้อวัสดุ/จ้างเฉพาะเจาะจง ไม่ใช่งานประมูล · 28 ตัวที่อยู่ใน tracker เดิมเป็น e-bidding 28/28 |

### 🔑 สาเหตุที่หาย — เชิงระบบ ไม่ใช่หายสุ่ม
28 e-bidding ที่ขาด แยกตามผู้ยื่น: **กิจการร่วมค้า ตักสิลา 14 · กิจการร่วมค้า RMN 9 · กิจการร่วมค้า รักดี 3 · หจก. RMN เอง 2**
→ **26/28 เป็นงานที่ยื่นในนามกิจการร่วมค้า** — งาน JV ไม่ได้ถูกคีย์เข้า tracker

### 📊 ผลที่เปลี่ยน
```
seed_bids.js  558 → 586 records   seq FY2569 183-210 (seq เป็นเลขต่อปีงบ · เดิม 1-182 unique)
FY2569 bid (สถานะทำสัญญาแล้ว)  131,708,423 → 424,044,423
FY2568 ไม่กระทบ                308,197,279
```
> 📌 **user ยืนยัน: เกิน 300 ล. ไม่ใช่เรื่องใหม่** — RMN overrate SME → ต่ออายุ SME ไม่ได้ → ยื่นงานในนาม RMN ไม่ได้ → **เปลี่ยนไปใช้ รักดี** · ตัวเลขที่เพิ่มมาแค่ทำให้ tracker ตรงกับความจริงที่เกิดขึ้นแล้ว
> 🔎 แต่ในชุด 2569 **หจก.รักดีการโยธา (TIN 0443567000931) ชนะ 0 โครงการ** — มีแค่ `กิจการร่วมค้า รักดี` 3 · ถ้ารักดีคือตัวยื่นหลักตอนนี้ ควรเช็คว่ายังไม่ชนะจริง หรือข้อมูลชุดนี้เก่าเกิน (ถึง ~มี.ค.–เม.ย. 69)

### ⚠️ 2 ฟิลด์ที่ทำให้ตรงของเดิมไม่ได้ — ใส่แบบไม่เดา
- `date` — seed ใช้ **วันยื่นซอง** ซึ่งชุดข้อมูลรัฐไม่มี · วัดจาก 28 ตัวที่ทับกัน = วันประกาศ + 6…18 วัน (กลาง 8)
  → ใส่ **วันประกาศตรงๆ ไม่บวกเดา** + เขียนกำกับใน `note` ทุกแถว
- `name` — OPY ย่อชื่อเอง (ตรงเป๊ะ 0/28) → ใส่ชื่อเต็มจากต้นฉบับรัฐ
- `plant` `workType` `plantDist` `lowest` เว้นว่าง — ปกติของ schema (มีค่าแค่ 112/105/75/113 จาก 558)

### 🛠️ บทเรียน
- **API shift ≠ CSV shift** — ปัญหา column shift +7 อยู่ที่ API ของ opend เท่านั้น ไฟล์ CSV ที่โหลดตรงเรียงถูก
- ก่อนเติมข้อมูลก้อนใหญ่ ให้เอา **records ที่ทับกันอยู่แล้วมาเทียบก่อน** = ได้ ground truth ฟรีว่าวิธีดึงถูกไหม
- ตรวจ scope ของตารางก่อนเติม — tracker นี้เก็บเฉพาะ e-bidding ถ้าใส่เฉพาะเจาะจงเข้าไปจะเพี้ยนทั้ง dashboard
- 🧹 ลบ `_tmp_egp2569_match.csv` ออกจาก repo แล้ว

### ⏳ Pending
1. 25 รายการเฉพาะเจาะจง (5.37 ล.) — user ตัดสินว่าจะเก็บที่ไหน (ไม่ควรอยู่ tracker ประมูล)
2. 10 records เก่าที่ pct คิดจาก midPrice — ควร normalize เป็น budget-based
3. `date` ของ 28 แถวใหม่ = วันประกาศ · ถ้าได้วันยื่นซองจริงมาให้แก้ทับ
4. เช็คว่า หจก.รักดีการโยธา ชนะงานอะไรไปแล้วหรือยัง (ชุด 2569 ว่าง) — ต้องข้อมูลใหม่กว่า มี.ค. 69

---
