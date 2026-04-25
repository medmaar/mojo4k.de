export default function Footer() {
  return (
    <footer className="bg-black border-t border-white/5 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
          {/* Brand */}
          <div className="md:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-8 h-8 rounded-lg pricing-popular flex items-center justify-center">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="white">
                  <path d="M21 3H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h5v2H6v2h12v-2h-2v-2h5c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 14H3V5h18v12z"/>
                </svg>
              </div>
              <span className="text-xl font-bold gradient-text">IPTVV.DE</span>
            </div>
            <p className="text-gray-400 text-sm leading-relaxed max-w-xs">
              Deutschlands Premium IPTV-Dienst mit über 20.000 Sendern, 
              50.000+ VOD-Titeln und 4K-Qualität für das beste Streaming-Erlebnis.
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="font-semibold text-white mb-4">Service</h4>
            <ul className="space-y-2 text-sm text-gray-400">
              <li><a href="#features" className="hover:text-white transition-colors">Funktionen</a></li>
              <li><a href="#pricing" className="hover:text-white transition-colors">Preise</a></li>
              <li><a href="#channels" className="hover:text-white transition-colors">Sender</a></li>
              <li><a href="#faq" className="hover:text-white transition-colors">FAQ</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Rechtliches</h4>
            <ul className="space-y-2 text-sm text-gray-400">
              <li><a href="/impressum" className="hover:text-white transition-colors">Impressum</a></li>
              <li><a href="/datenschutz" className="hover:text-white transition-colors">Datenschutz</a></li>
              <li><a href="/agb" className="hover:text-white transition-colors">AGB</a></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-white/5 pt-6 flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="text-gray-500 text-sm">
            © {new Date().getFullYear()} IPTVV.DE · Alle Rechte vorbehalten
          </p>
          <p className="text-gray-600 text-xs">
            ⚠️ Nur für legale Inhalte. Nutzung auf eigene Verantwortung.
          </p>
        </div>
      </div>
    </footer>
  )
}
