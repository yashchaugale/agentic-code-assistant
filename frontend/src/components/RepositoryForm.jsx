import { useState } from "react";

export default function RepositoryForm({ onAnalyze }) {
  const [repoUrl, setRepoUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!repoUrl.trim()) return;

    onAnalyze(repoUrl);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex gap-4"
    >
      <input
        type="text"
        placeholder="Paste GitHub Repository URL..."
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        className="flex-1 rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white outline-none focus:border-blue-500"
      />

      <button
        type="submit"
        className="rounded-lg bg-blue-600 px-6 py-3 font-semibold hover:bg-blue-700"
      >
        Analyze
      </button>
    </form>
  );
}