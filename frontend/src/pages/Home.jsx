import { useState } from "react";
import api from "../services/api";

function Home() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkURL = async () => {
    if (!url.trim()) {
      setResult({
        error: "Please enter a URL",
      });
      return;
    }

    try {
      setLoading(true);
      setResult(null);

      const response = await api.post("/check", {
        url: url.trim(),
      });

      setResult(response.data);

    } catch (error) {
      console.log(error);

      setResult({
        error: "Error connecting to backend",
      });

    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <h1>PhishScan</h1>

      <p>
        Detect phishing URLs using AI
      </p>

      <input
        type="text"
        placeholder="Enter URL to check"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            checkURL();
          }
        }}
        style={{
          width: "400px",
          padding: "12px",
          margin: "20px",
        }}
      />

      <button
        onClick={checkURL}
        disabled={loading}
        style={{
          padding: "12px 25px",
          cursor: loading ? "not-allowed" : "pointer",
        }}
      >
        {loading ? "Checking..." : "Check URL"}
      </button>

      {result && (
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            width: "400px",
            border: "1px solid gray",
            borderRadius: "10px",
          }}
        >
          {result.error ? (
            <p>{result.error}</p>
          ) : (
            <>
              <h3>Scan Result</h3>

              <p>
                <strong>URL:</strong> {result.url}
              </p>

              <p>
                <strong>Prediction:</strong>{" "}
                {result.prediction}
              </p>

              <p>
                <strong>Confidence:</strong>{" "}
                {result.confidence}%
              </p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default Home;