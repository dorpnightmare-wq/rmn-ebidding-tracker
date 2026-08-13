# E-bidding Operating Assistance

## 🎯 Task Scope
รับข้อมูลการประมูล → เพิ่ม/แก้ไข `seed_bids.js` → git push

---

## 📋 Current Seq Status
> ❌ ห้าม hardcode ตาราง seq ที่นี่ (เคยมีตารางค้างที่ seq 94-102 ล้าหลัง 75 รายการ — ลบแล้ว 2026-08-13)
> ✅ อ่านจาก `seed_bids.js` เสมอ = source of truth
> หา seq ถัดไป: กรอง `fiscalYear` ล่าสุด → `max(seq) + 1`
> `fiscalYear` คำนวณจาก field `date` (วันประกาศ) — เดือน ≥ ต.ค. → ปี+1


---

## ⏳ Pending
- ไม่มี

## ✅ Done This Session
- seq 94–95 added (26 พค.69)
- seq 96–98 fixed road codes + midPrice/lowest (28 พค.69)
- seq 99–100 fixed name/status + midPrice/lowest (29 พค.69)
- seq 101 added (29 พค.69 บ่าย)
- seq 102 added + lowest confirmed (2 มิ.ย.69 บ่าย)

---

## 🔀 Data Entry Rules
- pct = `round((budget - bid) / budget * 10000) / 100`
- ต่ำสุด → `"รอผลพิจารณา [ เป็นผู้เสนอต่ำที่สุด ]"`
- ไม่ต่ำสุด → `"รอผลพิจารณา [ ไม่ได้เป็นผู้เสนอต่ำที่สุด ]"`
- ผลเช้า → 12:01 · ผลบ่าย → 16:01

## 🧬 Entry Schema — template บังคับ (เพิ่ม 2569-08-13 ตามที่ DA แจ้ง)
ทุก record ที่เพิ่มใหม่ **ต้องมี `fiscalYear` เสมอ** (เดิม template ไม่มี field นี้ → เกิด record ขาด 143 ตัว DA ต้องมาไล่เติมย้อนหลัง)

```js
{"seq": N, "id": "69XXXXXXXXX", "name": "...", "agency": "...", "province": "...",
 "budget": 0, "bid": 0, "pct": 0.00, "entity": "หจก.รักดี การโยธา",
 "status": "รอผลพิจารณา", "date": "2569-MM-DD", "midPrice": 0.00,
 "workType": "เสริมผิว", "plant": "มหาสารคาม", "fiscalYear": 2569}
```

**กฎคำนวณ `fiscalYear`** (ปีงบไทยเริ่ม 1 ต.ค.) — คำนวณจาก field **`date` (วันประกาศ)** เท่านั้น:
- เดือนของ `date` ≥ 10 (ต.ค.–ธ.ค.) → `fiscalYear = ปีของ date + 1` (เช่น `2568-10-15` → **2569**)
- เดือนของ `date` 01–09 → `fiscalYear = ปีของ date` (เช่น `2569-08-07` → **2569**)

> ⚠️ **แก้ไข 2569-08-13 (override กฎเดิม):** ห้ามคำนวณจากเลข `id` — id เข้ารหัส **เดือนที่ขึ้นระบบ e-GP** ซึ่งไม่ตรงกับวันประกาศจริงใน 26 records (DA ตรวจพบ) ยึด `date` เป็น source of truth เสมอ

- ห้ามละ field นี้แม้เพิ่ม record เดียว — ตรวจก่อน commit ทุกครั้ง
