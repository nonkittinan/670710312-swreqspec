# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:40 | test: 5 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ไม่ตรงเรื่อง), ไม่มี AC ตรง | T-02 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py: test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | ไม่มีการป้องกันคิวซ้ำในวันเดียวกันใน backend/app/booking/service.py:create_booking | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มีการคำนวณ 3 ช่วงที่ใกล้ที่สุดใน backend/app/booking/service.py หรือ backend/app/slots/service.py | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py: create_booking, next_queue_no, cancel_booking; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_01.py: test_AC_BKG_01 (ผ่าน) | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่มีคิวส่งข้อความซ้ำและไม่มีการคงบันทึกการจองเมื่อส่งข้อความไม่สำเร็จ | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-10 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | ไม่มี | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: test_AC_BKG_05 (ผ่าน) | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มีการบังคับ TLS 1.2 หรือการปกป้องข้อมูลรับส่ง | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มีคิว retry ภายใน 5 นาที | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มีการทดสอบผู้ใช้ใหม่ 8/10 คน | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL; backend/app/db/migrations/001_init.py: upgrade | backend/tests/test_T01_schema.py: test_T01_tables_created (ผ่าน) | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | ไม่มี audit middleware หรือการบันทึก audit log ณ runtime; มีเฉพาะตาราง backend/app/db/models.py: AuditLog | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC ตรง | T-03 | backend/app/auth/idp.py: get_verified_hn | backend/tests/test_AC_BKG_01.py: test_AC_BKG_01 (ผ่าน แต่ indirect) | ครบ |
| IF-HIS-01 | ไม่มี AC ตรง | T-09 | backend/app/booking/router.py: BookingRequest.national_id; backend/app/booking/router.py: logger.info(... national_id ...) | backend/tests/test_T01_schema.py: test_T01_no_national_id (ผ่าน) | ช่องโหว่ |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มีคิวส่งข้อความแบบ asynchronous และไม่มีการเก็บงานค้างส่ง | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/service.py: list_available_slots | FR-BKG-01 | ไม่ครบ | กำหนด DAYS_AHEAD = 14 แต่ spec ระบุภายใน 30 วันข้างหน้า |
| backend/app/booking/service.py: create_booking | FR-BKG-02 | ไม่ครบ | ไม่มีการตรวจว่าผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ส่วนหนึ่ง | บันทึกการจองและตัดที่นั่งทำได้ แต่การคัดกรองที่นั่งเต็มใช้ `remaining < 0` แทน `<= 0` |
| backend/app/booking/service.py: next_queue_no | Q-02 | ไม่ตรง | เลือกรูปแบบ `A001` โดยไม่มีคำตอบจากเจ้าหน้าที่เวชระเบียน |
| backend/app/booking/router.py: BookingRequest.national_id | IF-HIS-01 | ไม่ตรง | ระบุ field เลขบัตรประชาชนใน request แม้ spec บอกไม่เก็บและไม่ให้ใช้ |
| backend/app/booking/router.py: logger.info("national_id") | DOM-PDPA-01, IF-HIS-01 | ไม่ตรง | บันทึกข้อมูลที่ spec ห้ามเก็บ/แสดงใน log |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ตรง | ตั้งค่า PostgreSQL สำหรับระบบจริง แต่ test ใช้ SQLite เท่านั้น |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ตรง | ตรวจ token รูปแบบ `Bearer verified:<HN>` ก่อนเปิดข้อมูล |
| frontend/src/App.jsx | FR-BKG-01, FR-BKG-03 | ไม่ทำ | หน้าเว็บยังเป็นโครงเริ่มต้น ไม่แสดงผลการจองหรือการแจ้งช่วงเวลาเต็ม |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | spec ระบุภายใน 30 วันข้างหน้า แต่โค้ดใช้ 14 วัน จึงไม่ทำตามข้อความที่ผู้ใช้เห็นจริง | แก้โค้ด - ต้องใช้ 30 วันตาม FR-BKG-01 และปรับ test ให้ตรงกับเงื่อนไขจริง |
| F-002 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | Q-02, FR-BKG-04 | โค้ดกำหนดรูปแบบ `A001` โดยไม่ได้รอคำตอบจากเจ้าหน้าที่เวชระเบียน ทำให้การแสดงหมายเลขคิวเป็นการเดาแทนทีม | เพิ่ม Q-xx - รอเจ้าหน้าที่เวชระเบียนตอบก่อนออกแบบหมายเลขคิวและการทดสอบ |
| F-003 | ละเมิด Constraint | backend/app/booking/router.py: BookingRequest.national_id; logger.info("national_id") | IF-HIS-01, DOM-PDPA-01 | มี field เลขบัตรประชาชนและบันทึกลง log แม้ spec ระบุไม่เก็บเลขบัตรประชาชนในตารางการจองและควรเก็บเฉพาะ HN | แก้โค้ด - ลบ field และ log ที่แฝงเลขบัตรประชาชนออกจาก request และทุก log |
| F-004 | test อ่อน / ช่องโหว่ | backend/app/booking/service.py: create_booking | FR-BKG-04 | เงื่อนไข `if slot.remaining < 0` ช่วยให้ remaining = 0 ยังจองได้และทำให้ slot ติดลบได้ ส่วน test ที่มีอยู่แค่ remaining=1 จึงไม่เปิดเผยจุดนี้ | แก้โค้ด - ใช้ `remaining <= 0` เพื่อป้องกันไม่ให้มีที่ว่าง 0 ยังจองได้ และเพิ่ม test ขอบ |
| F-005 | FR ไม่มี AC | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | FR-BKG-06 | spec มีคำสั่งให้คำนวณช่วงว่างตามแพ็กเกจ แต่ไม่มี AC ใดตรวจเรื่องนี้ จึงเป็นช่องโหว่ของ spec ที่ช่วยให้โค้ดไม่ถูกตรวจจริง | แก้ spec - เพิ่ม AC สำหรับการเปลี่ยนแพ็กเกจหรือเว้นเรื่องนี้ออกจาก scope |
| F-006 | ของแถม | backend/app/booking/router.py: cancel_booking; backend/app/booking/service.py: cancel_booking | UC-02, Out of scope | มี endpoint ยกเลิกการจอง และฟังก์ชันคืนที่นั่ง แม้ spec ระบุยกเลิก/เลื่อนคิวเป็น Out of scope | แก้โค้ด - ของแถม อยู่ใน Out of scope (UC-02) ลบ endpoint และ cancel_booking ออก |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | - | ไม่มีข้อค้นพบเดิมที่แก้แล้วในรอบนี้ |
