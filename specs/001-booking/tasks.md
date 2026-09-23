# Tasks: จองคิวตรวจสุขภาพ (Booking)
- Feature: จองคิวตรวจสุขภาพ (Booking)
- Spec ID: SPEC-BKG-001
- อ้างอิง plan.md: specs/001-booking/plan.md
- วันที่: 2569-09-23

## สรุป
- จำนวน task: 11
- จำนวน task ที่ต้องรอ Open Question: 1 (Q-02)

### T-01 สร้างตารางข้อมูลและ migration
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-01
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: migration สร้างตาราง slots, bookings, audit_logs และ schema บันทึก HN เท่านั้น
- สถานะ: เสร็จ

### T-02 สร้าง API ค้นช่วงว่างและคำนวณแพ็กเกจ
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_slots.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /slots ส่งคืนช่วงเวลาและที่นั่งคงเหลือใน 30 วันข้างหน้า และ p95 ความเร็วได้ตามเงื่อนไขทดสอบ
- สถานะ: พร้อมทำ

### T-03 กำหนด flow จองคิวและเตรียมการออกหมายเลขคิวตาม Q-02
- รองรับ: FR-BKG-04, IF-NOT-01
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_booking_basic.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: POST /bookings บันทึกการจอง ตัดที่นั่ง และคืนผลการจองพร้อม field queue_no แต่ยังต้องรอคำตอบ Q-02 เพื่อกำหนดรูปแบบและเงื่อนไขการออกหมายเลขคิวอย่างเป็นทางการ
- สถานะ: รอ Q-02

### T-04 ป้องกันการจองซ้ำในวันเดียวกัน
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_booking_duplicate.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: เมื่อมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน ระบบปฏิเสธการจองใหม่และส่งกลับหมายเลขคิวเดิม
- สถานะ: พร้อมทำ

### T-05 จัดการช่วงเวลาเต็มและเสนอ 3 ตัวเลือกใกล้เคียง
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/slots/service.py, backend/app/booking/service.py, backend/tests/test_booking_full_slot.py
- ต้องทำหลัง: T-02, T-03, T-04
- เสร็จเมื่อ: เมื่อช่วงเลือกเต็ม ระบบคืน 409 พร้อม 3 ช่วงที่ว่างใกล้ที่สุดในวันเดียวกันและวันถัดไป และไม่สร้างรายการจองซ้อน
- สถานะ: พร้อมทำ

### T-06 จัดการคิวส่งข้อความยืนยันและส่งซ้ำ
- รองรับ: FR-BKG-05, NFR-REL-02, IF-NOT-01
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_notification_retry.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: การจองยังถูกบันทึกแม้ส่งข้อความไม่สำเร็จ และมีงานส่งซ้ำภายใน 5 นาทีตามที่กำหนด
- สถานะ: พร้อมทำ

### T-07 สร้าง audit log middleware สำหรับการเข้าถึงข้อมูลการจอง
- รองรับ: DOM-PDPA-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/app/main.py, backend/tests/test_audit_log.py
- ต้องทำหลัง: T-01, T-03
- เสร็จเมื่อ: ทุกการเข้าถึงข้อมูลการจองบันทึก actor_id, accessed_at และ hn ลง audit log อย่างครบถ้วน
- สถานะ: พร้อมทำ

### T-08 ตรวจยืนยันตัวตนและค้น HN จาก HIS
- รองรับ: IF-IDP-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-08
- ไฟล์ที่แตะ: backend/app/auth/idp.py, backend/app/his/client.py, backend/app/main.py, backend/tests/test_identity_and_his.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: ระบบตรวจว่าผู้ใช้ยืนยันตัวตนแล้วก่อนเข้าถึงข้อมูลผู้รับบริการ และค้น HN จาก HIS โดยไม่เก็บเลขบัตรประชาชนในตารางการจอง
- สถานะ: พร้อมทำ

### T-09 สร้างหน้าเลือกแพ็กเกจและช่วงเวลาแบบ mock API
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานหน้าจอพื้นฐานของ T-09
- ไฟล์ที่แตะ: frontend/src/pages/SlotPicker.jsx, frontend/src/App.jsx, frontend/src/__tests__/SlotPicker.test.jsx
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: ผู้ใช้สามารถเลือกแพ็กเกจและวัน/ช่วงเวลาที่ว่างได้ พร้อมแสดงจำนวนที่นั่งคงเหลือจาก API จำลอง
- สถานะ: พร้อมทำ

### T-10 สร้างหน้ายืนยันและหน้าแสดงผลการจองแบบ mock API
- รองรับ: FR-BKG-03, FR-BKG-04, FR-BKG-05
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/pages/BookingResult.jsx, frontend/src/__tests__/AC-BKG-03.test.jsx
- ต้องทำหลัง: T-09
- เสร็จเมื่อ: หน้ายืนยันแสดงข้อความ “ช่วงเวลาเต็ม” พร้อม 3 ตัวเลือก และหน้าแสดงผลการจองแสดงหมายเลขคิวแม้ส่งข้อความไม่สำเร็จ
- สถานะ: พร้อมทำ

### T-11 ต่อหน้าจอกับ API จริงและยืนยัน flow หลัก
- รองรับ: FR-BKG-01, FR-BKG-03, FR-BKG-04, FR-BKG-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงาน integration ของ T-11
- ไฟล์ที่แตะ: frontend/src/api/client.js, frontend/src/pages/SlotPicker.jsx, frontend/src/pages/ConfirmBooking.jsx, frontend/src/pages/BookingResult.jsx
- ต้องทำหลัง: T-02, T-05, T-08, T-09, T-10
- เสร็จเมื่อ: หน้าจอเรียก API จริงผ่าน /api ได้และทุก flow หลักแลกเปลี่ยนข้อมูลกับ backend อย่างต่อเนื่อง
- สถานะ: พร้อมทำ

## ตารางตรวจความครบ AC
| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-03 |
| AC-BKG-02 | T-04 |
| AC-BKG-03 | T-05, T-10 |
| AC-BKG-04 | T-06 |
| AC-BKG-05 | T-02 |
| AC-BKG-06 | T-07 |

## ตารางตรวจความครบ Constraint
| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01 |
| DOM-PDPA-01 | T-01, T-07 |
| IF-IDP-01 | T-08 |
| IF-HIS-01 | T-01, T-08 |
| IF-NOT-01 | T-03, T-06 |

## สิ่งที่ยังไม่ทำ
- Q-02: หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร (เช่น A001)? -> ถามเจ้าหน้าที่เวชระเบียน
  - รอ task: T-03
- ไม่มี task ใดที่เกิน scope จาก spec เช่น login, README, หรือการจัดการหน้าที่ไม่อยู่ใน FR/Constraint ของฟีเจอร์นี้

