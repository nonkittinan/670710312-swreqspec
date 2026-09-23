# Prompt Log

## ครั้งที่ 1: 2569-09-23
- ใช้คำสั่ง: /tasks
- วัตถุประสงค์: แยก requirements จาก specs/001-booking/spec.md เป็น tasks.md ตามหลัก Spec-Driven Development
- ผลลัพธ์: สร้างไฟล์ specs/001-booking/tasks.md เสร็จสิ้น โดยมี 11 task, 1 task ที่รอ Q-02, ครอบคลุม AC และ Constraint ที่มีใน spec แล้ว
- หมายเหตุ: ไม่เริ่มทำ task ใด ๆ ตามเงื่อนไขของ prompt

## ครั้งที่ 2: 2569-09-23
- ใช้คำสั่ง: /tasks
- วัตถุประสงค์: ตรวจทบทวน tasks.md หลังทีมระบุว่าให้ดู 2 ตารางให้ไม่มีช่องว่างและให้ task เรื่องหมายเลขคิวต้องเป็นรอ Q-02 ไม่ใช่พร้อมทำ พร้อมตรวจชื่อ task ว่ามีอะไรเกิน scope หรือไม่
- ผลลัพธ์: ปรับ T-03 ให้ชัดว่าเป็นงานที่รอ Q-02 โดยตรง ไม่ได้เดาแบบก้าวหน้า, ปรับชื่อ T-11 ให้สอดคล้องกับโฟลว์จริง, และยืนยันในสิ่งที่ยังไม่ทำว่าไม่มี task ใดที่เกิน scope จาก spec เช่น login หรือ README
- ข้อผิดพลาดที่แก้: กรณีที่ task เรื่องหมายเลขคิวเคยมีลักษณะเหมือนงานปกติที่ดำเนินได้โดยไม่ถาม Q-02 ซึ่งขัดกับกฎ 'ห้ามเดา' และ 'task ที่เกี่ยวกับ Open Question ต้องเป็น รอ Q-xx'

## ครั้งที่ 3: 2569-09-23
- ใช้คำสั่ง: /implement T-01 specs/001-booking/tasks.md
- ไฟล์ที่สร้างหรือแก้: backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_db_schema.py
- ผล test: pytest -q tests/test_db_schema.py -> ผ่านหลังแก้ปัญหา SQLAlchemy type annotation และเรียก init_db() ก่อนตรวจ schema
- สิ่งที่เกือบต้องเดาแต่ถามแทน: ไม่มี; โครงสร้าง task เป็นไปตาม spec และ plan อย่างชัดเจน จึงไม่ได้ต้องเดา
