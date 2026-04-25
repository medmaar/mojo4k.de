import { useState } from 'react'

const faqs = [
  {
    q: 'Was ist IPTV?',
    a: 'IPTV (Internet Protocol Television) ist eine Methode zur Übertragung von Fernsehprogrammen über das Internet. Im Gegensatz zu herkömmlichem Kabel- oder Satellitenfernsehen werden die Inhalte als Datenpakete über eine Internetverbindung gestreamt.'
  },
  {
    q: 'Welche Geräte werden unterstützt?',
    a: 'Unser Service ist kompatibel mit fast allen Geräten: Smart TVs (Samsung, LG, Sony), Android-Geräte, iPhones/iPads, Windows- und Mac-Computer, Amazon Firestick, MAG-Boxen, NVIDIA Shield und viele mehr.'
  },
  {
    q: 'Wie schnell ist die Aktivierung?',
    a: 'Nach deiner Bestellung wird dein Konto sofort aktiviert. Du erhältst deine Zugangsdaten innerhalb weniger Minuten per E-Mail.'
  },
  {
    q: 'Gibt es einen kostenlosen Test?',
    a: 'Ja! Wir bieten einen 24-Stunden kostenlosen Testaccount an. Schreibe uns einfach über WhatsApp oder Telegram und wir richten deinen Testzugang ein.'
  },
  {
    q: 'Welche Internetgeschwindigkeit benötige ich?',
    a: 'Für SD-Qualität reichen 5 Mbit/s, für Full HD empfehlen wir 15 Mbit/s und für 4K Ultra HD mindestens 25 Mbit/s. Eine stabile Verbindung ist wichtiger als hohe Geschwindigkeit.'
  },
  {
    q: 'Kann ich auf mehreren Geräten gleichzeitig schauen?',
    a: 'Ja, je nach gewähltem Paket kannst du auf 1 bis 4 Geräten gleichzeitig streamen. Für weitere Verbindungen kontaktiere uns für ein individuelles Angebot.'
  },
  {
    q: 'Gibt es eine Geld-zurück-Garantie?',
    a: 'Wir bieten keinen automatischen Erstattungsservice, da wir einen kostenlosen Test anbieten. Wir empfehlen, erst den Testaccount zu nutzen, um die Qualität zu prüfen.'
  },
]

function FAQItem({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false)
  return (
    <div className="border border-white/10 rounded-xl overflow-hidden">
      <button
        onClick={() => setOpen(!open)}
        className="w-full flex items-center justify-between p-5 text-left bg-white/5 hover:bg-white/10 transition-colors"
      >
        <span className="font-semibold text-white pr-4">{q}</span>
        <svg
          width="20" height="20" fill="none" stroke="#FF6B00" strokeWidth="2" viewBox="0 0 24 24"
          className={`flex-shrink-0 transition-transform ${open ? 'rotate-180' : ''}`}
        >
          <path d="M6 9l6 6 6-6"/>
        </svg>
      </button>
      {open && (
        <div className="px-5 py-4 text-gray-400 leading-relaxed bg-black/20 text-sm">
          {a}
        </div>
      )}
    </div>
  )
}

export default function FAQ() {
  return (
    <section id="faq" className="py-24 bg-black/30">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <span className="text-brand-orange text-sm font-semibold uppercase tracking-wider">Häufige Fragen</span>
          <h2 className="text-4xl md:text-5xl font-black mt-3 mb-4">
            FAQ
          </h2>
          <p className="text-gray-400 text-lg">
            Noch Fragen? Hier findest du Antworten auf die häufigsten Fragen.
          </p>
        </div>
        <div className="space-y-3">
          {faqs.map((faq) => (
            <FAQItem key={faq.q} q={faq.q} a={faq.a} />
          ))}
        </div>
      </div>
    </section>
  )
}
