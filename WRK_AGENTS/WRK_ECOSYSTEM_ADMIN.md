# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-08-24 #3 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

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

## 🔄 Session State (2026-09-01 — DA: cleanup โครงสร้าง workflow ตามมติใหม่)
> คำสั่ง: ยกเลิก DB · คง DESIGN_PRINCIPLES.md เป็นเอกสาร DA เป็นเจ้าของ · ประกาศ ChatGPT RMN Command Center = Strategic Advisor นอก workflow · ล้าง reference DB/API-disabled/path EXP · **ห้ามลบไฟล์หรือ archive ใด ๆ**

### 🗂️ โครงสร้างหลังจัดใหม่ (ยืนยันจากไฟล์จริง device_list_dir 2026-09-01)
- **agent ใช้งานจริง 6 ตัว**: DA · OPY · DOC · EXP · MM · UI — ไม่มีตัวที่ 7
- **ยกเลิกแล้ว 2 ของ** (ไฟล์ยังอยู่ ห้ามลบ): API Status (disabled) · Design Board/DB (2026-09-01)
- `agents\` = 6 KB (+ โฟลเดอร์ `maps`) · `WRK_AGENTS\` = WRK ใช้จริง 5 + `WRK_API_STATUS.md`(disabled) + archive 2
- WRK ตัวที่ 6 = **`RMN-eBidding-KB\WRK_DOC_EXPIRY.md`** (16,447 B) ย้ายออกตาม Core Rule 19 (PII)
- `RMN_Enterprise\DESIGN_PRINCIPLES.md` = เอกสารหลักการ + Decision log · **เจ้าของ = DA** · ไม่มี session แยก
- ที่ปรึกษาภายนอก: **ChatGPT RMN Command Center = Strategic Advisor** (ไม่ถือ scope/ไม่แตะไฟล์/ไม่ commit) · **Claude = Operate & Execute**

### ✅ แก้ไปแล้ว (3 ไฟล์ที่ grep แล้วเจอจริง)
- `KB_ECOSYSTEM_ADMIN.md` — ถอด row API Status + row Design Board ออกจาก Agent Registry → ย้ายเข้าตาราง "ยกเลิกแล้ว" · ตัด `DB=Design Board` ออกจาก nickname · แทนบล็อก `🔀 DA ↔ DB` ด้วยบล็อก "DESIGN_PRINCIPLES = เอกสาร ไม่ใช่ agent" + เส้นแบ่งที่ปรึกษาภายนอก · แก้ path EXP → `RMN-eBidding-KB\WRK_DOC_EXPIRY.md` · refresh verified list เป็น 2026-09-01
- `DESIGN_PRINCIPLES.md` — เขียน header ใหม่ (เอกสาร ไม่ใช่ KB ของ DB · เจ้าของ DA · advisor boundary) · ปิดข้อละเมิด #2 (EXP path) + #3 (API agent) เป็น ✅ แก้แล้ว · เพิ่ม Decision log 3 บรรทัด (2026-09-01)
- `WRK_AGENTS\CLAUDE.md` — **ไม่แก้** · grep แล้ว **ไม่มี reference ของ DB / API_STATUS / "7 agent" / netlify เลย** · `L31` (path EXP → RMN-eBidding-KB) ถูกอยู่แล้ว

### ⚠️ ที่ DA แก้ให้ไม่ได้ — user ต้องทำเอง
- **Cowork project instructions** (อยู่นอก git · DA อ่าน/แก้ไม่ได้) — ยังลิสต์ 7 agent และอาจยังชี้ `WRK_AGENTS\WRK_DOC_EXPIRY.md`
- `DESIGN_PRINCIPLES.md:307` ยังเขียนว่างานลบ netlify เป็นของ DA (ทำเสร็จ 2026-08-31 แล้ว) — **นอกขอบเขตคำสั่งรอบนี้ จึงไม่แตะ**
- `WRK_AGENTS\CLAUDE.md` ยัง 21,573 B = เกินเพดาน 20 KB (ยกมาจากรอบก่อน)
