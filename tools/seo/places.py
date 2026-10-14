"""Place pages: slug -> (place name, Bundesland or country). Slugs are the final (ASCII) slugs."""

_RAW = """
NW: aachen=Aachen ahlen=Ahlen attendorn=Attendorn bad-salzuflen=Bad Salzuflen beckum=Beckum bergheim=Bergheim
NW: bergisch-gladbach=Bergisch Gladbach bielefeld=Bielefeld bocholt=Bocholt bochum=Bochum bonn=Bonn bottrop=Bottrop
NW: castrop-rauxel=Castrop-Rauxel coesfeld=Coesfeld detmold=Detmold dinslaken=Dinslaken dorsten=Dorsten dortmund=Dortmund
NW: duesseldorf=Düsseldorf duisburg=Duisburg essen=Essen euskirchen=Euskirchen gelsenkirchen=Gelsenkirchen gladbeck=Gladbeck
NW: gronau=Gronau gummersbach=Gummersbach guetersloh=Gütersloh hagen=Hagen halver=Halver hamm=Hamm hattingen=Hattingen
NW: hemer=Hemer herford=Herford herne=Herne ibbenbueren=Ibbenbüren iserlohn=Iserlohn kaarst=Kaarst kamp-lintfort=Kamp-Lintfort
NW: kerpen=Kerpen koeln=Köln krefeld=Krefeld langenfeld=Langenfeld leverkusen=Leverkusen lippstadt=Lippstadt
NW: luedenscheid=Lüdenscheid altena=Altena luenen=Lünen marl=Marl meerbusch=Meerbusch menden=Menden meschede=Meschede minden=Minden
NW: moenchengladbach=Mönchengladbach moers=Moers muelheim=Mülheim an der Ruhr muenster=Münster neukirchen-vluyn=Neukirchen-Vluyn
NW: neuss=Neuss oberhausen=Oberhausen olpe=Olpe paderborn=Paderborn plettenberg=Plettenberg pulheim=Pulheim ratingen=Ratingen
NW: recklinghausen=Recklinghausen remscheid=Remscheid rheine=Rheine schwelm=Schwelm siegen=Siegen solingen=Solingen
NW: sprockhoevel=Sprockhövel steinfurt=Steinfurt troisdorf=Troisdorf unna=Unna velbert=Velbert viersen=Viersen warendorf=Warendorf
NW: werne=Werne wesel=Wesel wetter-ruhr=Wetter (Ruhr) witten=Witten wuerselen=Würselen wuppertal=Wuppertal
BW: aalen=Aalen backnang=Backnang boeblingen=Böblingen esslingen=Esslingen am Neckar freiburg=Freiburg im Breisgau
BW: friedrichshafen=Friedrichshafen goeppingen=Göppingen heidelberg=Heidelberg heidenheim=Heidenheim heilbronn=Heilbronn
BW: karlsruhe=Karlsruhe kirchheim=Kirchheim unter Teck konstanz=Konstanz leonberg=Leonberg loerrach=Lörrach mannheim=Mannheim
BW: nuertingen=Nürtingen pforzheim=Pforzheim radolfzell=Radolfzell rastatt=Rastatt reutlingen=Reutlingen rottenburg=Rottenburg am Neckar
BW: schorndorf=Schorndorf schwaebisch-gmuend=Schwäbisch Gmünd schwaebisch-hall=Schwäbisch Hall sindelfingen=Sindelfingen
BW: singen=Singen stuttgart=Stuttgart tuebingen=Tübingen ueberlingen=Überlingen ulm=Ulm villingen=Villingen-Schwenningen waiblingen=Waiblingen
BY: amberg=Amberg ansbach=Ansbach aschaffenburg=Aschaffenburg augsburg=Augsburg bamberg=Bamberg bayreuth=Bayreuth coburg=Coburg
BY: dachau=Dachau erding=Erding erlangen=Erlangen freising=Freising fuerth=Fürth fuerstenfeldbruck=Fürstenfeldbruck germering=Germering
BY: gunzenhausen=Gunzenhausen hof=Hof ingolstadt=Ingolstadt kaufbeuren=Kaufbeuren kempten=Kempten landshut=Landshut memmingen=Memmingen
BY: muenchen=München neumarkt=Neumarkt in der Oberpfalz nuernberg=Nürnberg olching=Olching passau=Passau regensburg=Regensburg
BY: rosenheim=Rosenheim roth=Roth schwabach=Schwabach schweinfurt=Schweinfurt straubing=Straubing unterschleissheim=Unterschleißheim
BY: vaterstetten=Vaterstetten weiden=Weiden in der Oberpfalz wuerzburg=Würzburg
HE: bad-homburg=Bad Homburg darmstadt=Darmstadt dreieich=Dreieich frankfurt=Frankfurt am Main fulda=Fulda giessen=Gießen hanau=Hanau
HE: hofheim=Hofheim am Taunus kassel=Kassel langen=Langen maintal=Maintal marburg=Marburg offenbach=Offenbach am Main
HE: ruesselsheim=Rüsselsheim wiesbaden=Wiesbaden
NI: aurich=Aurich braunschweig=Braunschweig buxtehude=Buxtehude celle=Celle delmenhorst=Delmenhorst emden=Emden garbsen=Garbsen
NI: goettingen=Göttingen hameln=Hameln hannover=Hannover hildesheim=Hildesheim lingen=Lingen lueneburg=Lüneburg meppen=Meppen
NI: nienburg=Nienburg nordhorn=Nordhorn oldenburg=Oldenburg osnabrueck=Osnabrück papenburg=Papenburg salzgitter=Salzgitter
NI: stade=Stade wilhelmshaven=Wilhelmshaven wolfenbuettel=Wolfenbüttel wolfsburg=Wolfsburg
SN: bautzen=Bautzen chemnitz=Chemnitz dresden=Dresden pirna=Pirna freiberg-sachsen=Freiberg glauchau=Glauchau goerlitz=Görlitz
SN: leipzig=Leipzig meissen=Meißen plauen=Plauen riesa=Riesa werdau=Werdau zwickau=Zwickau
TH: eisenach=Eisenach erfurt=Erfurt gera=Gera gotha=Gotha jena=Jena muehlhausen=Mühlhausen nordhausen=Nordhausen rudolstadt=Rudolstadt
TH: saalfeld=Saalfeld sonneberg=Sonneberg weimar=Weimar
RP: andernach=Andernach bad-kreuznach=Bad Kreuznach idar-oberstein=Idar-Oberstein kaiserslautern=Kaiserslautern koblenz=Koblenz
RP: ludwigshafen=Ludwigshafen am Rhein mainz=Mainz neuwied=Neuwied trier=Trier worms=Worms
SH: elmshorn=Elmshorn flensburg=Flensburg heide=Heide husum=Husum kiel=Kiel luebeck=Lübeck neumuenster=Neumünster
SH: norderstedt=Norderstedt rendsburg=Rendsburg
MV: greifswald=Greifswald neubrandenburg=Neubrandenburg rostock=Rostock schwerin=Schwerin stralsund=Stralsund wismar=Wismar
BB: bernau=Bernau bei Berlin cottbus=Cottbus eberswalde=Eberswalde oranienburg=Oranienburg potsdam=Potsdam strausberg=Strausberg
ST: halle=Halle (Saale) magdeburg=Magdeburg
SL: neunkirchen-saar=Neunkirchen saarbruecken=Saarbrücken saarlouis=Saarlouis st-ingbert=St. Ingbert voelklingen=Völklingen
HB: bremerhaven=Bremerhaven
CH: bern=Bern genf=Genf lausanne=Lausanne zuerich=Zürich freiburg-schweiz=Freiburg im Üechtland
AT: graz=Graz innsbruck=Innsbruck klagenfurt=Klagenfurt linz=Linz salzburg=Salzburg wien=Wien
"""

STATES = {
    'NW': 'Nordrhein-Westfalen', 'BW': 'Baden-Württemberg', 'BY': 'Bayern', 'HE': 'Hessen', 'NI': 'Niedersachsen',
    'SN': 'Sachsen', 'TH': 'Thüringen', 'RP': 'Rheinland-Pfalz', 'SH': 'Schleswig-Holstein',
    'MV': 'Mecklenburg-Vorpommern', 'BB': 'Brandenburg', 'ST': 'Sachsen-Anhalt', 'SL': 'Saarland', 'HB': 'Bremen',
    'BE': 'Berlin', 'HH': 'Hamburg', 'CH': 'Schweiz', 'AT': 'Österreich',
}

# Bundesland (and country) hub page for each state code
STATE_HUB = {
    'NW': 'iptv-nrw', 'BW': 'iptv-badenwuerttemberg', 'BY': 'iptv-bayern', 'HE': 'iptv-hessen', 'NI': 'iptv-niedersachsen',
    'SN': 'iptv-sachsen', 'TH': 'iptv-thueringen', 'RP': 'iptv-rheinland-pfalz', 'SH': 'iptv-schleswig-holstein',
    'MV': 'iptv-mecklenburg', 'BB': 'iptv-brandenburg', 'ST': 'iptv-sachsen-anhalt', 'SL': 'iptv-saarland', 'HB': 'iptv-bremen',
    'BE': 'iptv-berlin', 'HH': 'iptv-hamburg', 'CH': 'iptv-schweiz', 'AT': 'iptv-oesterreich',
}

# city-states: the city page is the state page
CITY_STATES = {'iptv-berlin': ('Berlin', 'BE'), 'iptv-hamburg': ('Hamburg', 'HH'), 'iptv-bremen': ('Bremen', 'HB')}

# state / region pages: slug -> (name, code or None)
REGIONS = {
    'iptv-nrw': ('Nordrhein-Westfalen', 'NW'), 'iptv-badenwuerttemberg': ('Baden-Württemberg', 'BW'),
    'iptv-bayern': ('Bayern', 'BY'), 'iptv-hessen': ('Hessen', 'HE'), 'iptv-niedersachsen': ('Niedersachsen', 'NI'),
    'iptv-sachsen': ('Sachsen', 'SN'), 'iptv-thueringen': ('Thüringen', 'TH'),
    'iptv-rheinland-pfalz': ('Rheinland-Pfalz', 'RP'), 'iptv-schleswig-holstein': ('Schleswig-Holstein', 'SH'),
    'iptv-mecklenburg': ('Mecklenburg-Vorpommern', 'MV'), 'iptv-brandenburg': ('Brandenburg', 'BB'),
    'iptv-sachsen-anhalt': ('Sachsen-Anhalt', 'ST'), 'iptv-saarland': ('Saarland', 'SL'),
    'iptv-ruhrgebiet': ('Ruhrgebiet', 'NW'), 'iptv-rhein-main': ('Rhein-Main-Gebiet', 'HE'),
}

PLACES = {}
for line in _RAW.strip().split('\n'):
    code, rest = line.split(':', 1)
    for tok in rest.strip().split(' '):
        pass
    # names contain spaces: split on " slug=" boundaries
    import re as _re
    for slug, name in _re.findall(r'([a-z0-9-]+)=(.+?)(?= [a-z0-9-]+=|$)', rest.strip()):
        PLACES['iptv-' + slug] = (name, code)
for k, v in CITY_STATES.items():
    PLACES[k] = v
