function ResultCard({ result }) {
  if (!result) return null;

  const safe = result.prediction === "SAFE";

  return (
    <div className="max-w-3xl mx-auto mt-10">
      <div className="rounded-2xl bg-slate-900 p-8 shadow-xl">

        <h2
          className={`text-3xl font-bold ${
            safe ? "text-green-400" : "text-red-400"
          }`}
        >
          {safe ? "🟢 SAFE" : "🔴 PHISHING"}
        </h2>

        <p className="mt-4 text-slate-300">
          URL: {result.url}
        </p>

        <p className="mt-2 text-xl">
          Confidence: <span className="font-bold">{result.confidence}%</span>
        </p>

      </div>
    </div>
  );
}

export default ResultCard;