import UrlScanner from "./components/UrlScanner";

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col items-center justify-center">
      <h1 className="text-4xl font-bold mb-2">PhishGuard AI</h1>
      <p className="text-slate-400 mb-10">Detect phishing URLs using AI</p>
      <UrlScanner />
    </div>
  );
}

export default App;