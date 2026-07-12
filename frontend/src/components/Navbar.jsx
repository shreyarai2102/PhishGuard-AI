function Navbar() {
  return (
    <nav className="flex items-center justify-between px-8 py-5 border-b border-slate-800">
      <h1 className="text-3xl font-bold text-cyan-400">
        🛡️ PhishGuard AI
      </h1>

      <button className="rounded-lg border border-cyan-400 px-4 py-2 text-cyan-400 hover:bg-cyan-400 hover:text-black transition">
        GitHub
      </button>
    </nav>
  );
}

export default Navbar;