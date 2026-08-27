# E-bidding Operating Assistance — OPY

> 📦 **ประวัติเต็มถึง 2569-08-20 ย้ายไปที่ `WRK_AGENTS/WRK_OPERATING_ARCHIVE_2569H2.md`** (ตาราง seq 94–174, Done This Session, Session State 2569-07-24 / 07-27 / 08-04 x2, prompt เก่า)
> ไฟล์นี้เก็บเฉพาะ **กฎที่ยังใช้จริง + state ปัจจุบัน + pending** ตามกฎเพดาน 20 KB (DB ตั้งไว้ 2026-08-24)
> ❌ ห้าม hardcode ตาราง seq ที่นี่อีก — `seed_bids.js` = source of truth เสมอ (หา seq ถัดไป: กรอง fiscalYear ล่าสุด → max(seq)+1)

---

## 🎯 Task Scope
รับข้อมูลการประมูล → เพิ่ม/แก้ `seed_bids.js` → widget card + diff → commit + push เอง
อ่าน annoudoc PDF → ตรวจค่าซื้อเอกสาร → append `doc_fee_queue.json` → dispatch fee-payment ถ้าต้องจ่าย

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

**ทั้งสองกรณีต้อง append `doc_fee_queue.json`** (Read ใหม่ก่อนเสมอ — Doc Fee Agent แก้ไฟล์นี้นอก session · append/read เท่านั้น ห้ามลบ entry เอง):
- ต้องจ่าย → `"status":"pending"`, amount, bank/bankAccNo/email (null ได้ถ้าประกาศไม่ระบุ — ห้ามไปขุดหาที่อื่น), payWindowStart/End, paymentMethod, submitMethod
- ไม่ต้องจ่าย → `"status":"no_fee_required"`, `"amount":0` (ต้อง append ด้วย ไม่งั้น Doc Fee Agent flag เป็นงานค้าง — เคยเกิดกับ SEQ163/164/167/171)
- ก่อน append: grep id ใน `doc_fees.json` ก่อน — ถ้าเจอ = จ่ายแล้ว ห้ามสร้าง pending ซ้ำ (bug จริง 2569-08-04)
- ขัดแย้งกัน → ยึด `doc_fees.json` เป็น source of truth

**ถ้า pending + amount > 0 → dispatch Agent tool (subagent_type: general-purpose) ทันที** โหลด skill `fee-payment` ประมวลผลในเซสชันเดียวกัน ส่ง id/agency/amount/bank/email/deadline/paymentMethod/submitMethod ไปให้ครบ
⛔ **ห้าม subagent web search / fetch เว็บหน่วยงานเด็ดขาด** — ใช้เฉพาะไฟล์ที่แนบมา · ข้อมูลไม่พอ = รายงานว่าขาด ห้ามเดา
`no_fee_required` → ไม่ต้อง dispatch, ไม่ต้องเปิด doc_*.pdf เลย

**ข้อจำกัด dispatch:** subagent รันครั้งเดียวจบ รอสลิปไม่ได้ · ทำแค่ first-pass ไม่ monitor ต่อ

---

## 🏛️ ระเบียบ กวจ. ว.515 (16 ก.ค. 2569)
- จ่ายได้ 2 ทาง: **bank_transfer** (โอนตรงเข้าบัญชีหน่วยงาน) หรือ **bill_payment** (KTB Corporate Online — Company Code + Ref.1 เลขผู้เสียภาษี + Ref.2 เบอร์โทร)
- ส่งหลักฐาน: ไม่ใช่ email เสมอไป — ประกาศส่วนใหญ่ตอนนี้ระบุ "ยื่นหลักฐานพร้อมข้อเสนอผ่านระบบ e-GP" → อ่านทุกครั้งเพื่อตัดสิน `email` / `e-GP` / `both`
- ยังต้องสร้าง PDF ใบแจ้งชำระ (ฝังสลิป) เสมอ แม้แนบเข้า e-GP

---

## ⚖️ แบ่งงาน OPY (ที่นี่) vs Doc Fee Agent
**OPY ผ่าน dispatch:** เจอ fee ตอนเพิ่ม SEQ → append queue + เรียก subagent ทันที · ใช้เฉพาะไฟล์ที่มี · ข้อมูลไม่พอ = mark ว่าขาด · จบที่ first-pass เดียว
**Doc Fee Agent (dispatch ทำแทนไม่ได้):**
1. รับสลิปจริง → ยืนยันเลขบัญชีจากสลิป (บางครั้งต่างจากประกาศ เช่น SEQ166 สลิป 404-6-21164-4 vs ประกาศ 406-2-61616-4 — **ยึดสลิป**) → PDF สุดท้าย + ส่งตาม submitMethod
2. Monitor queue แบบ recurring (เคส pending ค้างนาน)
3. ดูแลไฟล์ skill `fee-payment` / `e-bidding-operating` — **OPY ห้ามแตะ**
4. Correction ที่ต้องคุยกับ user หลายรอบ

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
- **OPY push เองได้** ผ่าน Windows-MCP PowerShell (sandbox bash ไม่มี credential):
  `cd C:\Users\Advice\OneDrive\Claude\Projects\RMN-eBidding-Workflow; git push origin main`
  ข้อความสีแดงใน PS = progress output ของ git **ไม่ใช่ error** · ตรวจซ้ำ `git fetch` แล้วเทียบ local vs origin
- ⛔ **ห้าม `git add .` / `git add -A`** — มีไฟล์ agent อื่นค้าง uncommitted (`WRK_MAPMAKER.md`, `PROJECT_INSTRUCTIONS_DRAFT.md`, `SKILL_build.md`, `SKILL_ebidding.md` ฯลฯ) → `git add` เจาะจงชื่อไฟล์เสมอ
- `.git/index.lock` / `HEAD.lock` ค้างบ่อย → sandbox ลบได้หลังเรียก `allow_cowork_file_delete` ครั้งเดียว (สิทธิ์ค้างทั้ง session) ไม่ต้องรบกวน user
- OneDrive sync ระหว่าง sandbox กับเครื่อง user มี delay — commit จาก sandbox อาจยังไม่เห็นทันทีใน PowerShell
- ⛔ **ห้ามใช้ `force:true` ใน device_commit_files เด็ดขาด** (บทเรียน 2569-08-27) — ต้อง **re-stage ก่อน commit ทุกครั้ง** แล้วส่ง `expectedMtimeMs` ที่ได้จาก stage รอบนั้น
  เหตุ: DA push งานเข้า repo ระหว่าง session (`318e98e`, `7d89ec7`) แล้ว OPY เขียนทับด้วยไฟล์เก่า → **ลบ 73 records ของ DA ทิ้ง** (commit `5950a5a`) ต้องกู้ด้วย `git checkout HEAD~1 -- seed_bids.js` (fix `78c8433`)
  ถ้า commit ถูก reject เพราะ mtime drift = **ไฟล์ถูกแก้จริง** → re-stage แล้วรวมงานใหม่ ห้าม force ทับ

### 📂 Working folder / scope
- หลัก: `C:\Users\Advice\OneDrive\Claude\Projects\RMN-eBidding-Workflow`
- แก้ได้: `seed_bids.js` · `doc_fee_queue.json` (append/read) · `WRK_AGENTS\WRK_OPERATING.md`
- อ่านอย่างเดียว: `doc_fees.json` · `WRK_OPERATING_ARCHIVE_2569H2.md`
- ห้ามแตะ: `rmn_ebidding_tracker_2.html`, `*.skill` ทั้งหมด, ไฟล์ของ agent อื่น

---

## 🔄 Session State (2569-08-20) — ปิด session, verified
- **Last SEQ = 181** · seed_bids.js **557 records** · commit `a904823` **push แล้ว** (local = origin ยืนยันด้วย git fetch)

| seq | id | หน่วยงาน | ยื่น | ต่ำสุด | ผล | plant |
|-----|----|---------|------|--------|-----|-------|
| 175 | 69079488448 | อบต.วังแสง (มค.) | 288,000 | 288,000 | ✅ | มหาสารคาม |
| 176 | 69059509007 | อบต.ใหม่นาเพียง (ขก.) | 1,058,000 | 1,044,000 | ❌ −14,000 | มหาสารคาม |
| 177 | 69079054553 | อบต.หมูม่น (กส.) | 638,000 | 602,270 | ❌ −35,730 | มหาสารคาม |
| 178 | 69069589057 | ทต.โนนสูงเปลือย (นภ.) | 1,118,000 | 1,118,000 | ✅ | ศรีบุญเรือง ⚠ |
| 179 | 69089150896 | ทต.สุวรรณคูหา (นภ.) | 466,000 | 466,000 | ✅ | ศรีบุญเรือง ⚠ |
| 180 | 69079253957 | ทต.เขื่อนอุบลรัตน์ (ขก.) | 1,198,000 | 1,198,000 | ✅ | ศรีบุญเรือง ⚠ |
| 181 | 69089123180 | ทต.โคกสูงสัมพันธ์ (ขก.) | 528,000 | 508,800 | ❌ −19,200 | ศรีบุญเรือง ⚠ |

- ค่าเอกสาร: ทั้ง 7 โครงการ **ไม่มีค่าเอกสาร** → append `no_fee_required` ครบใน `doc_fee_queue.json` (13 entries, **pending = 0**)
- ✅ บั๊กเก่าเคลียร์แล้ว: entry SEQ174 (`69079461100`) ที่เคยค้าง pending ถูก Doc Fee Agent ลบออกจาก queue เรียบร้อย
- Recheck อัตโนมัติก่อนปิด session: pct ถูกทั้ง 7 · fiscalYear ตรงกฎ date ทุกตัว · ไม่มี seq/id ซ้ำในสาย 94–181 · status ↔ lowest สอดคล้องกัน — **ไม่พบ error**
- ชื่อเรียก agent = **"OPY"** (แจ้งโดย DP 2569-08-20)

## 🔄 Session State (2569-08-27) — ล่าสุด
- **Last SEQ (FY2569) = 215** · seed_bids.js **632 records** · commit ล่าสุด `0244c50` push แล้ว (local = origin verified)
- SEQ ที่เพิ่มรอบนี้:

| seq | id | หน่วยงาน | ยื่น | วงเงิน | pct | plant | ผล |
|-----|----|---------|------|--------|-----|-------|-----|
| 182 | 69079170169 | อบต.ดงมะไฟ (สน.) | 1,348,000 | 2,074,000 | 35.00 | สกลนคร ⚠ | ✅ ต่ำสุด |
| 215 | 69029099286 | ทต.เมืองเก่า (ขก.) | 888,000 | 1,492,000 | 40.48 | มหาสารคาม | ⏳ รอผล 27 ส.ค. 12:01 |

- **doc fee ค้าง 1 รายการ**: `69029099286` 1,000฿ · KTB **405-6-06787-2** ชื่อบัญชี เทศบาลตำบลเมืองเก่า · bank_transfer · ส่งหลักฐาน **e-GP เท่านั้น** · deadline **ภายในวันและเวลาเสนอราคา 27 ส.ค.69 ก่อน 12:00** (เส้นตายเดียวกับยื่นซอง)
  - dispatch fee-payment รอบแรกแล้ว → queue field ครบ, รอสลิปจริงจาก user เพื่อสร้าง PDF ใบแจ้งชำระ + ตัดสิน payer_name
- doc_fee_queue.json = 15 entries (pending 1)
- 🩹 **Incident 2569-08-27**: force-commit ทับงาน DA (ดูกฎใหม่ในหมวด Git/Push) — กู้ครบแล้ว ไม่มีข้อมูลหาย
- 🆕 กฎใหม่ที่บันทึกรอบนี้: (1) การ์ดเดียวรวมทุกอย่าง (2) ห้าม force commit ต้อง re-stage (3) seq space แชร์กับ DA ต้องคำนวณใหม่ทุกครั้ง

## ⏳ Pending
- **doc fee `69029099286` 1,000฿** — รอ user โอน + ส่งสลิป → dispatch fee-payment รอบสองสร้าง PDF (deadline 27 ส.ค.69 12:00)
- ผลประมูล SEQ 215 — ถามได้หลัง 12:01 น. 27 ส.ค.69
