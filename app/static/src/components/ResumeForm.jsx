import { useState } from 'react'
import ParsedData from './ParsedData'

export default function ResumeForm() {
  const [parsedData, setParsedData] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    const formData = new FormData()
    formData.append('name', e.target.name.value)
    formData.append('email', e.target.email.value)
    formData.append('location', e.target.location.value)
    formData.append('file', e.target.file.files[0])

    const res = await fetch('/upload-resume', {
      method: 'POST',
      body: formData
    })

    const data = await res.json()
    setParsedData(data)
  }

  return (
    <div className="max-w-xl mx-auto bg-white p-6 rounded shadow">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="name" placeholder="Name" required className="border p-2 w-full rounded" />
        <input name="email" placeholder="Email" required className="border p-2 w-full rounded" />
        <input name="location" placeholder="Location" required className="border p-2 w-full rounded" />
        <input name="file" type="file" accept=".pdf,.docx" required className="border p-2 w-full rounded" />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          Upload Resume
        </button>
      </form>

      {parsedData && <ParsedData data={parsedData} />}
    </div>
  )
}