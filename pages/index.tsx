import Head from 'next/head'
import Navbar from '../components/Navbar'
import Hero from '../components/Hero'
import Features from '../components/Features'
import Channels from '../components/Channels'
import Pricing from '../components/Pricing'
import FAQ from '../components/FAQ'
import Contact from '../components/Contact'
import Footer from '../components/Footer'

export default function Home() {
  return (
    <>
      <Head>
        <title>IPTVV.DE – Premium IPTV Deutschland | 20.000+ Sender in 4K</title>
        <meta name="description" content="Deutschlands bester IPTV-Dienst mit über 20.000 Live-Sendern, 50.000+ Filmen & Serien in 4K Ultra HD. Jetzt kostenlos testen!" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta property="og:title" content="IPTVV.DE – Premium IPTV Deutschland" />
        <meta property="og:description" content="20.000+ Sender, 4K Qualität, 99.9% Betriebszeit. Jetzt kostenlos testen!" />
        <meta property="og:url" content="https://iptvv.de" />
        <meta name="robots" content="index, follow" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar />
      <main>
        <Hero />
        <Features />
        <Channels />
        <Pricing />
        <FAQ />
        <Contact />
      </main>
      <Footer />
    </>
  )
}
