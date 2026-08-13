# 📱 BOOTSTRAP_IOS — เปิด session บนมือถือ

> ใช้เฉพาะ **OPY** (บันทึกผลประมูล) และ **DA** (อ่าน state) เท่านั้น
> DOC · EXP · MM · UI · API → **PC เท่านั้น**

---

## 🔴 ข้อจำกัด (ยืนยันจากการทดสอบจริง 2026-08-13)
- session มือถือรันใน **cloud container** ไม่ใช่บน iPhone
- **ไม่มี bridge ไป PC** — bridge ผูกกับ session ที่เปิด ไม่ใช่ผูกกับบัญชี
- มือถือ **เห็นไฟล์ OneDrive/PC ไม่ได้เลย** → ช่องทางเดียวคือ git
- auth ของแอป GitHub อยู่ในเครื่อง iPhone → **container ใช้ไม่ได้** (Claude push เองไม่ได้)
- container ลบตัวเองเมื่อ session จบ → **งานที่ยังไม่ commit = หายถาวร**
- ไม่มีฟอนต์ไทย Sarabun → **ห้ามสร้าง PDF ราชการบนมือถือ**

---

## ▶️ Flow มาตรฐาน — ไม่ใช้ PAT

```
Claude มือถือ  ①อ่าน context (clone)
               ②ร่าง record JSON + widget ราคายื่น
                        ↓ copy
นาย            ③แอป GitHub → Edit File → Go to line → วาง → Commit
                        ↓
PC             ④git pull ก่อนเริ่มงานครั้งถัดไป (บังคับ)
```

### ① Clone (Claude รันเอง)
```
git clone --depth 1 -b main https://github.com/m4dm4rx/RMN-eBidding-Workflow.git
```
> ⚠️ ต้องมี `-b main` เสมอ

### ② อ่าน context ตาม agent
| เรียก | อ่านไฟล์ |
|---|---|
| **OPY** | `WRK_AGENTS/CLAUDE.md` → `KB/OPERATING.md` → `WRK_AGENTS/WRK_OPERATING.md` |
| **DA** | `WRK_AGENTS/CLAUDE.md` → `KB/agents/KB_ECOSYSTEM_ADMIN.md` → `WRK_AGENTS/WRK_ECOSYSTEM_ADMIN.md` |

### ③ Commit ผ่านแอป GitHub (นายทำเอง)
1. เปิด repo → ตรวจ **branch = `main`** (สำคัญที่สุด)
2. `seed_bids.js` → `···` → **Go to line** → บรรทัดสุดท้ายก่อน `];`
3. **Edit File** → วาง record ที่ Claude ร่างให้ (อย่าลืม `,` ท้ายบรรทัดก่อนหน้า)
4. **Commit** — ข้อความ: `seed: add seq NNN <หน่วยงาน> (ต่ำสุด/ไม่ต่ำสุด)`

---

## ⚠️ กฎกันข้อมูลหาย
1. **PC ต้อง `git pull` ก่อนเริ่มงานทุกครั้ง** — กัน split-brain
2. **เช็ค branch = main ทุกครั้งก่อน commit** — เคยมีบั๊ก master ค้างที่ seq 103 (105 บรรทัด) ขณะ main มี 553 records
3. **ห้ามแก้ค้างข้ามวัน** ทั้ง 2 ฝั่ง
4. **มือถือห้ามสร้าง scheduled task** — PC เป็นเจ้าของ 2 ตัวเดียว
5. **DA บนมือถือ = read-only** เขียน session state ตอนกลับ PC เท่านั้น
6. **KB มี 2 ที่** — ต้นฉบับ `M4RX-B4SE\...\E-Bidding\` · สำเนา `KB/` ใน repo
   → แก้ที่ต้นฉบับเสมอ แล้ว copy ทับ `KB/` ก่อน push (2 ไฟล์: `OPERATING.md`, `agents/KB_ECOSYSTEM_ADMIN.md`)

---

## 🚫 ห้ามทำบนมือถือ
| งาน | เหตุผล |
|---|---|
| MM แผนที่ PDF | ต้องใช้ `[EGP]_DATABASE` folder |
| DOC ใบแจ้งชำระ PDF | ไม่มีฟอนต์ Sarabun |
| DOC ตรวจสลิป | จอเล็ก เสี่ยงอนุมัติผิด |
| UI แก้ tracker HTML | ต้อง preview จอใหญ่ |
| EXP · API | นอก scope |

---

## 📌 Repo state (ณ 2026-08-13)
- default branch = **main** (เดิมเป็น master → แก้แล้ว)
- ลบ `master` และ `claude/pull-latest-changes-XmNZQ` ทิ้งแล้ว
- `seed_bids.js` = 553 records · seq ครบทุก record (ลำดับ key ไม่เหมือนกัน ไม่ใช่บั๊ก)
