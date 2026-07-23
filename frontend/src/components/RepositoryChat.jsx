import { useState } from "react";
import api from "../services/api";

export default function RepositoryChat({ sessionId }) {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response = await api.post("/chat", {
        session_id: sessionId,
        question,
      });

      console.log(response.data);

      setMessages((prev) => [
        ...prev,
        {
          question,
          answer: response.data.answer,
          sources: response.data.sources || [],
        },
      ]);

      setQuestion("");
    } catch (error) {
      console.error(error);
      alert("Failed to get response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-8 rounded-lg border border-gray-800 bg-gray-900 p-6">
      <h2 className="mb-4 text-xl font-bold">Ask RepoMind</h2>

      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything about this repository..."
        className="w-full rounded bg-gray-800 p-3 text-white"
        rows={4}
      />

      <button
        onClick={askQuestion}
        disabled={loading}
        className="mt-4 rounded bg-blue-600 px-4 py-2 hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "🤖 RepoMind is thinking..." : "Ask"}
      </button>

      <div className="mt-8 space-y-8">
        {messages.map((msg, index) => (
          <div
            key={index}
            className="rounded-lg border border-gray-800 bg-gray-800 p-6"
          >
            <div className="mb-6">
              <h3 className="mb-2 font-bold text-blue-400">You</h3>
              <p>{msg.question}</p>
            </div>

            <div>
              <h3 className="mb-2 font-bold text-green-400">RepoMind</h3>
              <p className="whitespace-pre-wrap">{msg.answer}</p>
            </div>

            {msg.sources.length > 0 && (
              <div className="mt-6">
                <h4 className="mb-3 font-semibold">Sources</h4>

                <div className="space-y-2">
                  {msg.sources.map((source, i) => (
                    <div
                      key={i}
                      className="rounded bg-gray-700 px-4 py-3"
                    >
                      <p className="font-medium">
                        📄{" "}
                        {source.file.replace(
                          "repositories/Packet_analyzer/",
                          ""
                        )}
                      </p>

                      <p className="text-sm text-gray-400">
                        📍 Lines {source.start_line} – {source.end_line}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}