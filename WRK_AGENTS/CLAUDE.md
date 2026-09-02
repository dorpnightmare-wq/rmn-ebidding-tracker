# RMN e-Bidding Tracker

## 🚫 NEVER USE (no exceptions)
TaskCreate · TaskUpdate · TaskList · TaskStop · TaskGet · AskUserQuestion · mcp__visualize__read_me

## 📌 Session Policy (STRICT)
- **ห้าม compact session เอง** — ถ้า context ใกล้หมด → แจ้ง "กรุณา Restart session" แทน
- เหตุผล: context ก่อน compact จะหายไปทั้งหมด ทำให้งานค้างเสียหาย
- **Email Check Box ต้องเป็น interactive widget** (mcp__visualize__show_widget) — ไม่ใช่ markdown ☐
ToolSearch → โหลดเฉพาะเมื่อ tool ไม่มีใน schema จริงๆ

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
  - 🛡️ ชดเชยด้วย: **เขียน session state ลง `WRK_<AGENT>.md` ระหว่างทาง ทุกครั้งที่งานเสร็จเป็นก้อน ห้ามรอตอนจบ** → เต็มกะทันหันก็ไม่มีอะไรหาย
  - ขั้นตอน: ① เขียน session state ลง `WRK_<AGENT>.md` → ② commit+push → ③ **สร้าง task ใหม่จาก PC + แนบ folder ตั้งแต่ข้อความแรก** → ④ ตั้งชื่อแชทให้ตรงเดิม → ⑤ อ่าน KB+WRK ต่องาน
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
- CMD: ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
- Mounts: `RMN-eBidding-Workflow` / `E-BIDDING` / `Downloads`

## 🔀 Git Push — **Claude push เอง ห้ามรบกวน user** (2026-08-13)
ทุก agent commit+push เองผ่าน **`Windows-MCP → PowerShell`** ไม่ต้องส่งคำสั่งให้ user รัน

```
$r="$env:USERPROFILE\OneDrive\Claude\Projects\RMN-eBidding-Workflow"
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

## 🔒 Data Separation Rules (CRITICAL)
- **Source of truth คือ `doc_fees.json` เท่านั้น** — ห้าม hardcode data ลงใน tracker HTML
- `const DOC_FEES = [];` ใน tracker HTML ต้องเป็น array เปล่าเสมอ — ห้าม agent ใดเขียนข้อมูลลงไป
- `fetch('https://raw.githubusercontent.com/m4dm4rx/RMN-eBidding-Workflow/main/doc_fees.json')` — ห้าม uiux-editor เปลี่ยน URL นี้
- ถ้า uiux-editor แก้ HTML แล้วเห็น DOC_FEES มีข้อมูล → ลบทิ้ง ใส่ `[]` แทนทันที

## 🔄 Session State (2026-06-16)
### ✅ Done (UI/UX Agent — session นี้)
- Restore saveBid/editBid/deleteBid ที่หายไปตอน API cleanup ✅
- Dashboard แสดงทุกปีงบ (Store.getAll) ✅
- ซ่อน year-tabs บน Dashboard tab ✅
- ลบ label "ปีงบประมาณ 2569" ออกจาก header/subtitle ✅
- Growth chart (dual-axis bar) layout 2×2 + Chart.js CDN ✅
- SME rewrite → จำนวนโครงการต่อห้าง แทน 300M tracker ✅
- ลบ card % ลดราคาเฉลี่ย (NaN bug) ✅
- Province chart ซ่อน ? (records ไม่มี province) ✅
- Normalize entity names ใน seed_bids.js ✅
  - "ห้างหุ้นส่วน" → "ห้างหุ้นส่วน RMN" (208 records)
  - "กิจการร่วมค้า" + "ร่วมค้า RMN" → "กิจการร่วมค้า RMN" (23)
  - "ร่วมค้า รักดี" → "กิจการร่วมค้า รักดี" (7)

### 📦 Entity Structure (confirmed)
| Entity | บทบาท | Records |
|---|---|---|
| ห้างหุ้นส่วน RMN | ห้างหลัก | 322 |
| กิจการร่วมค้า RMN | ร่วมค้ากับ รุ่งเรืองชัยฯ (เลิกใช้) | 23 |
| กิจการร่วมค้า รักดี | ร่วมค้ากับ รักดี การโยธา | 7 |
| กิจการร่วมค้า ตักสิลา | ร่วมค้ากับ ตักสิลา อาร์เอ็มเอ็น | 4 |

### ⚠️ รู้จัก — ยังไม่ลง
- กิจการร่วมค้า ตักสิลา มี 11 records ปี 2568 จากระบบเก่า (ยังไม่มีราคา)
- HEAD.lock / index.lock ค้างบ่อย → user ต้อง del ก่อน push ทุกครั้ง

### ⏳ Pending (Tracker)
- รอผล seq 99-100 → อัปเดต status + midPrice
- light mode toggle (dev agent)
- FIX 7 phase 2: one-off structural styles (dev agent)

### ⏳ Pending (Map Maker)
- ทต_แวงน่าง / อบต_ยางใหญ่ → ทำใหม่ session ใหม่
- ทม_สกลนคร (52.3 กม.) → ทำใหม่ session ใหม่
- อบต_ทรายมูล (62.9 กม.) → ทำใหม่ session ใหม่

## 🔄 Session State (2026-06-25)
### ✅ Done (session นี้)
- Modal popup: click project ID → popup รายละเอียด (pipeCard + projectCard) ✅
- Fix JS syntax error (backtick escape จาก Python heredoc) ✅
- Fix paid flag bug (reg truthy → ขึ้น จ่ายแล้ว ผิด) ✅
- pipeCard header redesign: ID+Agency+Status badge row + "ดูรายละเอียด ▶" ✅
- B+D contrast: badge row bg + project name left accent bar ✅
- Tab ค่าเอกสาร (renderDocFeeTab): ตาราง + paid/email toggle ✅
- Dashboard section ค่าเอกสาร (renderDashDocFee): รอจ่าย/รอส่ง email เท่านั้น ✅
- ลบ SME tab → ย้ายเป็น card ใน Dashboard ✅
- Viewer dark/light toggle switch (#view-theme-toggle) ✅
- Dashboard docfee: ลบ เรียบร้อย section, แสดงเฉพาะ pending ✅
- paid badge: clickable → toggleDocFeePaid() (true/false/null cycle) ✅
- Tab ค่าเอกสาร: col ช่วงเวลาการชำระเงิน, swap วิธีจ่าย→emailTo ✅
- fmtThaiDate(): "2569-06-25" → "25/มิ.ย./2569" ✅
- Tab ค่าเอกสาร: ลบ ฿, ซ่อน year-tabs, sort ใหม่สุดบน ✅
- SME card: วงเงินสะสม vs 300M limit (🟢<80% 🟡≥80% 🔴≥100%) ✅
- ลบ KPI card "ค่าเอกสารประมูลรวม" (ซ้ำกับ section renderDashDocFee) ✅

### 📋 doc_fees.json schema ใหม่ (Doc Fee Agent ต้องเพิ่ม)
| field | ความหมาย |
|---|---|
| feeStartDate | วันเริ่มจ่ายค่าเอกสาร (YYYY-MM-DD) |
| feeEndDate | วันสิ้นสุดจ่ายค่าเอกสาร (YYYY-MM-DD) |
| emailTo | email หน่วยงานที่ส่งหลักฐาน |

### ⏳ Pending
- topbar + tabs: เปลี่ยน bg จาก backdrop-filter blur → solid (ให้เหมือน section row 3)
- light mode toggle full implementation (dev agent)
- FIX 7 phase 2: one-off structural styles (dev agent)
- Map Maker: ทต_แวงน่าง / อบต_ยางใหญ่ / ทม_สกลนคร / อบต_ทรายมูล

## 🔄 Session State (2026-06-25 — E-Bidding Operating Agent)
### ✅ Done (session นี้)
- seq 127 อบต.เมืองเสือ มค. bid 796,000 ✅ ต่ำสุด
- seq 128 ทต.ปาฝา รอ. bid 598,000 ✅ ต่ำสุด
- seq 129 ทต.ศรีโคตร รอ. bid 568,000 ✅ ต่ำสุด
- seq 130 อบต.ม่วงลาย สน. bid 1,078,000 ✅ ต่ำสุด
- seq 131 อบต.หนองบัว หบ. bid 758,000 ✅ ต่ำสุด
- seq 132 อบต.โนนข่า ขก. bid 4,898,000 ❌ ไม่ต่ำสุด (-53,000) lowest 4,845,000
- seq 133 รพ.สุวรรณคูหา หบ. bid 1,558,000 ✅ ต่ำสุด
- seq 134 ทต.โคกพระ มค. bid 378,000 ✅ ต่ำสุด
- seq 135 ทต.ธัญญา กส. bid 598,000 ✅ ต่ำสุด
- seq 136 อบต.ปางกู่ หบ. bid 1,748,000 ✅ ต่ำสุด
- Lock format: SEQ summary line + 5-col table (เลขที่/หน่วยงาน/ที่ตั้งหน่วยงาน/ราคายื่น/Plant)

### 📋 Rules confirmed this session
- plantDist = เลขในวงเล็บ (เช่น "(สารคาม55)") — ไม่ใช่คอลัมน์ขวาสุด
- ชื่อหน่วยงาน: ถ้า PDF ≠ ตาราง → ใช้ PDF เสมอ (เช่น โนนข่า ≠ โนนซ่า, ปาฝา ≠ ปาฬา)
- ม่วงลาย วันยื่น 24 มิ.ย. (ตารางผิด บอก 22)

### ⏳ Pending
- (none)
push `doc_fees.json` / `doc_fee_queue.json` — **OPY push เอง** (2026-09-02)

## 🖥️ Multi-Machine
+ - ใช้ PowerShell เป็นหลักเสมอ — ห้ามใช้ CMD
- CMD: ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
+ - PowerShell: ใช้ `$env:USERPROFILE` เสมอ — ห้าม hardcode path
