# RMN e-Bidding Tracker

## 🚫 NEVER USE (no exceptions)
TaskCreate · TaskUpdate · TaskList · TaskStop · TaskGet · AskUserQuestion · mcp__visualize__read_me

## 📌 Session Policy (STRICT)
- **ห้าม compact session เอง** — ถ้า context ใกล้หมด → แจ้ง "กรุณา Restart session" แทน
- เหตุผล: context ก่อน compact จะหายไปทั้งหมด ทำให้งานค้างเสียหาย
- **Email Check Box ต้องเป็น interactive widget** (mcp__visualize__show_widget) — ไม่ใช่ markdown ☐
ToolSearch → โหลดเฉพาะเมื่อ tool ไม่มีใน schema จริงๆ

## 📢 ประกาศถึงทุก agent — **อ่านก่อนเริ่มงานทุกครั้ง**
> 🔴 **DA ต้องเขียนที่นี่ทุกครั้งที่เปลี่ยน registry/ownership/กฎร่วม — ในรอบ commit เดียวกัน** · ไม่ประกาศ = agent อื่นตัดสินใจซ้อนกันเอง (เกิดจริง 09-03: OPY ไม่รู้ว่า DB ปลด) · เก่ากว่า 30 วัน → `CLAUDE_ARCHIVE_*.md`

- **09-05 · 📞 ปิดเคส PII เบอร์ติดต่อ** — `087-223-5093` + ชื่อหุ้นส่วนผู้จัดการ = **เบอร์ธุรกิจ อยู่ใน repo public ได้** (มติ user) · **ไม่ต้อง mask ไม่ต้องย้าย** · Sir OPY ยกเลิกคำสั่งหยุดที่ DA สั่งไว้ · ⚔️ ปิดข้อขัดกัน Rule 19 vs 20 — sync KB ลง `KB/` ได้ตามปกติ · ⛔ ข้อยกเว้นนี้เฉพาะรายการนี้ เลขบัตร/เบอร์ส่วนตัวพนักงาน/เงินเดือน ยังอยู่ใต้ Rule 19 เต็ม
- **09-04 · checker เช้า = `Work Health Check` แล้ว (เลิกนับ turn/context)** — วัด git status · HEAD vs origin · ขนาด/mtime ของ WRK · pending ทั้งระบบ · **read-only 100% ห้าม commit/push/pull/fetch** · รายงานต้องบอก **อะไรค้าง + owner + ต้องทำอะไรต่อ** · 📌 **เปลี่ยน registry ครั้งหน้าต้องไล่ตรวจ SKILL.md ทั้ง 4 ตัวด้วย** (อยู่นอก git ไม่มีใครเตือน)
- **09-03 · ✅ Git Close-out** — งานเสร็จ = `git status` scope ตน → commit → push · ห้าม commit ไฟล์นอก ownership · รอ approval ให้เขียน `pending approval` (รายละเอียด § 🔀 Git Push)
- **09-03 · 🐦 Raven Mail = รูปแบบส่งข้อความข้ามฝั่ง** — ส่งถึง Lord COMMANDER of GPT / Codex / ข้าม agent ต้องขึ้นหัว `🐦 Raven Mail` + `จาก:` + `ถึง:` + `เรื่อง:` · **ชื่อผู้ส่งต้องตรงตัวจริง ห้ามสลับ** (รายชื่อเต็มใน `KB_ECOSYSTEM_ADMIN.md § 🐦`)
- **09-03 · `WRK_OPERATING_STATE.md` — owner Sir OPY · เฉพาะ Sir OPY** · OPY เปิด session อ่าน **2 ไฟล์** (`WRK_OPERATING.md`=กฎ + STATE=state/pending · เพดาน 20 KB ทั้งคู่ · เกินแล้วตัด state เก่าสุดเข้า archive ห้ามตัด pending) · ❌ **ไม่ใช่กฎทุก agent** — DA/EXP/MM/UI ใช้ WRK ไฟล์เดียว จะแยกต้องขอรับรองรายตัว
- **09-07 · 👑 naming model ใหม่ (มติ King Marx)** — ฝั่ง GPT = **`Lord COMMANDER of GPT`** · `COMMANDER GATEWAY` = ชื่อห้องแชทตั้งต้น/จุดรับเรื่อง **ไม่ใช่ตำแหน่ง** · `Grand Maester` = **retired** · Codex เรียกตามหน้าที่ **`Codex / Technical Execution`** · `Lord` = ผู้ดูแลอาณาจักร/ระบบของตน · ชื่อเก่าในบันทึกเดิม **คงไว้** แต่ Raven/เอกสาร/แผนผังที่เป็น **current ต้องใช้ชื่อใหม่**
- **09-07 · 👑 Raven = บล็อกเดียว copy ได้ + user กดส่ง = ยืนยันแล้ว** — King Marx กดส่ง Raven = ยืนยันเจตนา/ความถูกต้อง **ไม่ต้องขอยืนยันซ้ำ** · **ผู้ตัดสินเมื่อ 2 ฝั่งขัดกัน = King Marx เท่านั้น** · agent เสนอหลักฐานครบ 2 ด้าน **ห้ามตัดสินแทน**
- **09-07 · 💰 Finance Capture v1 = ระบบใหม่ แยกจาก e-Bidding โดยสิ้นเชิง** — `LINE → Cloud Run → Drive + hidden Sheet` · เจ้าของโค้ด/config = **Lord DA** · เจ้าของ Cloud resource ทุกตัว = **King Marx** (ตาราง 2 ชั้นอยู่ใน `KB_ECOSYSTEM_ADMIN.md § 💰`) · ⛔ **ห้ามอ้างอิงข้อมูล Finance Capture จาก repo public / Pages / tracker ทุกกรณี** — สลิปมีเลขบัญชี+ชื่อ = Rule 19 เต็มตัว · ที่ส่งออกได้คือ `[ยอด · วันที่ · ประเภท · record_id]` เท่านั้น
- **09-07 · 💰 ขอบเขต Finance Capture = "จ่ายจริง" เท่านั้น** — Sheet นี้ **ตอบไม่ได้** ว่าหนี้คงเหลือเท่าไหร่ / เหลือกี่งวด / ครบเมื่อไหร่ (ตารางแผนผ่อนยังไม่ถูกสร้าง) · ห้าม agent ใดอ่านยอดรวมใน Sheet นี้เป็นยอดหนี้คงเหลือ · ⚠️ `service.yaml` ค่า `maxScale: 1` + `containerConcurrency: 1` **เป็นกลไกความถูกต้อง ไม่ใช่ tuning** ห้ามแก้
- **09-07 · 📁 ย้าย repo ออกจาก OneDrive → `C:\Repos\` แล้ว (ทุกเครื่อง path เดียวกัน)** — `C:\Repos\RMN-eBidding-Workflow` · `C:\Repos\M4RX-B4SE` · `C:\Repos\RMN-eBidding-KB` · **sync ข้ามเครื่องใช้ `git push/pull` เท่านั้น ห้ามพึ่ง OneDrive** · ⛔ **ห้ามวาง git repo ใน OneDrive/iCloud/Dropbox อีก** — 09-07 พังจริง 3 แบบจากเหตุเดียว: `.lock` ค้างลบไม่ได้ · `.git/objects` ขาด ~60 objects · reflog เสีย ต้อง re-clone ทั้ง repo
- **09-07 · 🛠️ แต่ละ Sir ต้องแก้ path ใน WRK ของตัวเองรอบหน้าที่เปิด session** — DA แก้ให้ไม่ได้ (กฎห้าม commit ไฟล์นอก ownership) · **Sir OPY**: `WRK_OPERATING.md:107,122` · `WRK_FEE_PAYMENT.md:173` · **Sir MM**: `WRK_MAPMAKER.md:46` · **Codex**: `scripts/harvest_all.ps1:2` · `build_taksila_letterhead.py:13` · เดิมเป็น `C:\Users\Advice\OneDrive\...` ซึ่ง **ผูกกับชื่อ user เครื่องเดียว** ใช้กับเครื่องที่ 2 ไม่ได้ → เปลี่ยนเป็น `C:\Repos\...`

## ⚙️ Core Rules
- Diff/changelog only — ห้าม output full file/table
- grep/bash หา section ก่อน — ห้าม Read ทั้งไฟล์
- Edit (diff) เสมอ — Write เฉพาะ full rewrite
- อ่านไฟล์ครั้งเดียว/task — ไม่อ่านซ้ำ verify
- ห้ามเดาข้อมูล — ถามก่อนถ้าไม่ชัด
- bash output → pipe | head -40 เสมอ — ห้าม dump .git/objects
- Auto-update MD @ 90% context → append ## 🔄 Session State → แจ้ง user เริ่ม session ใหม่
- คำนวณ usage ก่อนทุก Edit — ถ้า context ไม่พอ ห้าม Edit แจ้ง user แทน
- 👑 Preview สิทธิ์นายเท่านั้น — แสดง visual preview ทุกครั้งที่แก้ไข UI (ห้าม skip)

## 🔀 Multi-Device Rules (rev.2 — 2026-08-13 ยืนยันจาก iPhone จริง)
- **16.** งานทุกอย่าง **execute บน PC (MARX) เครื่องเดียว** — มือถือเป็นแค่ช่องพิมพ์คำสั่ง ไม่มี state แยก จึงไม่มี split-brain
- **17.** มือถือ = **remote control** → เปิด session เดิมใน **Cowork tab** แล้วพิมพ์ต่อ · **ใช้ได้ครบทุก agent** (bridge ผูกกับ session รอดข้ามการปิด/เปิดแอป)
  - PC offline/หลับ → tool error → **แจ้ง user ว่า execute ไม่ได้ รอ PC ออนไลน์** · **ห้าม fallback ไป clone/GitHub app**
- **18.** git ทั้งหมดรันผ่าน **`Windows-MCP → PowerShell`** (PowerShell จริงบนเครื่อง — มี network + ลบ `.lock` ได้)
  - ⛔ **ห้ามใช้ `device_bash` รัน git** — VM นั้นไม่มี network (403 proxy) และลบ `HEAD.lock`/`index.lock` ไม่ได้ → lock ค้างทุกครั้ง
  - device_bash ใช้ได้เฉพาะ **อ่าน/แก้ไฟล์**
- **19.** ข้อมูลส่วนบุคคล (เลขบัตร ปชช. / เบอร์ส่วนตัว / IP เครื่อง) → repo **private `RMN-eBidding-KB`** เท่านั้น ห้ามลง repo public
  - 📍 ไฟล์ที่ย้ายไป private แล้ว: `WRK_DOC_EXPIRY.md` · `MEMORY_BACKUP_*.md` · `NETWORK_NOTES.md` → หาที่ `RMN-eBidding-KB\` **ไม่ใช่** `WRK_AGENTS\`
- **20.** แก้ KB ที่ต้นฉบับ `M4RX-B4SE\...\E-Bidding\` เสมอ → copy ทับ `KB/` ใน repo ก่อน push

- **21. Restart session → ทำจาก PC เท่านั้น** (ทดสอบแล้ว 2026-08-13)
  - bridge ติดตอน **แนบ folder เข้า Cowork task** ตอนเริ่มงาน · มือถือ Add context **ไม่มีตัวเลือก folder** → task ใหม่จากมือถือ = **ไม่มี bridge** ทำงานไม่ได้
  - ⚠️ context เต็มตอนอยู่นอกบ้าน = คุยต่อไม่ได้จนกลับ PC — **user รับได้ ไม่ต้องเช็ค/เตือนล่วงหน้า** เตือนตอนเต็มจริงเท่านั้น
  - 🛡️ ชดเชยด้วย: **เขียน session state ลง `WRK_<AGENT>.md` (Sir OPY → `WRK_OPERATING_STATE.md`) ระหว่างทาง ทุกครั้งที่งานเสร็จเป็นก้อน ห้ามรอตอนจบ** → เต็มกะทันหันก็ไม่มีอะไรหาย
  - ขั้นตอน: ① เขียน session state → ② commit+push → ③ **สร้าง task ใหม่จาก PC + แนบ folder ตั้งแต่ข้อความแรก** → ④ ตั้งชื่อแชทให้ตรงเดิม → ⑤ **อ่าน `📢 ประกาศ` + KB + WRK** ต่องาน (Sir OPY อ่าน `WRK_OPERATING_STATE.md` เพิ่ม)
- **22. หนึ่งงาน = หนึ่ง agent session** — ห้ามให้ DA ทำงานแทน (KB/WRK/log จะลงผิดที่ + เปลือง context) · DA ทำได้แค่ บอกว่าใช้ agent ตัวไหน · เช็ค read-only · แก้ข้อมูลเก่าข้าม agent · git ให้ทุก agent

> ✅ ปิดเคส sleep: user ไม่ใช้ sleep mode — **PC เปิดตอนตื่น ปิดตอนนอน** → remote จากมือถือใช้ได้ช่วงเช้า–ดึกทุกวัน (ครอบคลุมรอบ 12:01 / 16:01)
> ⚠️ bridge หลุดชั่วคราวได้ตอนเน็ตตก → **กลับมาเอง** ไม่ต้อง restart แค่ลองใหม่
> 📦 workflow เก่า (clone + commit ผ่านแอป GitHub) = **ON HOLD** ไม่ใช้แล้ว — เก็บไว้ที่ `BOOTSTRAP_IOS.md` เผื่อวันหน้า

## 📁 Files & URLs
- Main: `rmn_ebidding_tracker_2.html` (single source of truth)
- Logo: `assets/logo.png`
- Live: https://m4dm4rx.github.io/RMN-eBidding-Workflow/
- Repo: https://github.com/m4dm4rx/RMN-eBidding-Workflow.git

## 🏗️ Backbone
M4RX-B4SE/RMN_Enterprise/E-Bidding/

## 🖥️ Multi-Machine
- **ใช้ PowerShell เป็นหลักเสมอ — ห้ามใช้ CMD**
- PowerShell: ใช้ `$env:USERPROFILE` เสมอ — ห้าม hardcode path
- CMD (ถ้าจำเป็นจริง): ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
- Mounts: `RMN-eBidding-Workflow` / `E-BIDDING` / `Downloads`

## 🔀 Git Push — **Claude push เอง ห้ามรบกวน user** (2026-08-13)
ทุก agent commit+push เองผ่าน **`Windows-MCP → PowerShell`** ไม่ต้องส่งคำสั่งให้ user รัน

```
$r="C:\Repos\RMN-eBidding-Workflow"
Remove-Item "$r\.git\HEAD.lock","$r\.git\index.lock" -Force -ErrorAction SilentlyContinue
git -C $r add <file>
git -C $r commit -m "msg"
git -C $r push
git -C $r rev-parse --short HEAD; git -C $r rev-parse --short origin/main
```
- **ลบ `.lock` ก่อนทุกครั้ง** (lock ค้างบ่อยจาก OneDrive) — PowerShell ลบได้ `device_bash` ลบไม่ได้
- ⛔ **ห้ามใช้ `device_bash` รัน git** — Linux VM ไม่มี network (403 proxy) · ใช้อ่าน/แก้ไฟล์เท่านั้น
- ปิดงานต้องรายงาน `HEAD` = `origin/main` ทุกครั้ง
- PC offline → แจ้ง user "execute ไม่ได้ รอ PC ออนไลน์" · ห้ามส่งคำสั่งให้ user ไปรันเอง

> GitHub Pages deploy จาก branch `main` · push ธรรมดาได้เลย

### ✅ Git Close-out — เกณฑ์ "งานเสร็จ" ของทุก Sir (มติ Lord Commander 2026-09-03)
งานถือว่า **เสร็จและส่งมอบ** เมื่อ owner ทำครบ 3 ข้อ:
1. ตรวจ `git status` **เฉพาะ scope ของตน**
2. commit การเปลี่ยนแปลงของตนให้เรียบร้อย
3. push เมื่อ policy ของงานนั้นกำหนดให้ sync กลาง
- ⛔ **ห้าม commit ไฟล์นอก ownership ของตน** (ดู File Ownership Matrix ใน `KB_ECOSYSTEM_ADMIN.md`)
- ⏸️ งานที่รอ user approval → เขียน **`pending approval`** ใน WRK · **ห้ามเรียกว่างานเสร็จ**
- ใช้กับ **Sir OPY / EXP / MM / UI ทุกคน**

## 🎨 UI Rules
- Light mode default · Viewer URL: `?view=1` (mobile) · Editor: no param (desktop)
- View mode: ซ่อน data-edit-only, theme btn, ปรับ tab labels สั้น
- KPI border-left accent · filter inputs pill-shape · expand btn = text-link

## 📋 STATUS values
รอผลพิจารณา/เป็นผู้เสนอต่ำสุด · ไม่ได้เป็นผู้เสนอต่ำสุด · อนุมัติสั่งจ้าง · จัดทำสัญญา · แพ้การประมูล · แพ้/ขาดคุณสมบัติ · ยกเลิกโครงการ · ห้างขอยกเลิก

## 🤖 Agents
แต่ละ agent มีหน้าที่เดียวเท่านั้น — ห้ามรับงานนอกขอบเขต
| Agent | แก้ได้ | ห้ามแตะ |
|---|---|---|
| MAPMAKER | PDF แผนที่ | อื่นทั้งหมด |
| BIDDING OPERATING | `seed_bids.js` · **`doc_fee_queue.json`** · **`doc_fees.json`** | tracker HTML |
| UI/UX EDITOR | tracker HTML (UI/CSS/layout/logic) | `DOC_FEES` array, fetch URL |
| ~~E-BIDDING DOC FEE~~ | 🚫 **DISABLED 2026-09-02** — ห้าม route งานมา · ไฟล์ `KB_FEE_PAYMENT.md`/`WRK_FEE_PAYMENT.md` เก็บไว้ ห้ามลบ | — |

## 🔄 Doc Fee — กฎบังคับ (procedure เต็ม → `E-Bidding\OPERATING.md`)
⛔ **ห้าม output PDF/Email ก่อน user ยืนยัน Slip Verification**
⛔ **ห้ามอัป `doc_fees.json` ก่อน user แจ้ง "ส่งแล้ว"**
📄 ช่องทางส่งหลักฐาน default = **แนบเข้า e-GP** (อีเมลเฉพาะที่หน่วยงานระบุ)
👤 เจ้าของงาน = **Sir OPY** ผ่าน skill `fee-payment` · OPY ปิด entry เข้า `doc_fees.json` + push เอง
📖 ขั้นตอนเต็ม 7 ขั้น + ตาราง Slip Verification + Email Signature
   → `M4RX-B4SE\RMN_Enterprise\E-Bidding\OPERATING.md` (สำเนา sync: `KB\OPERATING.md`)


## 🔒 Data Separation Rules (CRITICAL)
- **Source of truth คือ `doc_fees.json` เท่านั้น** — ห้าม hardcode data ลงใน tracker HTML
- `const DOC_FEES = [];` ใน tracker HTML ต้องเป็น array เปล่าเสมอ — ห้าม agent ใดเขียนข้อมูลลงไป
- `fetch('https://raw.githubusercontent.com/m4dm4rx/RMN-eBidding-Workflow/main/doc_fees.json')` — ห้าม uiux-editor เปลี่ยน URL นี้
- ถ้า uiux-editor แก้ HTML แล้วเห็น DOC_FEES มีข้อมูล → ลบทิ้ง ใส่ `[]` แทนทันที

## 📦 Archive
- session log ก่อน ก.ค. 69 (3 section) ย้ายไป `WRK_AGENTS/CLAUDE_ARCHIVE_2569H1.md` เมื่อ 2026-09-02 — **ไม่ต้องอ่านตอนเปิด session**
- 📏 เพดานไฟล์นี้ **20 KB** · เกินเมื่อไหร่ให้ย้าย session log เก่าเข้า archive ก่อน **ห้ามยุบ section ที่เป็นกฎ**
