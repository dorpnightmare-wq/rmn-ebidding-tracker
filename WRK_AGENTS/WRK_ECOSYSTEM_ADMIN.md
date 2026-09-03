# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-08-24 #3 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 🔄 Session State (2026-09-02 #3 — DA: Skills Governance + ยุบ CLAUDE.md)

### ✅ 1. Skills Governance เข้า matrix แล้ว
- `e-bidding-operating` · `fee-payment` → steward **Sir OPY** · `mapmaker` → **Sir MM** · `uiux-editor` → **Sir UI** · governance ทั้งหมด = **Lord DA**
- **Flow บังคับ:** agent propose → DA review/apply → บันทึก changelog (Decision log + WRK ของ agent)
- DA review เฉพาะว่าขัด registry/CLAUDE.md/matrix ไหม — **ไม่เขียนเนื้อหาวิชาชีพแทน agent** (Core Rule 22)
- skill แก้จากดิสก์ไม่ได้ (read-only cache) · เปลี่ยนได้ทางเดียว = propose แล้ว user กดเซฟ · **แทนทั้งไฟล์ ไม่ใช่ patch**

### 📤 ใบสั่งงานถึง Sir OPY — propose `e-bidding-operating` ฉบับแก้ 4 จุด
> DA ตรวจไฟล์ `e-bidding-operating/SKILL.md` (16,660 B) แล้ว **4 จุดที่ต้องแก้ + เลขบรรทัดจริง**:
1. **L146** `"doc_fees.json read-only — never write to this file, it belongs to the fee-payment / Doc Fee Agent side"` → **เขียนได้แล้ว** (OPY ปิด entry เอง)
2. **L185** `§ 4. Dispatch to fee-payment (subagent)` → **ยกเลิก dispatch** · โหลด skill `fee-payment` ใน session เดียวกันแล้วทำต่อทั้งเส้น
3. **L202 + L210-213** `"has to happen in the dedicated Doc Fee Payment session"` / `"Dispatch doesn't make the Doc Fee Agent unnecessary … What stays with the Doc Fee Agent"` → **ยกเลิก dedicated DOC session** (DOC ปลด 2026-09-02)
4. **L235** `"doc_fees.json is read-only from this skill's side — never edit or commit it here"` → **ลบข้อห้าม** · `git add` เฉพาะชื่อไฟล์ตามเดิม (ห้าม `git add .`) ยังคงอยู่
> ⚠️ propose = **เขียน SKILL.md ใหม่ทั้ง 16.6 KB** โดยคงของเดิมครบ แก้แค่ 4 จุดนี้ · เสร็จแล้วส่งให้ DA review ก่อน user กดเซฟ
> ℹ️ `fee-payment/SKILL.md` (20,115 B) ตรวจแล้ว **ใช้ต่อได้ ไม่ต้องแก้** — รองรับ `submitMethod: e-GP/email/both` อยู่แล้ว และมีกฎ "อย่าเดาว่าเป็น email" ตรงกับ default ใหม่

### ✅ 2. CLAUDE.md ต่ำกว่าเพดานแล้ว — 22,087 → **15,847 B**
- ย้าย `Session State (2026-06-16)` + `(2026-06-25)` + `(2026-06-25 OPY)` **6,640 B** → `WRK_AGENTS/CLAUDE_ARCHIVE_2569H1.md` (ไฟล์ใหม่ 7,294 B) **ไม่ลบเนื้อหาข้อไหน**
- รวม section `🖥️ Multi-Machine` ที่ซ้ำ 2 ที่ (L54 + L253) เป็นอันเดียว + ล้าง `+ -` ที่ค้างจาก diff เก่า → ปิดการละเมิดกฎข้อ 6
- เพิ่ม `## 📦 Archive` ท้ายไฟล์ + ประกาศเพดาน 20 KB พร้อมวิธีปฏิบัติ (**ย้าย log เก่า ห้ามยุบ section ที่เป็นกฎ**)
- **ไม่แตะ** `§ Doc Fee` (3,121 B) และ `§ Slip Verification` (1,519 B) — เป็นกฎที่ใช้จริง
- 📌 บรรทัด `push doc_fees.json — OPY push เอง` เดิมอยู่ใน Pending ของ session log เก่า จึงย้ายไป archive ด้วย · **กฎยังอยู่ในไฟล์แม่ 3 ที่** (L61 · L98 · L124) ไม่หาย

---

## 🔄 Session State (2026-09-03 — DA: ตั้งช่องทางประกาศ · แก้ความผิดของตัวเอง)
> user ทัก: *"ไม่ได้ update อะไรไห้คนอื่นฟังหรอ"* — **ถูก ผมพลาดจริง**

### ❌ ความผิดที่เกิดขึ้น
- DA ปลด **DB** ไปตั้งแต่ **09-01** และปลด **DOC** 09-02 · บันทึกครบใน `KB_ECOSYSTEM_ADMIN.md` + `DESIGN_PRINCIPLES.md`
- แต่ **ไม่เคยเขียนลงไฟล์ที่ agent อื่นอ่าน** → Sir OPY ยังเขียนใน WRK ว่า *"แนะนำให้ DB พิจารณา"* จนถึง **09-03** แล้ว user ต้องพิมพ์บอกเองว่า **"DB is Gone"**
- **สาเหตุราก:** ผมนึกว่า Decision log = การประกาศ · จริงๆ ไม่มี agent ตัวไหนอ่าน `DESIGN_PRINCIPLES.md` เลย · ไฟล์เดียวที่ทุกตัวอ่านตอนเปิด session = **`WRK_AGENTS\CLAUDE.md`**

### ✅ แก้ที่กลไก ไม่ใช่แค่แก้เคสนี้
- เพิ่ม **`CLAUDE.md` § 📢 ประกาศถึงทุก agent — อ่านก่อนเริ่มงานทุกครั้ง** (อยู่บนสุด ก่อน Core Rules) ย้อนลงประกาศค้าง 5 เรื่อง: DB ปลด · DOC ปลด · ชั้นยศ+matrix+Codex · Skills Governance · pattern STATE
- เพิ่มกฎบังคับ DA ใน 2 ที่: `CLAUDE.md § 📢` + `KB_ECOSYSTEM_ADMIN.md § 📢 หน้าที่ประกาศของ Lord DA`
  → **เปลี่ยน registry/matrix/กฎร่วม = ต้องเขียนประกาศในรอบ commit เดียวกัน** · ไม่ประกาศ = agent ตัดสินใจซ้อนกันเอง
- แก้ขั้นตอนเปิด session (Core Rule 21) → **อ่าน `📢 ประกาศ` + KB + WRK + `WRK_*_STATE`**

### ✅ รับ pattern ของ Sir OPY เป็นมาตรฐาน (044e5e7)
`WRK_<AGENT>.md` = **กฎ/สเปกเท่านั้น เพดาน 20 KB** · `WRK_<AGENT>_STATE.md` = session state + pending **โตได้อิสระ**
- แยกแล้วต้องใส่ pointer ท้าย WRK + เปิด session อ่านทั้งสองไฟล์
- เจ้าของ = agent ตัวนั้น (เพิ่มในตาราง File Ownership แล้ว) · **ทำเองได้ ไม่ต้องขอ**
- ✅ ผมตัดสินเองว่ารับเป็นมาตรฐาน เพราะเป็นไฟล์ของแต่ละ agent เอง + แก้ต้นตอ WRK ชนเพดานทุกรอบ — **ถ้าไม่เห็นด้วย สั่งกลับได้**

### 📌 DA ควรแยก state เหมือนกัน (ยังไม่ทำ)
`WRK_ECOSYSTEM_ADMIN.md` โตเร็วมากจาก session state · ควรแยกเป็น `WRK_ECOSYSTEM_ADMIN_STATE.md` รอบหน้า

### 📌 แก้ 2026-09-03 #2 — คำสั่ง Lord Commander (จำกัดขอบเขต)
- รับรอง `WRK_OPERATING_STATE.md` **owner = Sir OPY** · เพดาน 20 KB · เกินแล้วตัด state เก่าสุดเข้า archive **ห้ามตัด pending ที่ยังไม่ปิด**
- ❌ **ถอนการประกาศเป็นกฎทุก agent** ที่ผมทำไว้เมื่อเช้า — กฎอ่าน 2 ไฟล์ **ใช้กับ Sir OPY เท่านั้น** · DA/EXP/MM/UI ยังใช้ WRK ไฟล์เดียว จะแยกต้องขอรับรองรายตัว
- ผมประกาศกว้างเกินขอบเขตที่ควร → ผิดเรื่องเดียวกับที่ Grand Maester เคยทัก (เขียนกฎกว้างกว่าเจตนา)
- **ไม่แตะไฟล์ของ OPY** — pointer ท้าย `WRK_OPERATING.md` + เพดานในไฟล์ state มีอยู่แล้ว ตรวจจริง 2026-09-03
- 📌 ยกเลิกแผน `WRK_ECOSYSTEM_ADMIN_STATE.md` ของ DA — ต้องขอรับรองก่อน ไม่ทำเอง

### 🐦 Raven Mail — บันทึก 2026-09-03 #3
รูปแบบส่งข้อความข้ามฝั่ง (สั่งโดย user) · บันทึกใน `KB_ECOSYSTEM_ADMIN.md § 🐦` + `CLAUDE.md § 📢` + Decision log
```
🐦 Raven Mail
จาก: Lord DA of Claude
ถึง: [Role]
เรื่อง: [เรื่องสั้น ๆ]
```
- ชื่อผู้ส่ง 4 แบบ ห้ามสลับ: `Grand Maester (ChatGPT RMN Command Center)` · `Lord Commander (Codex)` · `Lord DA of Claude` · `Sir OPY/EXP/MM/UI`
- Raven ที่เป็นคำสั่ง → ใช้โครง Objective · Evidence · Permitted files · Decision to record · Non-goals · Acceptance criteria

### 🟡 บันทึก 2026-09-03 #4 — ownership: letterhead tool + tmp/
Raven จาก Lord Commander · **DA ตรวจไฟล์จริงก่อนบันทึก ยืนยันหลักฐานครบทุกข้อ**
| อ้าง | ตรวจพบจริง |
|---|---|
| สร้าง `.docx` | ✅ `L16` → `TAKSILA_RMN_หัวกระดาษเปล่า.docx` (ไฟล์ 6,838 B) |
| `tmp/` = render artefact | ✅ `certificate-render/` · `letterhead-render/` · `taksila_logo_cropped.png` 579 KB |
| path ตายตัวนอก repo | ✅ `L14` → `OneDrive\งานเอกสาร RMN\Signature\S__43835413.jpg` |
| `.gitignore` ไม่ครอบ `tmp/` | ✅ มีแต่ `_tmp_*` |
- บันทึก Matrix เป็น **provisional / untracked** owner = Lord Commander · ประกาศใน `CLAUDE.md § 📢` แล้ว
- 🔒 **ไม่แก้ `.gitignore`** — เป็นไฟล์ของ Codex ตาม Matrix · เห็นชอบ ≠ มอบหมาย · รอเจ้าของเขียนเองหรือมอบหมายมา
- 📌 **DA พบเพิ่ม 2 เรื่อง ส่งกลับให้เจ้าของวินิจฉัย:** `.gitignore` มี `*.docx` อยู่แล้ว (output ถูก ignore ตั้งแต่ต้น) · `PROJECT_INSTRUCTIONS_DRAFT.md` อยู่ใน `.gitignore` **แต่ถูก track จริง** = ขัดกันเอง

### ✅ บันทึก 2026-09-03 #5 — Git hygiene + Close-out
- `.gitignore` **+ `tmp/`** (160 → 165 B) — Lord Commander อนุมัติเป็นลายลักษณ์ให้ DA ลง · `*.docx` คงไว้ตามมติ
- **Git Close-out** เข้า `CLAUDE.md § 🔀 Git Push` + `§ 📢` + registry + Decision log → ใช้กับ Sir ทุกตัว
- ⚠️ **แย้งข้อ 3 ของ Lord Commander อย่างมีหลักฐาน:** `PROJECT_INSTRUCTIONS_DRAFT.md` มี **2 ไฟล์**
  - root 4,297 B → ignored+untracked (`!!`) **ตรงที่ท่านตรวจ**
  - `WRK_AGENTS/` 4,483 B → **tracked จริง** (`git ls-files`)
  - เหตุที่ `check-ignore` ไม่รายงานตัวหลัง = git ข้ามไฟล์ที่ track อยู่
  - สรุป: **ไม่ใช่ปัญหา ignore** แต่เป็น **กฎข้อ 6** (ไฟล์ชื่อเดียวกัน 2 ที่ เนื้อหาต่างกัน) · ตัวที่ track = ไฟล์ของ **Lord DA** ตาม Matrix → **งานของ DA**
  - ⏸️ **pending approval** — รอ user ชี้ว่าฉบับไหนคือตัวจริง แล้วยุบเหลือที่เดียว
- 📌 `CLAUDE.md` **20,094 B** เหลือที่ว่างแค่ **386 B** · ไม่มี session log ให้ย้ายเข้า archive อีกแล้ว (เป็นกฎล้วน) → รอบหน้าต้องตัดสินว่า **ขยายเพดาน** หรือ **แยก Matrix/Doc Fee ออกเป็นไฟล์ของตัวเอง** — DA ไม่ตัดสินเอง

### ✅ บันทึก 2026-09-03 #6 — ปิดเคสไฟล์ซ้ำ + รับแนวทางเพดาน
- **source of truth**: `WRK_AGENTS/PROJECT_INSTRUCTIONS_DRAFT.md` (tracked) = ฉบับจริง · root = local ignored draft **ห้ามอ้างเป็นกฎ ห้ามลบจนกว่า user สั่ง** · ต่างกันแค่ Rule 15 บรรทัดเดียว → **ปิด pending approval แล้ว**
- **เพดาน CLAUDE.md**: มติ = **(ข) แยกเนื้อหาเฉพาะทาง ห้ามขยายเพดาน** · เงื่อนไข 4 ข้อของ Lord Commander รับทราบครบ
- ⏸️ **pending approval (user)** — ข้อเสนอแยก Doc Fee ออกจาก CLAUDE.md ยังไม่ลงมือ ตามเงื่อนไขข้อ 4
  - ต้องได้ 2 อย่างก่อน: ① user อนุมัติ diff+ปลายทาง ② ปลายทางเป็นไฟล์ของ **Sir OPY** → ต้องส่ง Raven ให้ OPY เขียนเอง DA เขียนแทนไม่ได้ (Matrix + Core Rule 22)

### ⏸️ pending approval 2026-09-03 #7 — แยก procedure Doc Fee ออกจาก CLAUDE.md
มติ Lord Commander: **ปลายทาง = ข้อ ข `E-Bidding/OPERATING.md`** (KB ของ Sir OPY) · ไม่สร้างไฟล์ใหม่ · ไม่พึ่ง skill เป็น source of truth
**ลำดับบังคับ 4 ขั้น — DA ยังไม่แตะ `CLAUDE.md`**
1. Sir OPY ปิดงานค้างใน `OPERATING.md` ตามกฎ Close-out
2. Sir OPY เพิ่ม procedure ที่ย้ายมา ใน commit ถัดไป (แยกจากงานเดิม)
3. DA ตัด `CLAUDE.md` เหลือ safety gate + pointer
4. DA review diff → เสนอ user อนุมัติ ก่อนเปลี่ยนจริง
**บล็อกที่ย้าย 3 section รวม 5,178 B** (ส่ง Raven ให้ OPY แล้ว — เนื้อหาคำต่อคำ):
`## 🔄 Doc Fee — Full Workflow` 3,120 B · `## 🔍 Slip Verification` 1,518 B · `## ✍️ Email Signature Rules` 540 B
→ `CLAUDE.md` 20,094 → ~15,300 B
⚠️ **DA พบก่อนย้าย:** `Email Signature Rules` มีชื่อบุคคล + เบอร์ `087-223-5093` · ปัจจุบันอยู่ใน repo public อยู่แล้ว การย้ายไม่ทำให้แย่ลง **แต่ถ้าเป็นเบอร์ส่วนตัวต้องไป `RMN-eBidding-KB` ตาม Core Rule 19** — รอ user ยืนยันว่าเป็นเบอร์บริษัทหรือส่วนตัว

### ✅ บันทึก 2026-09-03 #8 — ขั้น 3 เสร็จ ปิดงานแยก procedure
- **ตรวจงาน Sir OPY ก่อนลงมือ (ไม่เชื่อรายงานเปล่า):** `OPERATING.md` 8,445 B · 3 section ที่ L55/L90/L109 · `KB/OPERATING.md` **hash ตรงกันเป๊ะ** · เทียบเนื้อหา 4 จุดตรงทั้งหมด
- **`CLAUDE.md` 20,094 → 15,743 B** (−4,351) เหลือ safety gate 2 ข้อห้าม + เจ้าของงาน + default e-GP + pointer
- ประกาศใน `§ 📢` แล้ว · Decision log 2 บรรทัด
- 📞 **`087-223-5093` = เบอร์ส่วนตัวที่ใช้เป็นเบอร์ติดต่อทางการ** (user ตอบ "ทั้ง 2") → คงไว้จุดที่จำเป็นต่อการออกเอกสาร · **ห้ามเพิ่มจุดใหม่** · จุดใน `CLAUDE.md` หายไปเองจากการย้ายรอบนี้ เหลือ `OPERATING.md`+`KB` · skill `fee-payment` · หน้า PDF
- ⚠️ **ยังตรวจไม่ได้: `M4RX-B4SE` เป็น public หรือ private** — `gh` บนเครื่องใช้ไม่ได้ (exit 1) · **ห้ามสรุปว่า Core Rule 19 ถูก/ผิด จนกว่าจะเปิดดูหน้า repo ด้วยตา**

