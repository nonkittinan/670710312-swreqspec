import { fireEvent, render, screen } from '@testing-library/react'
import SlotPicker from '../pages/SlotPicker.jsx'

test('แสดงช่วงเวลาว่างและจำนวนที่นั่งคงเหลือเมื่อเลือกแพ็กเกจและวันที่', async () => {
  render(<SlotPicker />)

  expect(screen.getByText('เลือกแพ็กเกจและช่วงเวลา')).toBeTruthy()

  fireEvent.change(screen.getByLabelText('แพ็กเกจ'), {
    target: { value: 'GENERAL' },
  })

  fireEvent.change(screen.getByLabelText('วันที่'), {
    target: { value: '2026-09-24' },
  })

  expect(await screen.findByText(/09:00/)).toBeTruthy()
  expect(screen.getByText(/คงเหลือ\s*3\s*ที่/)).toBeTruthy()
})
