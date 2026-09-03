# WRK_OPERATING — Session State & Pending (OPY)

> กฎทั้งหมดอยู่ที่ `WRK_OPERATING.md` · ไฟล์นี้เก็บ **state ล่าสุด + pending** เท่านั้น
> เขียน state ทุกครั้งที่งานเสร็จเป็นก้อน **ห้ามรอตอนจบ session** · เพดาน 20 KB — เกินแล้วตัด state เก่าสุดออก (ประวัติอยู่ใน git log)

## 🔄 Session State (2569-09-03)
- **Last SEQ (FY2569) = 220** · `seed_bids.js` **637 records** · `doc_fees.json` **36 entries** · queue **pending 0** · HEAD = origin `74a24ec`
- 🏗️ **DB agent ปิดตัว 2569-09-03** → OPY ตัดสินใจเรื่องไฟล์ตัวเองได้เอง · แยก state ออกจาก WRK รอบนี้ (กฎเพดาน 20 KB ของ DB ยังใช้ต่อ)
- 218 `69069406325` ทต.หนองกุง (กส.) 1,818,000 / 3,498,000 / 48.03 / มหาสารคาม → **✅ ต่ำสุด** · ไม่มีค่าเอกสาร
- 220 `69069484638` ทต.พระยืน (ขก.) 1,598,000 / 2,669,106.30 (=ราคากลาง) / 40.13 / มหาสารคาม · รักดี → **❌ −139,000** (ต่ำสุด 1,459,000)
  ค่าเอกสาร 500฿ KTB 405-1-49087-4 **ต้องจ่าย*ในวัน+เวลาเสนอราคา*เท่านั้น** — โอน 3 ก.ย. 14:04 ทัน · PDF ลง Log · ปิดเข้า doc_fees.json (36) แล้ว
- 📁 กฎใหม่: การ์ดต้องมีชื่อไฟล์ 3 ตัว + ปุ่มคัดลอก · tag ตาม entity · KB OPERATING.md รับ Doc Fee workflow จาก CLAUDE.md (DA raven 2569-09-03) · state แยกไฟล์นี้ออกมา
- 219 `68099553809` อบจ.บึงกาฬ ยื่น 6,865,000 / วงเงิน 6,870,000 / pct 0.07 / สกลนคร · entity **RMN** (plant=ตักสิลา ⚠) → **❌ −133,000** · ค่าเอกสาร 5,000฿ KTB 447-0-29255-9 จ่าย 02/09 แนบ e-GP ปิดแล้ว
- 🆕 กฎรอบนี้ (CLAUDE.md `8c46853`): DOC disabled → OPY ทำ fee ทั้งเส้น · Slip Verification บังคับ · git ผ่าน PowerShell · doc_fees.json เขียนได้ · FY2569 33 records pct เพี้ยน (seq≤158) = ของ DA ไม่ใช่งาน OPY
- ⚠️ id ขึ้นต้น 68 แต่ fiscalYear 2569 ได้ (คิดจาก `date`) · user แก้ entity กลางทางได้ ยึดครั้งล่าสุด

## ⏳ Pending
- **ไม่มี pending งานจริง** — ผลครบ · queue pending 0 · push ครบ
- ไม่เร่ง: skill `fee-payment` ยังชี้ path ปลายทาง PDF ผิด (ต้องเป็น Log folder) — OPY แก้ `*.skill` เองไม่ได้ ต้องให้ user/DA แก้

> 📜 state 2569-08-28 (seq 182/215/216/217 · queue 15 pending 0 · commit `e418c7c`) → ดู `git log` + `WRK_OPERATING_ARCHIVE_2569H2.md`
> ⚠️ บทเรียนที่ยังใช้: SEQ217 วงเงินในตาราง user พิมพ์ผิด 50,000 จริง 500,000 — ตัวเลขไม่สมเหตุผล = ถาม ห้ามเดา
