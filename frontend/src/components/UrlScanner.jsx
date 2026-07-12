import { useState } from "react";
import api from "../services/api";
import ResultCard from "./ResultCard";

function UrlScanner() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function scanUrl() {
    if (!url) return;

    setLoading(true);

    try {
      const response = await api.post("/api/check", {
        url,
      });

      setResult(response.data);
    } catch (err) {
      alert("Backend not running!");
      console.error(err);
    }

    setLoading(false);
  }

  return (
    <div className="max-w-3xl mx-auto px-6">

      <div className="bg-slate-900 rounded-2xl p-8">

        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          className="w-full rounded-xl bg-slate-800 p-4 outline-none"
        />

        <button
          onClick={scanUrl}
          className="mt-6 w-full rounded-xl bg-cyan-500 py-4 font-bold hover:bg-cyan-600"
        >
          {loading ? "Scanning..." : "Scan URL"}
        </button>

      </div>

      <ResultCard result={result} />

    </div>
  );
}

export default UrlScanner;