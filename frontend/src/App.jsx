import { useState } from "react";

import Header from "./components/Header";
import RepositoryForm from "./components/RepositoryForm";
import RepositoryInfo from "./components/RepositoryInfo";

import api from "./services/api";

function App() {
  const [repository, setRepository] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeRepository = async (repoUrl) => {
    try {
      setLoading(true);

      const response = await api.post("/analyze", {
        repo_url: repoUrl,
      });
      console.log("FULL RESPONSE:", response);
      console.log("DATA:", response.data);

      setRepository(response.data.analysis);
    } catch (error) {
  console.error("Error:", error);

  if (error.response) {
    console.log("Status:", error.response.status);
    console.log("Data:", error.response.data);
  }

  alert("Failed to analyze repository.");
} finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      <Header />

      <main className="mx-auto max-w-6xl p-8">

        <RepositoryForm onAnalyze={analyzeRepository} />

        {loading && (
          <p className="mt-6">
            Analyzing repository...
          </p>
        )}

        <RepositoryInfo repository={repository} />

      </main>
    </div>
  );
}

export default App;