# Bygger /ny/ (svenska) och /ny/en/ (engelska). Kör: python3 ny/_bygg.py
# Filer som börjar med _ publiceras inte av GitHub Pages.
import os, html
NY = os.path.dirname(os.path.abspath(__file__))
SITE = "https://valvet.sluggan.com/ny/"
MAIL = "studionvalvet@gmail.com"
LANGS = ("sv", "en")

# adresser per språk, relativt /ny/
PATHS = {
  "sv": dict(home="", work="vara-jobb/", job="jobb/{}/", clients="kunder/", about="om-oss/", contact="kontakt/"),
  "en": dict(home="en/", work="en/work/", job="en/work/{}/", clients="en/clients/", about="en/about/", contact="en/contact/"),
}

T = {
  "sv": dict(nav=("Våra jobb", "Kunder", "Om oss", "Kontakt"), client="Kund", scope="Uppdrag", see="Se jobbet", next="Nästa jobb",
             brief="Brief", did="Vårt arbete", what="Det här gör vi", home_alt="StudionValvet – till startsidan",
             hero="Från idé till<br>färdig produktion", book="Boka en kreativ konsultation:", subject="Kreativ%20konsultation",
             ask="Blir ni nästa?<br>Hör av er →", country="", map="Karta till Gamla Riksbankshuset"),
  "en": dict(nav=("Our work", "Clients", "About", "Contact"), client="Client", scope="Scope", see="See the project", next="Next project",
             brief="Brief", did="What we did", what="What we do", home_alt="StudionValvet – home",
             hero="From idea to<br>finished production", book="Book a creative consultation:", subject="Creative%20consultation",
             ask="Could you be next?<br>Get in touch →", country="<br>Sweden", map="Map to Gamla Riksbankshuset"),
}

PAGES = {
  "home": {"sv": ("StudionValvet – film, content, design och musik i Uppsala",
                  "Vi hjälper varumärken, artister och företag med branding, content och marknadsföring – från idé till färdig produktion. Studio i Gamla Riksbankshuset, Uppsala."),
           "en": ("StudionValvet – film, content, design and music in Uppsala",
                  "We help brands, artists and companies with branding, content and marketing – from idea to finished production. Studio in Gamla Riksbankshuset, Uppsala.")},
  "work": {"sv": ("Våra jobb – StudionValvet", "Ett urval av det vi gjort: film, content, branding, foto och musik."),
           "en": ("Our work – StudionValvet", "A selection of our work: film, content, branding, photography and music.")},
  "clients": {"sv": ("Kunder – StudionValvet", "Varumärken, artister och företag vi arbetat med."),
              "en": ("Clients – StudionValvet", "Brands, artists and companies we've worked with.")},
  "about": {"sv": ("Om oss – StudionValvet", "Kreativ partner för branding, content och marknadsföring, med studio i Gamla Riksbankshuset i Uppsala."),
            "en": ("About – StudionValvet", "A creative partner for branding, content and marketing, with a studio in Gamla Riksbankshuset in Uppsala.")},
  "contact": {"sv": ("Kontakt – StudionValvet", "Boka en kreativ konsultation. Studio i Gamla Riksbankshuset, Kungsängsgatan 17–19, Uppsala."),
              "en": ("Contact – StudionValvet", "Book a creative consultation. Studio in Gamla Riksbankshuset, Kungsängsgatan 17–19, Uppsala.")},
}

def L(sv, en): return {"sv": sv, "en": en}

JOBS = [
  dict(slug="fraseriet", title="Fraseriet", kund="Fraseriet",
       uppdrag=L("Social media, reklamfilm, branding", "Social media, commercial, branding"),
       hero="img/kunder/fraseriet-bg.jpg",
       teaser=L("Vi tog över Fraseriets sociala medier, moderniserade uttrycket och skapade en röd tråd med mer rörligt och strategiskt innehåll.",
                "We took over Fraseriet's social media, modernized the look and created a common thread with more video and more strategic content."),
       brief=L(["När StudionValvet tog över Fraseriets sociala medier hade kontot ca 760 följare och ett svårutläst flöde. Företaget eftersökte tydlig visuell riktning."],
               ["When StudionValvet took over Fraseriet's social media, the account had around 760 followers and a feed that was hard to read. The company was looking for a clear visual direction."]),
       did=L(["Målet var att modernisera uttrycket, skapa en röd tråd och öka engagemanget genom mer rörligt och strategiskt innehåll.",
              "För att visualisera det Fraseriet har att erbjuda gästerna såg vi vikten i att presentera produkterna på ett smakfullt och levande vis. Genom att fokusera på färg, textur och grafik ville vi representera Fraseriets konsekventa leverans i smaker och känsla.",
              "Arbetet med Fraseriet är ett pågående uppdrag och vi arbetar aktivt tillsammans med kunden för att öka synligheten."],
             ["The goal was to modernize the look, create a common thread and increase engagement through more video and more strategic content.",
              "To show what Fraseriet has to offer its guests, we wanted to present the food in a tasteful and vivid way. By focusing on color, texture and graphics, we set out to capture how consistently Fraseriet delivers on flavor and feel.",
              "Fraseriet is an ongoing assignment, and we work closely with the client to keep growing their visibility."]),
       media=[("video", ["fraseriet-reklamfilm"]),
              ("tallvideo", ["fraseriet-social-1", "fraseriet-social-2", "fraseriet-social-3", "fraseriet-social-4"]),
              ("sq", [("img/kunder/fraseriet-orange-mayhem.png", "Orange Mayhem", "dark"),
                      ("img/kunder/fraseriet-pask.jpg", L("Öppettider påsken 2026", "Easter opening hours 2026"), ""),
                      ("img/kunder/fraseriet-aggjakt.jpg", L("Äggjakt Uppsala", "Easter egg hunt in Uppsala"), "")]),
              ("img", [("img/kunder/fraseriet-orange-mayhem-foto.jpg", "Orange Mayhem"), ("img/kunder/fraseriet-pollo-loco.jpg", "Pollo Loco"),
                       ("img/kunder/fraseriet-bangkok-banger.jpg", "Bangkok Banger"), ("img/kunder/fraseriet-funky-falafel.jpg", "Funky Falafel 2.0")])]),
  dict(slug="topel-beats", title="Topel Beats", kund="Topel Beats",
       uppdrag=L("Branding, logotypfamilj, merch", "Branding, logo family, merch"),
       hero="img/kunder/topel-bg.jpg",
       teaser=L("En sammanhållen logotypfamilj för en artist som ser sig själv som en utomjording på uppdrag att sprida sin musik inom hiphop-scenen.",
                "A cohesive logo family for an artist who sees himself as an alien on a mission to spread his music through the hip-hop scene."),
       brief=L(["Projektet började som en förfining av ett befintligt varumärke. Artisten, som är en del av vårt team, ser sig själv som en utomjording på ett uppdrag att sprida sin musik inom hiphop-scenen."],
               ["The project started as a refinement of an existing brand. The artist, who is part of our team, sees himself as an alien on a mission to spread his music through the hip-hop scene."]),
       did=L(["Genom att lyssna på hans idéer och musik översatte vi visionen till en sammanhållen logotypfamilj som tydliggör hans identitet och bevarar karaktären bakom uttrycket."],
             ["By listening to his ideas and his music, we translated the vision into a cohesive logo family that makes his identity clear while keeping the character behind it."]),
       media=[("sq", [("img/kunder/topel-logo-1.png", L("Topel Beats logotyp", "Topel Beats logo"), ""),
                      ("img/kunder/topel-logo-2.png", L("Topel Beats logotyp, grön", "Topel Beats logo, green"), "")]),
              ("sq", [("img/kunder/topel-logo-3.png", L("Topel Beats logotyp, röd", "Topel Beats logo, red"), ""),
                      ("img/kunder/topel-ufo.png", L("Topel Beats ufo-symbol", "Topel Beats UFO symbol"), "")]),
              ("img", [("img/kunder/topel-merch.jpg", L("Hoodies med Topel Beats logotyp", "Hoodies with the Topel Beats logo"))])]),
  dict(slug="darkness-shall-pass", title="Darkness Shall Pass", kund="Viktor Andersson",
       uppdrag=L("Hemsida, dokumentation", "Website, documentation"),
       hero="img/kunder/viktor-bg.jpg",
       teaser=L("Studiematerial och dokumentation av ett kulturarrangemang om psykisk hälsa, kopplat till bokprojektet Darkness Shall Pass.",
                "Study material and documentation of a cultural event about mental health, connected to the book project Darkness Shall Pass."),
       brief=L(["Ta fram studiematerial och dokumentera ett kulturarrangemang om psykisk hälsa, i samverkan med Etnograferna, för vidare kommunikation kopplat till arrangemanget och bokprojektet Darkness Shall Pass."],
               ["Produce study material and document a cultural event about mental health, in collaboration with Etnograferna, for further communication around the event and the book project Darkness Shall Pass."]),
       did=L(["Vi producerade studiematerialet i form av en hemsida och dokumenterade arrangemanget. Materialet följer låtarna en efter en.",
              '<a class="u" href="http://darknessshallpass.my.canva.site/darkness-shall-pass-viktor-andersson" target="_blank" rel="noopener">Besök projektet i sin helhet →</a>'],
             ["We produced the study material as a website and documented the event. The material follows the songs one by one.",
              '<a class="u" href="http://darknessshallpass.my.canva.site/darkness-shall-pass-viktor-andersson" target="_blank" rel="noopener">See the full project →</a>']),
       media=[("img", [("img/kunder/viktor-banner.png", "Viktor Andersson – Darkness Shall Pass")]),
              ("img", [("img/kunder/viktor-sida-4.png", L("Del 1: Introduktion", "Part 1: Introduction")),
                       ("img/kunder/viktor-sida-5.png", L("Låten P.P", "The song P.P"))]),
              ("img", [("img/kunder/viktor-sida-1.png", L("Låtarna Maniac, Fantasy och Wake up", "The songs Maniac, Fantasy and Wake up")),
                       ("img/kunder/viktor-sida-2.png", L("Låtarna I can't run och Honest mistake", "The songs I can't run and Honest mistake")),
                       ("img/kunder/viktor-sida-3.png", L("Låtarna Divine purpose och Darkness shall pass", "The songs Divine purpose and Darkness shall pass"))])]),
  dict(slug="cobra-combat", title="Cobra Combat", kund="Cobra Combat",
       uppdrag=L("Logotyp, varumärkesprofil, social media", "Logo, brand identity, social media"),
       hero="img/kunder/cobra-bg.jpg",
       teaser=L("Från uppstart formar vi Cobra Combats visuella identitet – logotyp, varumärkesprofil och grunden för deras närvaro i sociala medier.",
                "From day one, we're shaping Cobra Combat's visual identity – logo, brand identity and the foundation of their social media presence."),
       brief=L(["Cobra Combat är nystartat inom personal training, group training, fitness och martial arts, och behövde ett visuellt uttryck från grunden."],
               ["Cobra Combat is a new business in personal training, group training, fitness and martial arts, and needed a visual identity built from the ground up."]),
       did=L(["Pågående arbete där vi från uppstart formar Cobra Combats visuella identitet. Vi utvecklar logotyp, varumärkesprofil och riktlinjer för uttrycket, samtidigt som vi lägger grunden för deras närvaro i sociala medier."],
             ["An ongoing project where we're shaping Cobra Combat's visual identity from the start. We're developing the logo, brand identity and guidelines, while laying the foundation for their presence on social media."]),
       media=[("sq", [("img/kunder/cobra-emblem.png", L("Cobra Combats emblem", "Cobra Combat emblem"), ""),
                      ("img/kund-cobra.png", L("Cobra Combats logotyp", "Cobra Combat logo"), "")])]),
  dict(slug="kings-of-kong", title="Kings of Kong", kund="Kings of Kong, Topel Beats",
       uppdrag=L("Musik- och ljudproduktion", "Music and sound production"),
       hero="video/musik-video-1.jpg",
       teaser=L("Inhouse-produktioner där ljudet skräddarsys efter situationen du som artist eller ni som verksamhet befinner er i.",
                "In-house productions where the sound is tailored to where you are as an artist or a business."),
       brief=L(["Musik och ljud som förstärker berättelser, varumärken och helhetsupplevelser."],
               ["Music and sound that strengthen stories, brands and experiences."]),
       did=L(["Med inhouse-produktioner från bl.a. Topel Beats och Kings of Kong finns det hos oss utrymme att skräddarsy ljudproduktionen efter situationen du som artist eller ni som verksamhet befinner er i – med full kreativ kontroll från idé till färdig produktion.",
              '<a class="u" href="https://open.spotify.com/artist/1QbrSZbx4FD7Up6G8raE9Q" target="_blank" rel="noopener">Spotify →</a>&nbsp;&nbsp; <a class="u" href="https://www.beatstars.com/topelbeats" target="_blank" rel="noopener">Topel Beats på BeatStars →</a>'],
             ["With in-house productions from Topel Beats and Kings of Kong, among others, we have room to tailor the sound to where you are as an artist or a business – with full creative control from idea to finished production.",
              '<a class="u" href="https://open.spotify.com/artist/1QbrSZbx4FD7Up6G8raE9Q" target="_blank" rel="noopener">Spotify →</a>&nbsp;&nbsp; <a class="u" href="https://www.beatstars.com/topelbeats" target="_blank" rel="noopener">Topel Beats on BeatStars →</a>']),
       media=[("spotify", L("Kings of Kong på Spotify", "Kings of Kong on Spotify")),
              ("video", ["musik-video-1", "musik-video-2"]),
              ("raw", '<p class="cap">Video: Simonapaulina</p>')]),
  dict(slug=L("foto-i-studion", "studio-photography"), title=L("Foto i studion", "Studio photography"), kund=L("Flera kunder", "Several clients"),
       uppdrag=L("Produktfoto, produktvideo, miljöbilder", "Product photos, product video, location shots"),
       hero="img/tjanster/foto-miljo-ljus.jpg",
       teaser=L("Allt från produktfotografering till miljöbilder och annat visuellt material som förmedlar rätt känsla och lyfter kommunikationen.",
                "Everything from product photography to location shots and other visual material that sets the right mood and lifts your communication."),
       brief=L(["Bilder och visuellt material som förmedlar rätt känsla och lyfter kommunikationen."],
               ["Images and visual material that convey the right feeling and lift your communication."]),
       did=L(["Vi erbjuder allt från produktfotografering till miljöbilder och annat visuellt material som kan stärka ert varumärke – med egen studio i Gamla Riksbankshuset."],
             ["We offer everything from product photography to location shots and other visual material that can strengthen your brand – with our own studio in Gamla Riksbankshuset."]),
       media=[("img", [("img/tjanster/foto-kedja.jpg", L("Guldkedja", "Gold chain")), ("img/tjanster/foto-tandare.jpg", L("Tändare", "Lighter")),
                       ("img/tjanster/foto-telefon.jpg", L("Grön telefonlur", "Green telephone receiver")), ("img/tjanster/foto-yinyang.jpg", L("Yin-yang-kulor i ask", "Yin-yang balls in a box"))]),
              ("studio", L(("Matfoto", "Fotografering i studion", "Produktfoto i studion"), ("Food photo", "Shooting in the studio", "Product shot in the studio"))),
              ("img", [("img/tjanster/foto-miljo-ljus.jpg", L("Uteservering i kvällsljus", "Outdoor seating in evening light")),
                       ("img/tjanster/foto-miljo-fonster.jpg", L("Fönster i svartvitt", "Window in black and white"))])]),
]

SERVICES = [
  (L("Filmproduktion", "Film production"),
   L("Vi producerar film som berättar er historia på ett engagerande och visuellt starkt sätt – från idé och manus till inspelning, redigering och färdig leverans.",
     "We produce films that tell your story in an engaging and visually striking way – from idea and script to shoot, edit and final delivery."), "fraseriet"),
  (L("Content & marknadsföring", "Content & marketing"),
   L("Vi skapar innehåll och kampanjer som engagerar, bygger relationer och stärker er synlighet i digitala och sociala kanaler.",
     "We create content and campaigns that engage, build relationships and boost your visibility across digital and social channels."), "fraseriet"),
  (L("Varumärke & design", "Brand & design"),
   L("Vi utvecklar visuella identiteter och design som ger ert varumärke en tydlig, konsekvent och professionell närvaro i alla kanaler.",
     "We develop visual identities and design that give your brand a clear, consistent and professional presence in every channel."), "topel-beats"),
  (L("Foto & visuellt material", "Photo & visual content"),
   L("Vi producerar bilder och visuellt material som förmedlar rätt känsla och lyfter er kommunikation.",
     "We produce images and visual material that convey the right feeling and lift your communication."), "foto-i-studion"),
  (L("Musik & ljudproduktion", "Music & sound production"),
   L("Vi skapar musik och ljud som förstärker berättelser, varumärken och helhetsupplevelser – med inhouse musikproduktion som ger full kreativ kontroll.",
     "We create music and sound that strengthen stories, brands and experiences – with in-house music production that gives full creative control."), "kings-of-kong"),
]

ABOUT = {
  "sv": ("Vi är en kreativ partner för varumärken, artister och företag som vill ha hjälp med branding, content och marknadsföring i ett sammanhållet grepp.",
         "Genom att kombinera design, film, musik och innehåll i samma team kan vi ta idéer hela vägen till färdig produktion. Med bakgrund inom film- och tv-produktion samt medie- och kommunikationsvetenskap förenar vi kreativt skapande med förståelse för hur budskap engagerar och bygger varumärken. Vi arbetar nära våra kunder, är flexibla i vårt arbetssätt och drivs av att skapa lösningar som både syns, hörs och känns.",
         "Med kontor och studio beläget i det gamla Riksbankshuset i centrala Uppsala ser vi till att alltid finnas nära och tillgängliga för våra kunder, samarbetspartners och andra som är intresserade av verksamheten. Vi ligger ett stenkast från Centralstationen och har därför närhet till Uppsala, Stockholm och kringliggande orter."),
  "en": ("We're a creative partner for brands, artists and companies who want branding, content and marketing brought together as one coherent whole.",
         "By combining design, film, music and content in one team, we can take ideas all the way to finished production. With backgrounds in film and TV production as well as media and communication studies, we pair creative craft with an understanding of how messages engage people and build brands. We work closely with our clients, stay flexible in how we work, and are driven by creating solutions that are seen, heard and felt.",
         "With our office and studio in the old Riksbank building, Gamla Riksbankshuset, in central Uppsala, we're always close at hand for clients, partners and anyone curious about what we do. We're a stone's throw from Uppsala Central Station, which puts Uppsala, Stockholm and the surrounding area within easy reach."),
}

PEOPLE = [("David", "+46708913214", "070-891 32 14", "+46 70 891 32 14"),
          ("Younes", "+46720444707", "072-044 47 07", "+46 72 044 47 07"),
          ("Topel", "+46723129002", "072-312 90 02", "+46 72 312 90 02")]


def e(s): return html.escape(s, quote=True)
def t(x, lang): return x[lang] if isinstance(x, dict) else x
def url(lang, kind, slug=None):
    p = PATHS[lang][kind]
    return p.format(slug) if slug else p
def job_url(lang, j): return url(lang, "job", t(j["slug"], lang))
def job_by_sv_slug(s): return next(j for j in JOBS if t(j["slug"], "sv") == s)


def page(lang, kind, title, desc, body, slug=None, current=None, home=False):
    path = job_url(lang, job_by_sv_slug(slug)) if kind == "job" else url(lang, kind)
    depth = path.count("/")
    R = "../" * depth                  # till /ny/
    A = "../" * (depth + 1)            # till repots rot
    tr = T[lang]
    links = [("work", tr["nav"][0]), ("clients", tr["nav"][1]), ("about", tr["nav"][2]), ("contact", tr["nav"][3])]
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{R}{url(lang, k)}"{cur if current == k else ""}>{label}</a>' for k, label in links)
    # samma sida på andra språket
    alt = {l: (job_url(l, job_by_sv_slug(slug)) if kind == "job" else url(l, kind)) for l in LANGS}
    on = ' class="on"'
    switch = " / ".join(f'<a href="{R + alt[l] or "./"}" hreflang="{l}" lang="{l}"{on if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    hreflang = "\n".join([f'<link rel="alternate" hreflang="{l}" href="{SITE}{alt[l]}">' for l in LANGS] +
                         [f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt["sv"]}">'])
    snap = ' class="snap"' if home else ''
    out = f'''<!doctype html>
<html lang="{lang}"{snap}>
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{hreflang}
<link rel="icon" href="{A}img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500&family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}style.css">
</head>
<body>

<nav class="nav">{nav}<span class="lang">{switch}</span></nav>
<a class="mark" href="{R + url(lang, "home") or "./"}"><img src="{A}img/logo.png" alt="{tr["home_alt"]}"></a>

<main>
{body.replace("{A}", A).replace("{R}", R)}
</main>

<footer>
  <div class="giant" aria-hidden="true">V</div>
  <div class="cols">
    <p>StudionValvet<br>Gamla Riksbankshuset<br>Kungsängsgatan 17–19<br>753 32 Uppsala{tr["country"]}</p>
    <p><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{R}{url(lang, "contact")}">{tr["nav"][3]}</a></p>
    <p><a href="https://www.instagram.com/studionvalvet/" target="_blank" rel="noopener">Instagram</a><br><a href="https://www.tiktok.com/@studionvalvet" target="_blank" rel="noopener">TikTok</a><br><a href="https://www.linkedin.com/search/results/companies/?keywords=Studion%20Valvet" target="_blank" rel="noopener">LinkedIn</a></p>
  </div>
  <p class="copy">© 2026 StudionValvet</p>
</footer>

<script src="{R}main.js"></script>
</body>
</html>
'''
    full = os.path.join(NY, path, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(out)


def meta(j, lang):
    tr = T[lang]
    return f'{tr["client"]}: {e(t(j["kund"], lang))}<br>{tr["scope"]}: {e(t(j["uppdrag"], lang))}'


def media_html(kind, items, lang):
    row = lambda n, inner, cls="": f'<div class="row{cls}" style="--n:{n}">{inner}</div>'
    video = lambda v, cls="": f'<video{cls} controls playsinline preload="none" poster="{{A}}video/{v}.jpg"><source src="{{A}}video/{v}.mp4" type="video/mp4"></video>'
    if kind == "raw":
        return items
    if kind == "video":
        return row(len(items), "".join(video(v) for v in items))
    if kind == "tallvideo":
        return row(len(items), "".join(video(v, ' class="tall"') for v in items))
    if kind == "sq":
        return row(len(items), "".join(f'<img class="sq {c}" src="{{A}}{s}" alt="{e(t(a, lang))}" loading="lazy">' for s, a, c in items))
    if kind == "spotify":
        return row(2, '<iframe src="https://open.spotify.com/embed/track/66zWHne0Lw9h2wmRUUfgZ9" title="Spotify" height="352" loading="lazy" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
                      f'<img src="{{A}}img/tjanster/musik-kings-of-kong.png" alt="{e(t(items, lang))}" loading="lazy" style="max-width:300px;justify-self:center;background:none">')
    if kind == "studio":
        mat, kedja, burk = t(items, lang)
        return row(4, video("foto-produktvideo", ' class="tall"') +
                      f'<img class="tall" src="{{A}}img/tjanster/foto-mat.jpg" alt="{e(mat)}" loading="lazy">'
                      f'<img class="tall" src="{{A}}img/tjanster/foto-studio-kedja.jpg" alt="{e(kedja)}" loading="lazy">'
                      f'<img class="tall" src="{{A}}img/tjanster/foto-studio-burk.jpg" alt="{e(burk)}" loading="lazy">')
    return row(len(items), "".join(f'<img src="{{A}}{s}" alt="{e(t(a, lang))}" loading="lazy">' for s, a in items),
               " one" if len(items) == 1 else "")


def build(lang):
    tr = T[lang]
    u = lambda kind, slug=None: "{R}" + url(lang, kind, slug)
    ju = lambda j: "{R}" + job_url(lang, j)

    # start
    teasers = "\n".join(f'''<a class="full teaser" href="{ju(j)}">
  <img class="bg" src="{{A}}{j["hero"]}" alt="" loading="lazy">
  <div class="inner rise">
    <h2 class="big">{e(t(j["title"], lang))}</h2>
    <div class="meta"><p>{meta(j, lang)}</p><p>{e(t(j["teaser"], lang))}<br><span class="go">{tr["see"]}</span></p></div>
  </div>
  <img class="logo" src="{{A}}img/logo.png" alt="">
</a>''' for j in JOBS)
    page(lang, "home", *PAGES["home"][lang], f'''<section class="full intro">
  <video class="bg" autoplay muted loop playsinline poster="{{R}}media/hero.jpg"><source src="{{R}}media/hero-mobil.mp4" type="video/mp4" media="(max-width: 760px)"><source src="{{R}}media/hero.mp4" type="video/mp4"></video>
  <div class="inner"><h1 class="big">{tr["hero"]}</h1></div>
  <img class="logo" src="{{A}}img/logo.png" alt="">
</section>
{teasers}''', home=True)

    # våra jobb
    rows = "\n".join(f'''  <a class="job rise" href="{ju(j)}">
    <div class="pic"><img src="{{A}}{j["hero"]}" alt="" loading="lazy"></div>
    <div><h2 class="mid">{e(t(j["title"], lang))}</h2><div class="who"><p>{meta(j, lang)}</p></div><p class="txt">{e(t(j["teaser"], lang))}</p></div>
  </a>''' for j in JOBS)
    page(lang, "work", *PAGES["work"][lang],
         f'<section class="page">\n<h1 class="big">{tr["nav"][0]}</h1>\n<div class="jobs">\n{rows}\n</div>\n</section>', current="work")

    # jobbsidor
    for i, j in enumerate(JOBS):
        nxt = JOBS[(i + 1) % len(JOBS)]
        text = (f'<h2>{tr["brief"]}</h2>' + "".join(f"<p>{p}</p>" for p in t(j["brief"], lang)) +
                f'<h2>{tr["did"]}</h2>' + "".join(f"<p>{p}</p>" for p in t(j["did"], lang)))
        media = "\n  ".join(media_html(k, it, lang) for k, it in j["media"])
        page(lang, "job", f'{t(j["title"], lang)} – StudionValvet', t(j["teaser"], lang), f'''<article class="page case">
<h1 class="big">{e(t(j["title"], lang))}</h1>
<div class="text">{text}<p>{meta(j, lang)}</p></div>
<div class="media">
  {media}
</div>
<a class="next" href="{ju(nxt)}"><small>{tr["next"]}</small><span class="mid" style="font-family:var(--serif)">{e(t(nxt["title"], lang))} →</span></a>
</article>''', slug=t(j["slug"], "sv"), current="work")

    # kunder
    cells = [
      (ju(job_by_sv_slug("fraseriet")), '<img src="{R}media/kund-fraseriet.png" alt="Fraseriet">'),
      (ju(job_by_sv_slug("cobra-combat")), '<img src="{A}img/kund-cobra.png" alt="Cobra Combat">'),
      (ju(job_by_sv_slug("topel-beats")), '<img src="{A}img/kund-topel.png" alt="Topel Beats">'),
      (ju(job_by_sv_slug("darkness-shall-pass")), '<span class="name">Viktor<br>Andersson</span>'),
      (ju(job_by_sv_slug("kings-of-kong")), '<span class="name">Kings<br>of Kong</span>'),
      (u("contact"), f'<span class="ask">{tr["ask"]}</span>'),
    ]
    grid = "\n".join(f'  <a class="rise" href="{h}">{c}</a>' for h, c in cells)
    page(lang, "clients", *PAGES["clients"][lang],
         f'<section class="page">\n<h1 class="big">{tr["nav"][1]}</h1>\n<div class="logos">\n{grid}\n</div>\n</section>', current="clients")

    # om oss
    lead, p1, p2 = ABOUT[lang]
    svc = "\n".join(f'  <a href="{ju(job_by_sv_slug(s))}"><h3 class="mid">{e(t(n, lang))}</h3><p>{e(t(d, lang))}</p></a>' for n, d, s in SERVICES)
    page(lang, "about", *PAGES["about"][lang], f'''<section class="full"><img class="bg" src="{{A}}img/riksbankshuset.jpg" alt="{"Gamla Riksbankshuset i Uppsala" if lang == "sv" else "Gamla Riksbankshuset in Uppsala"}"></section>
<section class="page">
<p class="lead rise" style="font-family:var(--serif)">{lead}</p>
<div class="cols rise">
  <p>{p1}</p>
  <p>{p2}</p>
</div>
<div class="list rise">
  <h2>{tr["what"]}</h2>
{svc}
</div>
</section>''', current="about")

    # kontakt
    people = "\n".join(f'  <p>{n}<br><a href="tel:{tel}">{sv if lang == "sv" else intl}</a></p>' for n, tel, sv, intl in PEOPLE)
    page(lang, "contact", *PAGES["contact"][lang], f'''<div class="map"><iframe src="https://www.google.com/maps/embed?origin=mfe&pb=!1m3!2m1!1sKungs%C3%A4ngsgatan+17,+753+32+Uppsala!6i15" title="{tr["map"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<section class="contact">
  <p>Gamla Riksbankshuset<br>Kungsängsgatan 17–19<br>753 32 Uppsala{tr["country"]}</p>
  <p>{tr["book"]}<br><a href="mailto:{MAIL}?subject={tr["subject"]}">{MAIL}</a></p>
{people}
</section>''', current="contact")


for lang in LANGS:
    build(lang)
print("ok")
