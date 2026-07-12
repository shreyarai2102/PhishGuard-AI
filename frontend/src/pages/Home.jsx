import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UrlScanner from "../components/UrlScanner";

function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />
      <Hero />
      <UrlScanner />
    </div>
  );
}

export default Home;