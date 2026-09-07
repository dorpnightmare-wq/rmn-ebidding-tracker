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

## 🔄 Session State (2026-09-05 — DA: ไฟล์สัญญาจากฝ่ายบัญชี + ปิดเคส PII)

### 📥 แหล่งข้อมูลใหม่ — ไฟล์สัญญา งบ69 จากฝ่ายบัญชี (Top)
`สัญญางาน งบ69.xlsx` (67.66 kB) รับทาง LINE 2569-09-05 · **7 sheet · 172 สัญญา · 538,305,862 บาท** · ครอบคลุมถึง **1 ก.ย. 69**
| sheet | n | รวม (incl VAT) |
|---|---:|---:|
| RMN | 107 | 219,138,939 |
| กิจการร่วมค้า ตักสิลา | 19 | 175,571,000 |
| หจก.รักดี | 23 | 10,389,000 |
| กิจการร่วมค้า RMN | 11 | 95,142,000 |
| RMN ยกเลิก ❌ | 7 | 7,248,423 |
| กิจการร่วมค้า รักดี | 3 | 29,928,000 |
| บจ.ตักสิลา 🆕 | 2 | 888,500 |

**ท่อข้อมูลนี้ทำงานเองแล้ว** — user สั่ง Top ว่า *"ถ้าเพิ่มใหม่ครั้งต่อไปให้ top แค๊ปแบบนี้ส่งให้พี่ด้วยนะ"* · Top ยืนยัน *"ผมจะทำไว้แบบนี้"* → เข้ากฎข้อ 10-11 (ใช้ของที่คนทำอยู่แล้ว)

### 🔎 ผลแมตช์เข้า seed_bids (84 record ที่ยังไม่ปิด)
| | n | หมายเหตุ |
|---|---:|---|
| ✅ ปิดได้ (ราคาตรง + ชื่อหน่วยงานตรงเป๊ะ) | **35** | 33,053,000 บาท · มีเลขที่สัญญา + วันทำสัญญาครบ |
| ❌ ติดธงยกเลิก | 2 | seq 22 · 23 ทต.นาจาน (E4/E5 2569) |
| ⚠️ ต้องตรวจมือ | 1 | seq 57 — `เทศบาลเมืองกระนวน หมู่ที่ 11` vs `เทศบาลเมืองกระนวน` |
| ⏳ ยังไม่เซ็นสัญญา | 46 | **สถานะ `รอผลพิจารณา` เดิมถูกต้องแล้ว ไม่ต้องแก้** |

**46 ตัวไม่ใช่ข้อมูลขาด** — capture สรุปของบัญชีแยกคอลัมน์ `รอเซ็นสัญญา` ไว้: RMN 120,335,000 · กิจการร่วมค้า RMN 25,848,000 · หจก.รักดี 10,389,000 · บจ.ตักสิลา 888,500

### 🔴 บทเรียน — ผมเจอ false match ของตัวเอง 1 ตัว
`seq 175 อบต.วังแสง 288,000` ถูกผมแมตช์ให้สัญญา `E01/2569 ของ ทต.หนองกุงธนสาร` = **คนละหน่วยงาน**
สาเหตุ: เทียบชื่อหน่วยงานแบบ token overlap 12 ตัวอักษร → หลวมเกิน · เจอเพราะพิมพ์ชื่อ 2 ฝั่งวางข้างกันดู **ไม่ใช่เพราะระบบเตือน**
แก้: ตัด prefix (`องค์การบริหารส่วนตำบล/เทศบาลตำบล/แขวงทางหลวง/อบต./ทต./ขทช.`) แล้วบังคับส่วนที่เหลือ **ตรงเป๊ะ** → 48 เหลือ 35
> **ราคาซ้ำข้ามปีมีจริง:** 1,188,000 ตรง 4 record (seq 11·20·52·67) · 288,000 ตรง 2 · 1,688,000 ตรง 2

### ⚠️ ยอดไม่ตรงกับ capture ของบัญชี — ยังไม่สรุป ต้องถาม Top
```
                      capture "เซ็นแล้ว"     ผมรวมจาก xlsx        ต่าง
RMN                   106,228,801.38      204,802,746.73   +98,573,945
กิจการร่วมค้า ตักสิลา   153,280,629.86      164,085,046.73   +10,804,417
กิจการร่วมค้า RMN       64,306,000.00       88,917,757.01   +24,611,757
กิจการร่วมค้า รักดี      19,504,672.89       27,970,093.46    +8,465,421   (ก่อน VAT)
```
ผมสูงกว่าทุกก้อน · **sheet รายละเอียดไม่มีคอลัมน์บอกว่าตัวไหนเซ็นแล้ว** และใช้ `วันที่ทำสัญญา` แทนไม่ได้ (171/172 แถวมีวันครบ · ขาด 4 แถวใน sheet RMN · 2 แถวไม่มีเลขสัญญาเลย: ทต.นาซอ 998,000 · ทต.แกดำ 578,000)
→ **คำถามถึง Top:** sheet รายละเอียดรวมตัวที่รอเซ็นสัญญาไว้ด้วยหรือเปล่า ถ้ารวม ดูจากคอลัมน์ไหน

### ✅ ปิดเคส PII (มติ user 2026-09-05)
`087-223-5093` + ชื่อหุ้นส่วนผู้จัดการ = **เบอร์ธุรกิจ** → อยู่ใน repo public ได้ · ไม่ต้อง mask ไม่ต้องย้าย · **ปิดข้อขัดกัน Rule 19 vs 20** · ยกเลิกคำสั่งหยุดที่ผมสั่ง Sir OPY ไว้
⛔ ข้อยกเว้นจำกัดเฉพาะรายการนี้ — เลขบัตร ปชช./เบอร์ส่วนตัวพนักงาน/เงินเดือน ยังอยู่ใต้ Rule 19 เต็ม

### 🧹 กันออกจากงานประมูล
`เฉพาะเจาะจง` 8 สัญญา 2,665,500 บาท (บจ.ตักสิลา 2 + อื่น 6) — ชื่อโครงการระบุ *"โดยวิธีเฉพาะเจาะจง"* → ไม่เข้า seed_bids · **บจ.ตักสิลา ไม่ต้องเพิ่มเป็น entity ที่ 6**

### ⏸️ pending approval
1. **ที่วางไฟล์ handoff 2 ตัว** — `_handoff_OPY_close_2569-09-05.csv` (35+2+1 พร้อม `agency_seed` vs `agency_acct` + note ที่มา) · `สัญญา_งบ69_จากฝ่ายบัญชี_2569-09-05.csv` (172 แถว อ่านออกไม่ต้องเปิด xlsx) → รอ user เลือก repo root / `[EGP]...DATABASE\Log\` / แชทเฉยๆ
2. **xlsx ต้นฉบับ** เก็บเข้า `[EGP]...DATABASE` ไหม
3. **Strict Rule R1-R3** เสนอ Lord Commander แล้ว รอรับรอง (R1 join key · R2 เฉพาะเจาะจง · R3 สถานะยกเลิก 2 คำ)
4. **35 record** ยังไม่ส่ง Sir OPY — รอ R1 รับรองก่อน (ตามที่ผมแจ้ง OPY ไว้)


## 🔄 Session State (2026-09-07 — DA: naming model + กฎ Raven + จัดระเบียบ working copy)
- ✅ **มติ King Marx — naming model ใหม่** บันทึกแล้ว: `KB § ชั้นยศ` + `KB § 🐦 Raven Mail` · `DESIGN_PRINCIPLES` Decision log 2 แถว · `CLAUDE.md § 📢` 2 บรรทัด (ประกาศในคอมมิตเดียวกันตามหน้าที่ broadcast)
- ✅ artifact `process-map.html` แก้ชื่อกล่อง advisor + แถว ownership → **republish ทับ URL เดิม** (ไม่แตะเนื้อหาอื่นตามที่รับปากใน Raven)
- 🛠️ **พบและแก้: working copy ไม่ตรง origin ทั้ง 2 repo** — `M4RX-B4SE` ค้างบน branch `claude/upbeat-johnson-xdUyN` (1 commit `21cf15d`, **ไม่มี KB_ECOSYSTEM_ADMIN.md / DESIGN_PRINCIPLES.md บนดิสก์เลย**) → `git checkout -B main origin/main` ได้ `ec7af3e` · `RMN-eBidding-Workflow` ช้ากว่า origin **78 commit** → `merge --ff-only` ได้ `c61cfb9` · ⚠️ **ไม่มีข้อมูลหาย** ของครบบน origin/main ทุกไฟล์
- ⚠️ **บทเรียน PowerShell (จดไว้กันซ้ำ):** `$KL = Get-Content $k` — ถ้าใช้ชื่อ `$K` จะ **ทับตัวแปร `$k` ทันที** เพราะ PowerShell ไม่แยกตัวพิมพ์เล็ก/ใหญ่ → path กลายเป็นค่าว่าง เขียนไฟล์ไม่ได้ (เจอจริง 2 รอบ) · ต่อไปตั้งชื่อ array ว่า `$KL/$DL/$CL` เท่านั้น
- ⏸️ **pending approval — ยังไม่บันทึกลงดิสก์ ห้ามถือเป็นกฎ:** architecture Workspace/GitHub/LINE · ownership TAB 1/2/3 · ผู้รับสรุปรายวัน + ผู้มีสิทธิเขียน · guard rails ①–⑩ · ถ้อยคำเส้นแบ่ง advisor (เปิด/ปิด) · TAB 2 `basis_amount` รอคำตอบ Top
- 📌 LINE OA `RMN Finance Capture` **Friends = 1** → office/แม่ ยังไม่เข้าระบบ ยังทดสอบ intake จริงไม่ได้ · สถานะ not operational
