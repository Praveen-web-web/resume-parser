export default function ParsedData({ data }) {
  return (
    <div className="mt-6 p-4 border rounded bg-gray-50">
      <h2 className="text-xl font-bold mb-2">Parsed Resume Data</h2>
      <ul className="list-disc pl-5 space-y-1">
        {Object.entries(data).map(([key, value]) => (
          <li key={key}>
            <strong>{key.replace(/_/g, ' ')}:</strong> {value || 'Not found'}
          </li>
        ))}
      </ul>
    </div>
  )
}