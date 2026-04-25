import { useState } from 'react'
import Link from 'next/link'

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-black/80 backdrop-blur-md border-b border-white/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg pricing-popular flex items-center justify-center">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="white">
                <path d="M21 3H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h5v2H6v2h12v-2h-2v-2h5c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 14H3V5h18v12z"/>
              </svg>
            </div>
            <span className="text-xl font-bold gradient-text">IPTVV.DE</span>
          </Link>

          {/* Desktop Nav */}
          <div className="hidden md:flex items-center gap-8">
            <a href="#features" className="text-gray-400 hover:text-white text-sm transition-colors">Funktionen</a>
            <a href="#pricing" className="text-gray-400 hover:text-white text-sm transition-colors">Preise</a>
            <a href="#channels" className="text-gray-400 hover:text-white text-sm transition-colors">Sender</a>
            <a href="#faq" className="text-gray-400 hover:text-white text-sm transition-colors">FAQ</a>
            <a href="#contact" className="text-gray-400 hover:text-white text-sm transition-colors">Kontakt</a>
          </div>

          {/* CTA */}
          <div className="hidden md:flex items-center gap-3">
            <a href="#pricing" className="bg-brand-orange hover:bg-brand-orange-dark text-white text-sm font-semibold px-5 py-2 rounded-lg transition-all glow-orange">
              Jetzt starten
            </a>
          </div>

          {/* Mobile menu btn */}
          <button onClick={() => setMenuOpen(!menuOpen)} className="md:hidden text-white p-2">
            <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
              {menuOpen
                ? <path d="M6 18L18 6M6 6l12 12"/>
                : <path d="M4 6h16M4 12h16M4 18h16"/>}
            </svg>
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div className="md:hidden bg-black/95 border-t border-white/5 px-4 py-4 flex flex-col gap-4">
          <a href="#features" onClick={() => setMenuOpen(false)} className="text-gray-300 hover:text-white">Funktionen</a>
          <a href="#pricing" onClick={() => setMenuOpen(false)} className="text-gray-300 hover:text-white">Preise</a>
          <a href="#channels" onClick={() => setMenuOpen(false)} className="text-gray-300 hover:text-white">Sender</a>
          <a href="#faq" onClick={() => setMenuOpen(false)} className="text-gray-300 hover:text-white">FAQ</a>
          <a href="#contact" onClick={() => setMenuOpen(false)} className="text-gray-300 hover:text-white">Kontakt</a>
          <a href="#pricing" className="bg-brand-orange text-white font-semibold px-5 py-2 rounded-lg text-center">Jetzt starten</a>
        </div>
      )}
    </nav>
  )
}
