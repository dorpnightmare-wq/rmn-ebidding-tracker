# 📦 CLAUDE.md — Archive 2569 H1 (session log ที่ย้ายออก 2026-09-02)

> ต้นฉบับ: `WRK_AGENTS/CLAUDE.md` · ย้ายออกเพราะไฟล์แม่เกินเพดาน 20 KB
> **ไม่มีเนื้อหาข้อไหนถูกลบ** — ย้ายทั้งก้อน 3 section ตามเดิม · **ไม่ต้องอ่านตอนเปิด session**
> กฎที่ยังใช้จริงอยู่ในไฟล์แม่ทั้งหมด ที่นี่คือ session log ประวัติเท่านั้น

---

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

## 📢 ประกาศที่ย้ายมาเก็บ (09-01 / 09-02 — เกิน 30 วันหรือถูกมติใหม่แทนแล้ว)

- **09-01 · DB (Design Board) ปลดแล้ว** — ไม่ใช่ agent/session · `RMN_Enterprise\DESIGN_PRINCIPLES.md` = **เอกสารหลักการ + Decision log เจ้าของ DA** · **ห้ามรอ DB ตัดสินใจ** เรื่องไฟล์ของตัวเอง ตัดสินเองได้เลย
- **09-02 · DOC (Fee Payment) ปลดแล้ว** — ค่าเอกสารทั้งเส้นอยู่ใต้ **OPY** · OPY เขียน `doc_fees.json` + push ได้เอง · **ห้าม route/dispatch ไป DOC**
- **09-02 · ชั้นยศ + File Ownership Matrix** — `Codex = Lord Commander` (เจ้าของ scripts/infra) · Claude = executor ของไฟล์ตาม domain · **ตารางเจ้าของไฟล์อยู่ใน `KB_ECOSYSTEM_ADMIN.md`** — ไฟล์ที่ไม่อยู่ในตาราง = ถามก่อนแก้
- **09-02 · Skills Governance** — `agent propose → DA review/apply → บันทึก changelog` · agent ห้าม propose skill ของ agent อื่น
- **09-03 · 📖 procedure Doc Fee/Slip/Email ย้ายไป `E-Bidding\OPERATING.md`** (เจ้าของ Sir OPY · สำเนา sync `KB\OPERATING.md`) — `CLAUDE.md` เหลือ **safety gate + pointer** · ห้ามขยายเพดาน 20 KB ให้แยกเนื้อหาเฉพาะทางออกแทน
- **09-03 · `build_taksila_letterhead.py` + `tmp/` = Lord Commander** (provisional/untracked) — Claude อ่าน/รันได้ **แก้ไม่ได้**
- **09-03 · 🐦 Raven Mail = รูปแบบส่งข้อความข้ามฝั่ง** — ส่งถึง Lord COMMANDER of GPT / Codex / ข้าม agent ต้องขึ้นหัว `🐦 Raven Mail` + `จาก:` + `ถึง:` + `เรื่อง:` · **ชื่อผู้ส่งต้องตรงตัวจริง ห้ามสลับ** (รายชื่อเต็มใน `KB_ECOSYSTEM_ADMIN.md § 🐦`)
