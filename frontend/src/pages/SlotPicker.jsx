import { useMemo, useState } from 'react'

const mockSlots = [
  { id: 1, date: '2026-09-24', start: '09:00', end: '10:00', remaining: 3, packageCode: 'GENERAL' },
  { id: 2, date: '2026-09-24', start: '10:00', end: '11:00', remaining: 2, packageCode: 'GENERAL' },
  { id: 3, date: '2026-09-24', start: '13:00', end: '14:00', remaining: 1, packageCode: 'GENERAL' },
  { id: 4, date: '2026-09-24', start: '08:00', end: '09:00', remaining: 5, packageCode: 'PREMIUM' },
]

export default function SlotPicker() {
  const [packageCode, setPackageCode] = useState('GENERAL')
  const [date, setDate] = useState('2026-09-24')

  const visibleSlots = useMemo(() => {
    return mockSlots.filter((slot) => slot.packageCode === packageCode || !slot.packageCode)
  }, [packageCode])

  const filteredSlots = visibleSlots.filter((slot) => slot.date === date)

  return (
    <main className="mx-auto max-w-3xl p-6">
      <h1 className="text-2xl font-bold text-slate-800">เลือกแพ็กเกจและช่วงเวลา</h1>
      <div className="mt-6 grid gap-4 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
          แพ็กเกจ
          <select
            aria-label="แพ็กเกจ"
            value={packageCode}
            onChange={(event) => setPackageCode(event.target.value)}
            className="rounded-lg border border-slate-300 px-3 py-2 text-base"
          >
            <option value="GENERAL">GENERAL</option>
            <option value="PREMIUM">PREMIUM</option>
          </select>
        </label>

        <label className="flex flex-col gap-2 text-sm font-medium text-slate-700">
          วันที่
          <input
            aria-label="วันที่"
            type="date"
            value={date}
            onChange={(event) => setDate(event.target.value)}
            className="rounded-lg border border-slate-300 px-3 py-2 text-base"
          />
        </label>
      </div>

      <div className="mt-6 space-y-3">
        {filteredSlots.length === 0 ? (
          <p className="text-sm text-slate-500">ไม่พบช่วงเวลาว่างในวันที่เลือก</p>
        ) : (
          filteredSlots.map((slot) => (
            <button
              key={slot.id}
              type="button"
              className="flex w-full items-center justify-between rounded-xl border border-teal-200 bg-teal-50 px-4 py-3 text-left text-slate-700 shadow-sm"
            >
              <span>
                {slot.start} - {slot.end}
              </span>
              <span className="rounded-full bg-white px-2 py-1 text-sm font-medium text-teal-800">
                คงเหลือ {slot.remaining} ที่
              </span>
            </button>
          ))
        )}
      </div>
    </main>
  )
}
