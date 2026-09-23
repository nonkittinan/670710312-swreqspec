import { useEffect, useState } from 'react'

const today = new Date().toISOString().slice(0, 10)

export default function SlotPicker() {
  const [packageCode, setPackageCode] = useState('GENERAL')
  const [date, setDate] = useState(today)
  const [slots, setSlots] = useState([])

  useEffect(() => {
    const loadSlots = async () => {
      const params = new URLSearchParams({ date_from: date, package_code: packageCode })
      const response = await fetch(`/api/slots?${params.toString()}`)
      const data = await response.json()
      setSlots(data)
    }

    loadSlots()
  }, [packageCode, date])

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
        {slots.length === 0 ? (
          <p className="text-sm text-slate-500">ไม่พบช่วงเวลาว่างในวันที่เลือก</p>
        ) : (
          slots.map((slot) => (
            <button
              key={slot.id}
              type="button"
              className="flex w-full items-center justify-between rounded-xl border border-teal-200 bg-teal-50 px-4 py-3 text-left text-slate-700 shadow-sm"
            >
              <span>
                {slot.start_time} - {slot.end_time}
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
