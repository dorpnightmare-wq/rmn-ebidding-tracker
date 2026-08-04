# Document Fee Payment Agent

## 🎯 Role
สร้าง PDF ใบแจ้งชำระเงินค่าซื้อเอกสารประกวดราคา + Email text

---

## 🚫 NEVER USE
TaskCreate · TaskUpdate · TaskList · AskUserQuestion · mcp__visualize__read_me

---

## 📥 Input Required (per project)
- สลิปชำระเงิน (PDF upload — ห้ามส่งเป็น image ใน chat)
- ประกาศจัดซื้อ (ยอดเงิน / เลขบัญชี / อีเมลหน่วยงาน / วันที่)
- ตารางโครงการ (เลขโครงการ e-GP / หน่วยงาน)

---

## 📄 PDF Rules
- **Layout**: แบบฟอร์ม (ไม่ใช่จดหมาย)
- **Title**: แบบฟอร์มใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์
- **Fields**: เลขโครงการ · ชื่อห้าง · ธนาคาร · จำนวนเงิน+ตัวอักษร · ชื่อผู้ชำระ+โทร
- **Slip image**: embed ในกล่องใต้ fields
- **⚠️ ห้ามมีเส้นกรอบ (box/rect) ล้อมรอบส่วนรายละเอียดด้านบน (fields เลขโครงการ...เบอร์โทร) — ใช้เส้นใต้ (underline) แต่ละ field เท่านั้น ไม่ต้องมี rect ครอบทั้งกลุ่ม**
- **⚠️ ระยะห่างระหว่างบรรทัด "หลักฐานการชำระเงิน (สลิป) :" กับกรอบรูปสลิป = 1.0cm (ไม่ใช่ 0.4cm)**
- **Font**: Sarabun + SarabunBold จาก `/tmp/` (download google/fonts ถ้าไม่มี)
- **Engine**: reportlab inline script + fitz (PyMuPDF) แปลง slip PDF → PNG
- **Save**: ใช้ bytes-path `os.scandir()` เพราะ OneDrive mount มี Thai filename encoding issue

### ชื่อไฟล์
`ใบแจ้งชำระเงินค่าซื้อเอกสาร_[ชื่อย่อหน่วยงาน]_[เลขโครงการ].pdf`

### Save path
`E-BIDDING/Log/ใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคา/`

---

## 👤 ชื่อผู้ชำระเงิน
| ประเภทการชำระ | ชื่อผู้ชำระ |
|---|---|
| โอนปกติ / Mobile Banking | นางอนุรักษ์ บารพรม |
| เงินสด / Bill Payment / Counter | ห้างหุ้นส่วนจำกัด รักดีการโยธา |

โทร: 0872235093

---

## ✉️ Email Rules
### ⚠️ Subject line (STRICT — ห้ามลืมอีก)
ต้องมี **ชื่อหน่วยงาน + เลขที่โครงการ** เสมอ ทุกฉบับ ไม่มีข้อยกเว้น:
```
ส่งหลักฐานการชำระเงินค่าซื้อเอกสารประกวดราคา [ชื่อหน่วยงาน] [เลขโครงการ]
```
ถ้าหน่วยงานเดียวกันหลายโครงการ → ใส่เลขโครงการทุกตัวคั่นด้วย " / " เช่น
`... อบต.เหล่ากลาง 69059322288 / 69059323640`

### Closing (ห้ามเปลี่ยน)
```
ขอแสดงความนับถือ
นางอนุรักษ์ บารพรม
หุ้นส่วนผู้จัดการ
โทร. 087-223-5093
```

### หน่วยงานเดียวกัน → รวม email ฉบับเดียว
- ระบุ **โครงการที่ 1 / 2 / 3** กำกับแต่ละรายการ
- แนบไฟล์ทุกโครงการในฉบับเดียว

### หน่วยงานต่างกัน → แยก email

---

## 🔧 Technical: Thai Filename Workaround
```python
d = b'/sessions/.../mnt/E-BIDDING/Log/'
for e in os.scandir(d):
    if b'\xe0\xb9\x83\xe0\xb8\x9a\xe0\xb9\x81\xe0\xb8\x88\xe0\xb9\x89\xe0\xb8\x87\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3' in e.name:
        target_dir = e.path; break
dest = target_dir + b'/' + fname.encode('utf-8')
with open(dest, 'wb') as f: f.write(data)
```

---

## 🔄 Session State (2026-06-02)
### ✅ Done
- อบต.ขัวก่าย 69049306591 (1,000฿ ธ.ก.ส.) ✅
- อบต.หนองน้ำใส 69049233820 (2,000฿ กรุงไทย เงินสด) ✅
- อบต.เหล่าอ้อย 3 โครงการ: 69059185784(600฿) + 69059186084(500฿) + 69059185990(500฿) ✅
- อบต.ดงลาน 69059077331 (1,000฿ กรุงไทย เงินสด) ✅

### ⚠️ Notes
- สลิปต้อง upload เป็น PDF/JPG — image ใน chat embed ไม่ได้
- เลขบัญชีในสลิปอาจต่างจากประกาศ → ใช้ข้อมูลจากสลิปจริง
- email รวมถ้าหน่วยงานเดียวกัน

## 📋 Session State
### ✅ Done (โครงการที่จ่ายแล้ว)
- อบต.กัวข้าย 69049306591 (1,000฿ ก.ส.ช.)
- อบต.หนองน้ำส 69049233820 (2,000฿ กรุงเทพ เงินสด)
- อบต.เหล้าอ้อย 69059185784 (600฿) + 69059186084 (500฿) + 69059185990 (500฿)
- อบต.ดงลาด 69059077331 (1,000฿ กรุงเทพ เงินสด)

## 📄 PDF Layout (ฟอร์มใบแจ้งการชำระเงิน)
**แบบฟอร์มใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์**

Fields:
- /ชื่อหน่วยงาน/
- วันที่ / เดือน / พ.ศ.
- เลขที่โครงการ
- ชำระเงินผ่าน/ธนาคาร: กรุงไทย / สาขา: ___
- จำนวนเงิน (ตัวเลข + ตัวอักษร)
- ชื่อผู้ชำระเงิน: /ชื่อห้างที่ยื่นเสนอราคา/
- เบอร์โทรติดต่อ: 087-223-5093
- [กล่อง embed สลิปการโอนเงิน]

หมายเหตุ: รูปสลิปใน chat → embed ในกล่องสลิป ไม่ต้อง upload PDF แยก

## 📄 PDF Layout Spec (STRICT — ห้ามเบี่ยงเบน)

### หน้า A4 — แนวตั้ง, margin 2cm ทุกด้าน

**[Title - Bold, center, 14pt]**
แบบฟอร์มใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์

**[Row 1 - Bold]** /ชื่อหน่วยงาน/

**[Row 2 - Bold]** วันที่ ___ เดือน ___ พ.ศ. ___

**[Row 3 - Bold]** เลขที่โครงการ: ___

**[Row 4 - Bold]** ชำระเงินผ่าน/ธนาคาร: กรุงไทย &nbsp;&nbsp;&nbsp; สาขา: ___

**[Row 5 - Bold]** จำนวนเงิน: ___ บาท &nbsp;&nbsp;&nbsp; จำนวนเงินตัวอักษร: ___

**[Row 6 - Bold]** ชื่อผู้ชำระเงิน: /ชื่อห้าง/ &nbsp;&nbsp;&nbsp; เบอร์โทรติดต่อ: 087-223-5093

**[กล่องสลิป — border 1pt, padding 10pt]**
/สลิปการโอนเงิน/ — embed รูปสลิปตรงนี้

### ⚠️ ข้อห้าม
- ห้ามใช้ตาราง 2 column
- ห้ามให้ text ทับกับ border
- spacing ระหว่าง row ไม่น้อยกว่า 12pt
- font Sarabun ทั้งหมด — Bold สำหรับ label

---

## 🔄 Session State (2569-08-04) — Doc Fee Agent closeout (หลัง Operating recheck x5)

**ย้ายมาจาก `WRK_OPERATING.md` (2569-08-04) — เดิมบันทึกผิดไฟล์ ควรอยู่ที่นี่ตั้งแต่แรก**

**สิ่งที่แก้เพิ่มในรอบนั้น (แก้ root cause ของบั๊กที่ Operating เจอ ไม่ใช่แค่ patch):**
- ล้าง `doc_fee_queue.json` entry `69079461100` ที่ค้าง `pending` ออกแล้ว (ยึด `doc_fees.json` เป็นความจริง — จ่ายจบจริง, แนบเข้า e-GP แล้ว)
- แก้ root cause ใน skill `e-bidding-operating`: เพิ่ม step 0 ก่อนเขียน queue ทุกครั้ง — grep `doc_fees.json` ด้วย id ก่อนเสมอ ถ้าจ่ายแล้วห้ามเขียน `pending` ซ้ำ/ห้าม dispatch ซ้ำ (สาเหตุจริงของบั๊กวันนั้น: dispatch ไป research ซ้ำโครงการที่จ่ายไปแล้วในเซสชันเดียวกัน)
- เพิ่มเนื้อหา "Division of labor" + "Announcement file structure" (annoudoc vs doc_*.pdf, ใช้ pdftotext -f 9 -l 10 ประหยัด token) เข้า skill `e-bidding-operating` ให้ตรงกับที่ Operating session บันทึกไว้ใน `WRK_OPERATING.md` อยู่แล้ว — sync 2 แหล่งให้ตรงกัน
- เพิ่ม git hygiene rule (ห้าม `git add .`, วิธีจัดการ `.git/*.lock`) เข้า skill โดยตรง ไม่ใช่แค่ WRK file — กัน agent ในอนาคตพลาดซ้ำแม้ไม่เคยอ่าน `WRK_OPERATING.md` มาก่อน

**Verified ไม่มีปัญหาอื่นจาก session นั้น:**
- ทั้ง 4 payment วันนั้น (69079109557, 69079189741, 69069467561, 69079461100) ครบใน `doc_fees.json`, PDF สร้างสำเร็จทุกตัว, ส่งตาม submitMethod ถูกต้อง
- Skill `fee-payment` และ `e-bidding-operating` save สำเร็จผ่าน `save_skill` ทั้งคู่ (ไม่มี validation_errors)

**Follow-up 2569-08-04 (คืนนี้) — บั๊กที่เจอเพิ่มในไฟล์นี้เอง, แก้แล้ว:**
- `doc_fee_queue.json` มี trailing comma → JSONDecodeError → แก้แล้ว (commit `43d3bce`), 6 entries `no_fee_required` ยังอยู่ครบ ไม่ได้หาย
- payer-name table (บรรทัดด้านบน "👤 ชื่อผู้ชำระเงิน"): "เงินสด/Bill Payment/Counter" เคยเขียนผิดเป็น "อาร์เอ็มเอ็น เอ็นเตอร์ไพส์" ที่ถูกคือ "รักดีการโยธา" → แก้แล้ว (commit `719a194`)
- ทั้ง 2 commit push ขึ้น origin/main แล้ว (verified: `2f768ff..719a194 main -> main`, `git push` ยืนยัน "Everything up-to-date")
- ค้าง (ไม่เร่งด่วน, เงินจริงไม่กระทบ): backfill session state งานตั้งแต่ 17 ก.ค. เป็นต้นมา (บึงกาฬ/โนนแหลมทอง x2/สกลนคร ฯลฯ) ไม่เคยถูกบันทึกไว้ที่นี่เลย — เคยบันทึกผิดไปที่ `WRK_OPERATING.md` แทน

**ไม่มีอะไรน่ากังวลอื่นแล้ว** — ไม่ต้อง over-audit ซ้ำรอบหน้าเว้นแต่เจอความผิดปกติจริง

### 📂 Working folder requirement (Doc Fee Agent)
- โฟลเดอร์หลัก: `RMN-eBidding-Workflow` (mounted จาก `C:\Users\Advice\OneDrive\Claude\Projects\RMN-eBidding-Workflow`)
- ไฟล์ที่แก้ได้เต็มสิทธิ์: `doc_fees.json`, `doc_fee_queue.json` (แก้/ลบได้ทั้งคู่ — ต่างจาก Operating ที่ append/read เท่านั้น), `WRK_AGENTS/WRK_FEE_PAYMENT.md` (ไฟล์นี้เอง)
- ไฟล์อ่านอย่างเดียว: `seed_bids.js`, `WRK_AGENTS/WRK_OPERATING.md` (ทั้งคู่ของ Operating Agent — ห้ามเขียนทับอีก)
- script ที่ต้องใช้: `WRK_AGENTS/scripts/generate_fee_pdf_fixed.py` (ห้ามใช้ตัวเก่าใน .claude/skills)
- ต้องมี mount เพิ่ม: `[EGP]_E-BIDDING - [R.M.N_GROUP]_DATABASE/Log/` (สำหรับ save PDF), `Downloads`/`uploads` (สำหรับหาสลิป)
- Git: sandbox ไม่มี push credentials — commit ได้เอง, ต้องให้ user รัน `git push` จาก PowerShell เสมอ; ถ้าเจอ `.git/*.lock` ใช้ `allow_cowork_file_delete` ก่อน rm

### 🚀 Prompt เริ่ม session ถัดไป — Doc Fee Payment Agent (copy-paste ได้เลย)
```
อ่าน WRK_AGENTS/WRK_FEE_PAYMENT.md ท้ายไฟล์ก่อน (session state ของตัวเอง)
อ้างอิงเพิ่มเติม: WRK_AGENTS/WRK_OPERATING.md หัวข้อ "Recheck x5" ท้ายไฟล์ (สถานะฝั่ง Operating Agent เท่านั้น ไม่ต้องแก้ไฟล์นั้น)

สถานะล่าสุด: doc_fee_queue.json ว่างสนิท (6 entries no_fee_required, JSON valid), doc_fees.json มี 4 รายการจ่ายวันนั้นครบ (บึงกาฬ/โนนแหลมทอง x2/สกลนคร)
แก้ root cause บั๊ก queue ค้างแล้วใน skill e-bidding-operating (เช็ค doc_fees.json ก่อนเขียน queue เสมอ)
ระเบียบใหม่ ว.515 (16 ก.ค. 2569) มีผลแล้ว: 2 วิธีจ่าย (bank_transfer/bill_payment) + submitMethod ต้องเช็คจากประกาศ (email/e-GP/both) ไม่ใช่ email เสมอไป
Dispatch architecture ทำงานแล้ว (e-bidding-operating → Agent tool → fee-payment) แต่ยังไม่เคยเห็น end-to-end เต็มรูปแบบตอนมีสลิปจริงมาปิดงาน — สังเกตรอบหน้า
ค้าง: backfill session state งานตั้งแต่ 17 ก.ค. (ไม่เร่งด่วน)

พร้อมรับสลิป/ประกาศใหม่ตามปกติ: หาสลิปจาก uploads/Downloads → ตรวจสอบ paymentMethod/submitMethod จากประกาศ →
สร้าง PDF ด้วย generate_fee_pdf_fixed.py เสมอ (ฝังสลิป) → log doc_fees.json → ทำตาม submitMethod (email draft และ/หรือบอก user แนบเข้า e-GP) →
ลบออกจาก queue → commit เฉพาะไฟล์ที่แก้ (ห้าม git add .) → ส่ง push command ให้ user
```

