# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-08-24 #3 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 🔄 Session State (2026-09-02 — DA: ยุบ DOC เข้า OPY)
> คำสั่ง user: "น่าจะต้อง Disable DOC ไว้ก่อน เพราะไม่ได้ใช้เลย OPY ใช้ Skills แล้วสร้างได้ไวกว่าแต่ติดที่กฎเรื่อง push"

### 🔎 หลักฐานก่อนแก้ (ไม่เดา — อ่านจากไฟล์/git จริง)
- `WRK_FEE_PAYMENT.md` แก้ครั้งสุดท้าย **04-08-69** (~4 สัปดาห์) = ไม่มีใครเปิด session DOC เลย
- `git log doc_fee_queue.json` → commit ล่าสุดทั้งหมดเป็น **`fee(OPY): ...`** · `doc_fees.json` ก็ปิด entry จาก session OPY (e418c7c, 6623292)
- **ตัวบล็อกจริง = `CLAUDE.md:90`** `| BIDDING OPERATING | seed_bids.js เท่านั้น | tracker HTML, doc_fees.json |` → OPY เขียน doc_fees.json ไม่ได้ → entry ค้าง pending รอ agent ที่ไม่มีใครเปิด
- queue ปัจจุบัน 17 entries · doc_fees.json 34 entries

### ✅ แก้ไปแล้ว
- `CLAUDE.md` — ตาราง Agents: OPY แก้ได้ `seed_bids.js` + `doc_fee_queue.json` + `doc_fees.json` (ห้ามแตะแค่ tracker HTML) · row DOC → 🚫 DISABLED · § Doc Fee เปลี่ยนเจ้าของเป็น OPY ผ่าน skill `fee-payment` · step 5 ช่องทางส่งหลักฐาน default = แนบ e-GP (อีเมลเฉพาะเมื่อหน่วยงานระบุ) · step 7 + ท้ายไฟล์ = OPY push เอง
- `KB_ECOSYSTEM_ADMIN.md` — ถอด row Fee Payment ออกจาก registry → เข้าตาราง "ยกเลิกแล้ว" (เก็บไฟล์ ห้ามลบ) · OPY row รับ scope ค่าเอกสาร · nickname ตัด DOC · **agent ใช้งานจริง 6 → 5 ตัว**
- `KB_FEE_PAYMENT.md` — ติดป้าย 🚫 DISABLED ที่หัวไฟล์ (เนื้อหาสเปกคงไว้ทั้งหมด อ่านอ้างอิงได้)
- `DESIGN_PRINCIPLES.md` — Decision log 2 บรรทัด (ยุบ DOC · default e-GP) + แก้จำนวน agent 6→5 ทั้ง 2 จุด

### ⚠️ ค้าง / ที่ DA ทำให้ไม่ได้
- **skill `fee-payment` + `e-bidding-operating`** อาจยังเขียนว่า "dispatch ไป DOC" — skill เป็น read-only cache **DA แก้จากดิสก์ไม่ได้** ต้อง propose ให้ user save → **ยังไม่ตรวจเนื้อหา skill จริง อย่าเพิ่งสรุปว่าต้องแก้**
- `CLAUDE.md` = **22,087 B เกินเพดาน 20 KB** (เดิม 21,573) — ยุบได้จริงคือ § Doc Fee + § Slip Verification ที่ทับกับ skill แต่นั่นเป็นการเปลี่ยนระบบ **รอ user อนุมัติก่อน ไม่ทำเอง**
- queue `68099553809` ยัง pending — ตอนนี้ **OPY ปิดเองได้แล้ว** ไม่ต้องรอ DOC

---

## 🔄 Session State (2026-09-02 #2 — DA: รับ Codex + File Ownership Matrix)
> user เลือก **ตัวเลือก B** · Advisor สั่งให้เขียน matrix ก่อนเปลี่ยนชื่อยศลงเอกสารจริง — ทำตามลำดับนั้นแล้ว

### 👑 ชั้นยศ (alias — ไม่เปลี่ยน scope)
Grand Maester = ChatGPT RMN Command Center (ที่ปรึกษา ไม่แตะไฟล์) · **Lord Commander = Codex** (งานเทคนิค/ข้ามระบบ · แก้เฉพาะไฟล์ที่เป็น Codex owner) · Lord DA = DA (KB/registry/routing/Decision log) · Sir OPY/EXP/MM/UI = เจ้าของงานตาม domain · ~~Sir DOC~~ ปลดแล้ว

### 🗂️ File Ownership Matrix (เขียนจาก `git ls-files` จริง)
- `RMN-eBidding-Workflow` **26 ไฟล์ tracked** → OPY: seed_bids.js, doc_fee_queue.json, doc_fees.json, handoff csv · UI: tracker html, index.html, logo · MM: map_input.png · แต่ละ agent: WRK ตัวเอง · **DA**: CLAUDE.md, KB/, assets.json, BOOTSTRAP_IOS, PROJECT_INSTRUCTIONS_DRAFT, morning-prompt
- **Codex owner (5 ไฟล์)**: `scripts/harvest_all.ps1` · `scripts/harvest_egp.ps1` · `scripts/pull_egp.py` · `.gitignore` · `.claude/launch.json` → Claude **รันได้ แก้ไม่ได้**
- ✅ **แก้แล้ว 2026-09-02:** `WRK_AGENTS/scripts/generate_fee_pdf_fixed.py` → **owner = Sir OPY** (ไม่ใช่ Codex) · Codex review/ช่วยแก้ได้เมื่อได้รับมอบหมาย
  → **เส้นแบ่งที่ได้:** ไฟล์ที่ agent ใช้ทุกงาน = agent เป็น owner · เครื่องมือ/infra ที่ใช้เป็นครั้งคราว = Lord Commander
- `M4RX-B4SE` = 20 .md + 5 .gitkeep **ไม่มีโค้ดเลย** → DA ทั้ง repo · `RMN-eBidding-KB` = DA + EXP · **Codex ไม่แตะ (PII/Core Rule 19)**
- **ไฟล์ที่ไม่อยู่ใน matrix = ยังไม่มีเจ้าของ ต้องถามก่อนแก้**

### ✅ จุดเสี่ยงที่ปิดแล้ว
`generate_fee_pdf_fixed.py` = ตัว generate PDF ที่ OPY ใช้ทุกงาน → ย้าย owner มาเป็น **Sir OPY** ตามที่ user สั่ง · กันคอขวดแบบเดียวกับที่เพิ่งยุบ DOC ไป

### ⏳ ค้างจากรอบก่อน (ยังไม่แตะ)
1. skill `fee-payment` / `e-bidding-operating` อาจยังเขียน dispatch ไป DOC — ยังไม่เปิดอ่าน skill จริง
2. `CLAUDE.md` 22,087 B เกินเพดาน 20 KB — ยุบได้แต่เป็นการเปลี่ยนระบบ รออนุมัติ
3. ~~queue `68099553809` pending~~ → ✅ **ปิดแล้ว** (ตรวจ 2026-09-02: queue `status:done` · `doc_fees.json` มี entry `paidDate 2569-09-02` `submitMethod e-GP`) · OPY sync WRK แล้วที่ 2722f2d — **รายการค้างข้อ 3 ของผมเป็นข้อมูลเก่า แก้แล้ว**

---

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
