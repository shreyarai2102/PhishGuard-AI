import { useState } from "react";
import api from "../services/api";

function Home() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const checkURL = async () => {
    if (!url) {
      setResult("Please enter a URL");
      return;
    }

    try {
      setLoading(true);
      setResult("");

      const response = await api.post("/check", {
        url: url,
      });

      setResult(
        typeof response.data === "string"
          ? response.data
          : JSON.stringify(response.data)
      );

    } catch (error) {
      console.log(error);
      setResult("Error connecting to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ 
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center"
    }}>

      <h1>🛡️ PhishGuard AI</h1>

      <p>
        Detect phishing URLs using AI
      </p>

      <input
        type="text"
        placeholder="Enter URL to check"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{
          width: "400px",
          padding: "12px",
          margin: "20px"
        }}
      />

      <button
        onClick={checkURL}
        disabled={loading}
        style={{
          padding: "12px 25px",
          cursor: "pointer"
        }}
      >
        {loading ? "Checking..." : "Check URL"}
      </button>


      {result && (
        <div style={{
          marginTop: "30px",
          padding: "20px",
          border: "1px solid gray",
          borderRadius: "10px"
        }}>
          <h3>Result:</h3>
          <p>{result}</p>
        </div>
      )}

    </div>
  );
}

export default Home;