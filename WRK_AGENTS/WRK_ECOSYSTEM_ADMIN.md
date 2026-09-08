# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-09-07 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 🔄 Session State (2026-09-07 — DA: naming model + กฎ Raven + จัดระเบียบ working copy)
- ✅ **มติ King Marx — naming model ใหม่** บันทึกแล้ว: `KB § ชั้นยศ` + `KB § 🐦 Raven Mail` · `DESIGN_PRINCIPLES` Decision log 2 แถว · `CLAUDE.md § 📢` 2 บรรทัด (ประกาศในคอมมิตเดียวกันตามหน้าที่ broadcast)
- ✅ artifact `process-map.html` แก้ชื่อกล่อง advisor + แถว ownership → **republish ทับ URL เดิม** (ไม่แตะเนื้อหาอื่นตามที่รับปากใน Raven)
- 🛠️ **พบและแก้: working copy ไม่ตรง origin ทั้ง 2 repo** — `M4RX-B4SE` ค้างบน branch `claude/upbeat-johnson-xdUyN` (1 commit `21cf15d`, **ไม่มี KB_ECOSYSTEM_ADMIN.md / DESIGN_PRINCIPLES.md บนดิสก์เลย**) → `git checkout -B main origin/main` ได้ `ec7af3e` · `RMN-eBidding-Workflow` ช้ากว่า origin **78 commit** → `merge --ff-only` ได้ `c61cfb9` · ⚠️ **ไม่มีข้อมูลหาย** ของครบบน origin/main ทุกไฟล์
- ⚠️ **บทเรียน PowerShell (จดไว้กันซ้ำ):** `$KL = Get-Content $k` — ถ้าใช้ชื่อ `$K` จะ **ทับตัวแปร `$k` ทันที** เพราะ PowerShell ไม่แยกตัวพิมพ์เล็ก/ใหญ่ → path กลายเป็นค่าว่าง เขียนไฟล์ไม่ได้ (เจอจริง 2 รอบ) · ต่อไปตั้งชื่อ array ว่า `$KL/$DL/$CL` เท่านั้น
- ⏸️ **pending approval — ยังไม่บันทึกลงดิสก์ ห้ามถือเป็นกฎ:** architecture Workspace/GitHub/LINE · ownership TAB 1/2/3 · ผู้รับสรุปรายวัน + ผู้มีสิทธิเขียน · guard rails ①–⑩ · ถ้อยคำเส้นแบ่ง advisor (เปิด/ปิด) · TAB 2 `basis_amount` รอคำตอบ Top
- 📌 LINE OA `RMN Finance Capture` **Friends = 1** → office/แม่ ยังไม่เข้าระบบ ยังทดสอบ intake จริงไม่ได้ · สถานะ not operational

## 🔄 Session State (2026-09-07 ต่อ — DA: Finance Capture v1 ส่งมอบ + ย้าย repo ออกจาก OneDrive)
- ✅ **Execution Card RMN Finance Capture v1 ปิดครบ** — `M4RX-B4SE` `8ddaa84` governance (ก่อน) → `1ee1c0f` implementation · `Workflow` `40f8455` broadcast · RC1–RC9 อยู่ในโค้ดจริง · **60 offline tests ผ่านบนเครื่อง** · dependency 0 ตัว · ไม่มี secret ในไฟล์ใด · **หยุดก่อน deploy ตามคำสั่ง**
- 📌 MB1 ปิด: Messaging API channel `RMN Finance Capture` **Channel ID 2011458199** (ID ไม่ใช่ secret บันทึกได้)
- ✅ **ย้าย repo 3 ตัวออกจาก OneDrive → `C:\Repos\`** (path เดียวกันทุกเครื่อง ไม่มีชื่อ user) · `Workflow` `3c44f15` · `M4RX-B4SE` `1d37740`
- 🔴 **OneDrive ทำ git พังจริง 3 แบบในวันเดียว** — บทเรียนที่แพงที่สุดของวันนี้:
  ① `.git/*.lock` ค้าง ลบจาก mount ไม่ได้ → commit ไม่ผ่าน (แก้ชั่วคราวด้วย `mv` ได้ แต่ไม่ควรต้องทำ)
  ② `.git/objects` **ขาด ~60 objects** + reflog เสีย + commit-graph parse ไม่ผ่าน → `RMN-eBidding-Workflow` ต้อง **re-clone ทั้ง repo**
  ③ clone ลงมา **ผิด branch** เพราะ `origin/HEAD` ของ `M4RX-B4SE` ชี้ `claude/upbeat-johnson-xdUyN` (scaffold 1 commit) — หลอกทั้ง DA ตอนบ่ายและ clone ใหม่ตอนดึก · แก้ default branch บน GitHub แล้ว
- ⚠️ **path เดิมผูกชื่อ user** `C:\Users\Advice\OneDrive\...` → เครื่องที่ 2 (`asus`) ใช้ไม่ได้ตั้งแต่ต้น ไม่ใช่เพิ่งพัง
- ⚠️ **บทเรียน git จาก mount**: `device_bash` ลบไฟล์ไม่ได้ทั้ง mount (ไม่ใช่แค่ OneDrive) และ `core.autocrlf` ไม่ตั้งใน VM → ถ้า commit ตรงๆ ไฟล์ CRLF ที่ไม่ได้แตะจะกลายเป็น diff ทั้งไฟล์ · ต้องใส่ `-c core.autocrlf=input` ทุกคำสั่ง · **git ต้องผ่าน PowerShell เท่านั้น กฎเดิมถูกแล้ว**
- ⏸️ **ค้าง 4 ข้อ**
  ① `SKILL.md` ของ scheduled task ยังชี้ OneDrive · อยู่นอก git · `Documents\Claude` ขอสิทธิ์ผ่าน bridge ไม่ได้ → user รันสคริปต์เอง **ทั้ง 2 เครื่อง** (จุดนี้เคยทำ checker พังเงียบเป็นสัปดาห์)
  ② `_old_*` + `.corrupt_20260907` ใน OneDrive — เก็บ 7 วันแล้วลบ
  ③ Q1 Codex deploy GCP ได้จริงไหม — ถ้าไม่ได้ `runbook/RUNBOOK.md` เขียนให้ King Marx ทำเองครบทุกขั้น + rollback
  ④ Q2 แม่/Office เป็นเพื่อน OA + OA เข้ากลุ่มแล้วยัง — **Friends ยัง = 1** daily summary ยังส่งไม่ถึงใคร
- 🔎 **ยังไม่ย้าย ต้องตัดสินแยก** — `BSKNBot\` และ `RMN e-Bidding Tracker\` ยังเป็น repo ใน OneDrive เสี่ยงแบบเดียวกันเป๊ะ
- 📌 **แต่ละ Sir แก้ path ใน WRK ของตัวเอง** — DA แก้ให้ไม่ได้ตามกฎ ownership · ประกาศรายชื่อไฟล์ไว้ใน `CLAUDE.md § 📢` แล้ว · Sir MM ยังมี `WRK_MAPMAKER.md` uncommitted อยู่บนดิสก์ (ไฟล์ไม่หาย แต่ของที่เคย `git add` หายไปกับ object ที่เสีย ต้อง add ใหม่)


## 🔄 Session State (2026-09-08 — DA: จัดระเบียบ path หลังย้าย repo + รับ EBIDDING.md เข้า ownership)
- ✅ **`SKILL.md` ของ scheduled task 3 ตัวแก้ path → `C:\Repos\...`** (`doc-fee-morning-alert` ไม่ต้องแก้) · ⚠️ ไฟล์อยู่ `%USERPROFILE%\Documents\Claude\Scheduled\` **นอก git และมีแค่บนเครื่อง PC MARX** → เครื่อง `asus` ไม่มีเลย ต้องทำซ้ำเมื่อย้ายเครื่อง
- ✅ **registry**: `KB § scheduled tasks` บันทึก path ใหม่ครบ 4 task + ความเปราะที่ผูกกับเครื่องเดียว (`M4RX-B4SE 6360954`)
- ✅ **รับ `EBIDDING.md` เข้า Ownership Matrix + ติดป้าย ⚠️ HISTORICAL + ครอบ ⛔ 3 ส่วนที่ชี้ path ผิด** (`§ Files & URLs` · `§ Multi-Machine` · `§ Git Push`) — **ไม่ลบเนื้อหาเดิม เก็บเป็นหลักฐาน** (`M4RX-B4SE 33bc8b2`)
- 🔴 **ผมนับผิดเอง** — รายงานว่าเจอ scheduled task "ตัวที่ 5" แต่ registry ถูกอยู่แล้วที่ 4 ตัว (นับ `doc-fee-morning-alert` ซ้ำ) · บันทึกเป็นความผิดของผมใน `DESIGN_PRINCIPLES` Decision log
- ⚠️ **commit 2 ตัวมี BOM ในหัวข้อ** (`9c93cff`, `6360954`) เพราะ `Set-Content -Encoding UTF8` เขียน BOM → ต่อไปใช้ `New-Object Text.UTF8Encoding $false` เท่านั้น · แก้ย้อนหลังได้แต่ต้อง force-push **ยังไม่ทำ รอคำสั่ง**
- 📌 **archive รอบนี้** ย้าย session `09-04` + `09-05` (94 บรรทัด) เข้า `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` เพราะไฟล์ชน `20,453 / 20,480 B` เหลือ 27 B · **ตัดท้ายเข้า archive ไม่ขยายเพดาน**
- ⏸️ **ค้างต่อ** ① Raven ให้ Sir UI/UX ยืนยัน `EBIDDING.md § UI Rules` + `§ STATUS values` ยังตรงกับ tracker ไหม (**ต้องให้ King Marx เป็นคนส่ง**) ② Q1 Codex deploy GCP ได้จริงไหม ③ Q2 แม่/Office เป็นเพื่อน OA + OA เข้ากลุ่ม (**Friends ยัง = 1**) ④ deploy Finance Capture รออนุมัติแยก ⑤ `_old_*` + `.corrupt_20260907` ครบ 7 วันแล้วลบ ⑥ `BSKN-Expense_Bot-LINE` ahead 3 + dirty 4 ไฟล์ — King Marx ย้ายเอง ⑦ `Company-Assets/` + `KB_DOC_EXPIRY.md` ยังไม่มีเจ้าของใน git
