# E-bidding Operating Assistance — OPY

> 📦 ประวัติถึง 2569-08-20 → `WRK_OPERATING_ARCHIVE_2569H2.md`
> เก็บเฉพาะ **กฎที่ใช้จริง + state ปัจจุบัน + pending** · เพดาน 20 KB (DB 2026-08-24)
> ❌ ห้าม hardcode ตาราง seq ที่นี่อีก — `seed_bids.js` = source of truth เสมอ (หา seq ถัดไป: กรอง fiscalYear ล่าสุด → max(seq)+1)

---

## 🎯 Task Scope
รับข้อมูลการประมูล → เพิ่ม/แก้ `seed_bids.js` → widget card + diff → commit + push เอง
อ่าน annoudoc PDF → ตรวจค่าซื้อเอกสาร → append `doc_fee_queue.json` → **ทำ fee-payment เองทั้งเส้นจนปิด `doc_fees.json`**

---

## 🔀 Data Entry Rules
- `pct = round((budget - bid) / budget * 10000) / 100` — double-check ทุกครั้งก่อน commit (เคยพลาด seq167: 47.37 ผิด → 47.36)
- ต่ำสุด → `"รอผลพิจารณา [ เป็นผู้เสนอต่ำที่สุด ]"` · ไม่ต่ำสุด → `"รอผลพิจารณา [ ไม่ได้เป็นผู้เสนอต่ำที่สุด ]"`
- ผลเช้า → 12:01 · ผลบ่าย → 16:01 — **ห้ามถามผลก่อนเวลานี้**
- ⚠️ **seq numbering space แชร์กับ DA (2569-08-27)** — DA backfill ข้อมูลจาก data.go.th เข้ามาในสายเดียวกัน ทำให้ FY2569 max กระโดดจาก 182 → 214 โดยไม่แจ้งล่วงหน้า
  → **ต้อง re-stage `seed_bids.js` แล้วคำนวณ max(seq) ของ fiscalYear ล่าสุดใหม่ทุกครั้งก่อนเพิ่ม record** ห้ามใช้ "SEQ ถัดไป" ที่จำมาจาก session ก่อน
- **`fiscalYear` บังคับทุก record** — คำนวณจาก field `date` (วันประกาศ) เท่านั้น: เดือน ≥ 10 → ปี+1 · เดือน 01–09 → ปี
  ⚠️ **ห้ามคำนวณจากเลข `id`** (id = เดือนที่ขึ้นระบบ e-GP ไม่ตรงวันประกาศจริง 26 records — DA ตรวจพบ 2569-08-13) · schema เต็ม → `KB/OPERATING.md`
- budget = คอลัมน์ "วงเงิน" เสมอ · bid = ตัวเลขท้าย notes (เช่น "เสริมผิว+ผลงาน.(สารคาม79) ขั้น 968,000" → bid 968,000)
- workType = ข้อความก่อน "+" ใน notes (เช่น "เสริมผิว+ผลงาน(...)" → `เสริมผิว`)
- midPrice = ราคากลางจาก PDF ประกาศ (คนละตัวกับ budget — อ่าน PDF ทุกครั้ง ห้ามใช้ budget แทน)

### 🔍 Notes column parsing
- `(สารคามXX)` / `(ศรีบุญเรืองXX)` / `(สกลนครXX)` = ชื่อ plant + เลขอ้างอิงผลงาน (**ไม่ใช่ระยะทาง**) → ใช้ชื่อ plant ตรงนี้เสมอ
- ตัวเลขคอลัมน์สุดท้ายของตาราง (60/75/90) = ระยะเวลาดำเนินการ (วัน) — **ห้ามเอาไปใส่ plantDist**
- `plantDist` ใส่เฉพาะเมื่อ notes ระบุ "XXXกม." ชัดเจน (เช่น seq165 "110กม.") ไม่มี = ปล่อยว่าง ห้ามเดา

### 🏭 Plant ownership
| Plant | ผู้ถือครอง |
|---|---|
| มหาสารคาม | หจก.รักดี การโยธา |
| ศรีบุญเรือง (หนองบัวลำภู) | หจก.อาร์เอ็มเอ็น เอ็นเตอร์ไพส์ |
| สกลนคร | บ.ตักสิลา อาร์เอ็มเอ็น |

entity ยื่น ≠ ผู้ถือครอง → **แจ้งเตือน/detect เฉยๆ ในการ์ด** (โชว์ตาราง plant owner vs entity) — ไม่ต้องออกหนังสือยินยอมจริง, **ห้าม list เป็น pending** (ยืนยันจาก user 2569-08-04)

---

## 📋 Doc Fee Check (ทำทุกครั้งที่อ่านประกาศ)
**โครงสร้างไฟล์ประกาศ (ยืนยัน 2569-08-04):**
- `annoudoc_*.pdf` = ประกาศเชิญชวน — บอกแค่ "ต้องจ่ายไหม / เท่าไร" **ไม่เคยมี**เลขบัญชี/อีเมล
- `doc_*.pdf` = เอกสารประกวดราคา — วิธีชำระอยู่ **ข้อ ๔.๘(๖) มักหน้า 9-10** → ใช้ `pdftotext -f 9 -l 10 <file> -` (ห้าม Read ทั้งไฟล์ เปลือง token) ไม่เจอค่อยขยายช่วง
- user ส่งแค่ table + annoudoc เป็นปกติ — **ขอ `doc_*.pdf` เฉพาะตอน amount > 0** เท่านั้น

**ตัดสิน:** มี "ชำระเงินค่าซื้อเอกสาร ราคาชุดละ X บาท" → ต้องจ่าย · มีแต่ "ดาวน์โหลดผ่าน e-GP" → ไม่ต้องจ่าย

**ทั้งสองกรณีต้อง append `doc_fee_queue.json`** (Read ใหม่ก่อนเสมอ · ห้ามลบ entry เอง):
- ต้องจ่าย → `"status":"pending"`, amount, bank/bankAccNo/email (null ได้ถ้าประกาศไม่ระบุ — ห้ามไปขุดหาที่อื่น), payWindowStart/End, paymentMethod, submitMethod
- ไม่ต้องจ่าย → `"status":"no_fee_required"`, `"amount":0` (ต้อง append ด้วย ไม่งั้นถูก flag เป็นงานค้าง — เคยเกิดกับ SEQ163/164/167/171)
- ก่อน append: grep id ใน `doc_fees.json` ก่อน — ถ้าเจอ = จ่ายแล้ว ห้ามสร้าง pending ซ้ำ (bug จริง 2569-08-04)
- ขัดแย้งกัน → ยึด `doc_fees.json` เป็น source of truth

**pending + amount > 0 → OPY ทำเองทั้งเส้น** (โหลด skill `fee-payment` ในเซสชันนี้ · ⛔ ห้าม dispatch subagent · ⛔ ห้าม web search หา bank/email — ใช้เฉพาะไฟล์ที่แนบ ข้อมูลไม่พอ = บอกว่าขาด):
1. อ่าน queue → แสดง pending · 2. อ่าน entity จาก `seed_bids.js` (local) · 3. รอ user ส่งสลิป
4. **Slip Verification (MANDATORY ห้ามข้าม)** → output ตาราง 6 จุด รอ user ยืนยันก่อนเสมอ:
   ธนาคาร / เลขบัญชี / ชื่อบัญชีผู้รับ / ยอดเงิน / วันที่ (อยู่ใน payWindow) / **ชื่อผู้ฝาก = entity ที่ยื่นงาน**
   └ มี ❌ → หยุด แจ้ง user ทันที · ประกาศไม่ระบุเลขบัญชี = "เทียบไม่ได้" ไม่ใช่ ❌ แต่ต้องบอก
   └ ผู้จ่าย ≠ entity → ถาม "หน่วยงานอาจปฏิเสธ ดำเนินการต่อ?" ห้ามสร้าง PDF เอง
5. user ยืนยัน → สร้าง **PDF ใบแจ้งชำระ** · ช่องทางส่ง default = **แนบ e-GP** (user 2569-09-02 "No email from now on")
   └ Email text + Email Check Box widget → เฉพาะเมื่อหน่วยงาน**ระบุให้ส่งอีเมล**
6. รอ user แจ้ง "ส่งแล้ว" — ⛔ ห้ามอัป `doc_fees.json` ก่อน
7. **OPY เขียน `doc_fees.json` เอง** (paidDate + submitMethod + payerName + ref) → queue `"status":"done"` → push เอง
   ⚠️ `doc_fees.json` format = **1 บรรทัด/entry** ห้าม pretty-print ทั้งไฟล์ (พลาดจริง 2569-09-02 diff โป่ง 467 บรรทัด)
`no_fee_required` → ไม่ต้องทำอะไรต่อ ไม่ต้องเปิด doc_*.pdf

---

## 🏛️ ระเบียบ กวจ. ว.515 (16 ก.ค. 2569)
- จ่ายได้ 2 ทาง: **bank_transfer** (โอนตรงเข้าบัญชีหน่วยงาน) หรือ **bill_payment** (KTB Corporate Online — Company Code + Ref.1 เลขผู้เสียภาษี + Ref.2 เบอร์โทร)
- ส่งหลักฐาน: ไม่ใช่ email เสมอไป — ประกาศส่วนใหญ่ตอนนี้ระบุ "ยื่นหลักฐานพร้อมข้อเสนอผ่านระบบ e-GP" → อ่านทุกครั้งเพื่อตัดสิน `email` / `e-GP` / `both`
- ยังต้องสร้าง PDF ใบแจ้งชำระ (ฝังสลิป) เสมอ แม้แนบเข้า e-GP

---

## ⚖️ DOC agent — DISABLED 2026-09-02 (CLAUDE.md `8c46853`)
scope fee-payment **โอนมาที่ OPY ทั้งหมด** — ห้าม route/dispatch งานไป DOC · ไฟล์ `KB_FEE_PAYMENT.md`/`WRK_FEE_PAYMENT.md` เก็บไว้ ห้ามลบ
เหตุผล: ไม่มีคนเปิด session DOC เลย (WRK แก้ครั้งสุดท้าย 04-08-69) → queue ค้างขั้น "รอ DOC ปิด" ตายเงียบ
สิ่งที่ OPY รับมาเพิ่ม: รับสลิป → ยืนยันเลขบัญชีจากสลิป (**ยึดสลิปเสมอ** เช่น SEQ166 สลิป 404-6-21164-4 vs ประกาศ 406-2-61616-4) → PDF → ส่งตาม submitMethod → ปิด `doc_fees.json` → monitor queue เอง
ยังห้ามแตะ: ไฟล์ skill `*.skill` ทั้งหมด

---

## 🎨 Widget Reporting Rules
ทุก SEQ ใหม่ → render HTML widget การ์ด (คู่กับ diff text เสมอ — **diff = source of truth**, widget = ของอ่านง่าย, diff แสดงทีละบรรทัด ไม่รวมเป็น block เดียว)

องค์ประกอบการ์ด (สะสมทุกส่วน **ห้ามตัดของเดิมทิ้งตอนเพิ่มของใหม่**):
- เลขที่โครงการ **20px / weight 500 / text-primary** + badge `SEQ n` ฟ้า `#B5D4F4` bg / `#0C447C` text
- ชื่อหน่วยงาน **เต็มตามประกาศ** (เช่น "เทศบาลตำบลน้ำพอง" ไม่ใช่ "ทต.น้ำพอง") **17px / weight 500 / text-primary** — ชื่อย่อใส่วงเล็บต่อท้ายได้
- ราคายื่น: กล่อง `#FAC775` + ตัวเลข `#412402` **28px** — ⚠️ hex ตายตัว **ห้ามใช้ `var(--bg-warning)`** (พลิกใน dark mode)
- ตาราง: ประเภทงาน / วงเงิน / ส่วนต่าง / โรงงาน
- กล่องเตือนแดง: ค่าเอกสาร หรือ plant ≠ entity
- input "ผลประมูล (ราคาต่ำสุด)" + ปุ่ม "บันทึกผลประมูล" → `sendPrompt('ผลประมูล\nSEQ n (label) = value\n...')`

**🔒 กฎการ์ดเดียว (ยืนยันจาก user 2569-08-27):** ข้อมูลทั้งหมดของ SEQ นั้นต้องอยู่ใน **การ์ดเดียว** ห้ามแยกการ์ดย่อย/การ์ดที่สอง
ถ้ามีค่าเอกสาร → ฝังกล่องแดงในการ์ดเดิมให้ครบ: ยอดชำระ · ธนาคาร · เลขบัญชี (font-mono 16px) · ชื่อบัญชี · วิธีจ่าย + ช่องทางส่งหลักฐาน · deadline พร้อมคำเตือนถ้าเป็น "ภายในวันและเวลาเสนอราคา" · payer_name ที่รอสลิปตัดสิน · ปุ่ม "คัดลอกเลขบัญชี" + "โอนแล้ว ส่งสลิป"
ยึดหลักเดิม: สะสมทุกส่วน ห้ามตัดของเก่าออกตอนเพิ่มของใหม่

---

## 🚀 Git / Push
- ⛔ **ห้ามรัน git ผ่าน `device_bash` เด็ดขาด** (CLAUDE.md ข้อ 18) — VM ไม่มี network + ลบ `.lock` ไม่ได้ · device_bash = อ่าน/แก้ไฟล์เท่านั้น
- **git ทั้งหมด (add/commit/push) รันผ่าน Windows-MCP PowerShell**:
  ```
  $r="$env:USERPROFILE\OneDrive\Claude\Projects\RMN-eBidding-Workflow"
  Remove-Item "$r\.git\HEAD.lock","$r\.git\index.lock" -Force -ErrorAction SilentlyContinue
  git -C $r add <file>; git -C $r commit -m "msg"; git -C $r push
  git -C $r rev-parse --short HEAD; git -C $r rev-parse --short origin/main
  ```
  ปิดงานต้องรายงาน HEAD = origin/main ทุกครั้ง
  ข้อความสีแดงใน PS = progress output ของ git **ไม่ใช่ error** · ตรวจซ้ำ `git fetch` แล้วเทียบ local vs origin
- ⛔ **ห้าม `git add .` / `git add -A`** — มีไฟล์ agent อื่นค้าง uncommitted (`WRK_MAPMAKER.md`, `PROJECT_INSTRUCTIONS_DRAFT.md`, `SKILL_build.md`, `SKILL_ebidding.md` ฯลฯ) → `git add` เจาะจงชื่อไฟล์เสมอ
- `.git/index.lock` / `HEAD.lock` ค้างบ่อย → sandbox ลบได้หลังเรียก `allow_cowork_file_delete` ครั้งเดียว (สิทธิ์ค้างทั้ง session) ไม่ต้องรบกวน user
- OneDrive sync ระหว่าง sandbox กับเครื่อง user มี delay — commit จาก sandbox อาจยังไม่เห็นทันทีใน PowerShell
- ⛔ **ห้ามใช้ `force:true` ใน device_commit_files เด็ดขาด** (บทเรียน 2569-08-27) — ต้อง **re-stage ก่อน commit ทุกครั้ง** แล้วส่ง `expectedMtimeMs` ที่ได้จาก stage รอบนั้น
  เหตุ: DA push งานเข้า repo ระหว่าง session (`318e98e`, `7d89ec7`) แล้ว OPY เขียนทับด้วยไฟล์เก่า → **ลบ 73 records ของ DA ทิ้ง** (commit `5950a5a`) ต้องกู้ด้วย `git checkout HEAD~1 -- seed_bids.js` (fix `78c8433`)
  ถ้า commit ถูก reject เพราะ mtime drift = **ไฟล์ถูกแก้จริง** → re-stage แล้วรวมงานใหม่ ห้าม force ทับ

### 📂 Working folder / scope
- หลัก: `C:\Users\Advice\OneDrive\Claude\Projects\RMN-eBidding-Workflow`
- แก้ได้: `seed_bids.js` · `doc_fee_queue.json` · **`doc_fees.json` (เขียนได้แล้ว 2026-09-02)** · `WRK_AGENTS\WRK_OPERATING.md`
- อ่านอย่างเดียว: `WRK_OPERATING_ARCHIVE_2569H2.md`
- ห้ามแตะ: `rmn_ebidding_tracker_2.html`, `*.skill` ทั้งหมด, ไฟล์ของ agent อื่น

**📄 ปลายทาง PDF ใบแจ้งชำระค่าเอกสาร (ยืนยันจาก user 2569-08-27) — ห้ามทิ้งไว้ในโฟลเดอร์โปรเจกต์:**
`C:\Users\Advice\OneDrive\[EGP]_E-BIDDING - [R.M.N_GROUP]_DATABASE\Log\ใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคา\`
ชื่อไฟล์: `ใบแจ้งชำระเงินค่าซื้อเอกสาร_<ชื่อหน่วยงานเต็ม>_<id>.pdf` (ชื่อเต็ม ใช้ `_` ไม่ใช่ `.` — ตาม convention ไฟล์เดิมในโฟลเดอร์)
โฟลเดอร์นี้ **ไม่ได้ connect เป็น default** → เรียก `device_request_folder_access` ครั้งเดียวต่อ session
⚠️ skill `fee-payment` ยังชี้ path เก่า (E-BIDDING/Log fallback Downloads) — **OPY แก้ skill เองไม่ได้** · workaround: สร้าง PDF ในคอนเทนเนอร์ → `SendUserFile` → `device_commit_files` ไป Log folder ด้วยมือ

---

> ประวัติ session ก่อน 2569-08-28 → `WRK_OPERATING_ARCHIVE_2569H2.md` + git log · ชื่อเรียก agent = **"OPY"**

## 🔄 Session State (2569-09-02)
- **Last SEQ (FY2569) = 219** · `seed_bids.js` **636 records** · HEAD = origin `5cf6c8f`
- 218 `69069406325` ทต.หนองกุง (กส.) ยื่น 1,818,000 / วงเงิน 3,498,000 / pct 48.03 / มหาสารคาม → **✅ ต่ำสุด** · ไม่มีค่าเอกสาร
- 219 `68099553809` อบจ.บึงกาฬ ยื่น 6,865,000 / วงเงิน 6,870,000 / pct 0.07 / สกลนคร · entity **ห้างหุ้นส่วน RMN** (plant = ตักสิลา ⚠ แจ้งเตือน) → **❌ −133,000** (ต่ำสุด 6,732,000)
- ค่าเอกสาร `68099553809` **5,000฿** KTB 447-0-29255-9 ฝากเงินสด 02/09/2569 · แนบ e-GP · ปิดเข้า `doc_fees.json` (35 entries) · queue **pending 0**
- 🆕 กฎที่รับมารอบนี้ (CLAUDE.md `8c46853`): DOC disabled → OPY ทำ fee ทั้งเส้น · Slip Verification บังคับ · git ผ่าน PowerShell เท่านั้น · doc_fees.json เขียนได้
- ⚠️ บทเรียน: id ขึ้นต้น 68 แต่ fiscalYear 2569 ได้ (คิดจาก `date` เท่านั้น) · user แก้ entity กลางทางได้ ยึดครั้งล่าสุด
- 📌 พบแต่ไม่แก้ (นอกขอบเขต): FY2569 มี 33 records `pct` ไม่ตรงสูตร ทั้งหมด seq ≤ 158 = backfill ของ DA

## ⏳ Pending
- **ไม่มี pending งานจริง** — ผลครบ · queue pending 0 · push ครบ
- ไม่เร่ง: skill `fee-payment` ยังชี้ path ปลายทาง PDF ผิด (ต้องเป็น Log folder) — OPY แก้ `*.skill` เองไม่ได้ ต้องให้ user/DA แก้

> 📜 state 2569-08-28 (seq 182/215/216/217 · queue 15 pending 0 · commit `e418c7c`) → ดู `git log` + `WRK_OPERATING_ARCHIVE_2569H2.md`
> ⚠️ บทเรียนที่ยังใช้: SEQ217 วงเงินในตาราง user พิมพ์ผิด 50,000 จริง 500,000 — ตัวเลขไม่สมเหตุผล = ถาม ห้ามเดา
