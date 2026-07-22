export default function RepositoryInfo({ repository }) {
  if (!repository) return null;

  const info = repository.data;

  return (
    <div className="mt-8 rounded-lg border border-gray-800 bg-gray-900 p-6">
      <h2 className="mb-4 text-xl font-bold">
        Repository Information
      </h2>

      <p>
        <strong>Language:</strong> {info.language}
      </p>

      <p>
        <strong>Framework:</strong> {info.framework}
      </p>

      <p>
        <strong>Entry Point:</strong> {info.entry_point || "Not Found"}
      </p>
    </div>
  );
}