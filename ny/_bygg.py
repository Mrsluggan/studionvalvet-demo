# Bygger /ny/ (svenska) och /ny/en/ (engelska) från innehållet i ny/content/.
# Innehållet redigeras i admin (/ny/admin/) och sidan byggs om av GitHub Actions.
# Lokalt: python3 ny/_bygg.py
import os, re, json, glob, html, datetime
from urllib.parse import quote, quote_plus
NY = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(NY, "content")
SITE = "https://valvet.sluggan.com/ny/"
LANGS = ("sv", "en")

# adresser per språk, relativt /ny/
PATHS = {
  "sv": dict(home="", work="vara-jobb/", job="jobb/{}/", clients="kunder/", about="om-oss/", contact="kontakt/"),
  "en": dict(home="en/", work="en/work/", job="en/work/{}/", clients="en/clients/", about="en/about/", contact="en/contact/"),
}
MAP = {"sv": "Karta", "en": "Map"}


# --- innehåll -------------------------------------------------------------

def read(path):
    with open(path) as f:
        return json.load(f)

def localize(data, lang):
    """Admin sparar svenska och engelska i samma fil. Fält som saknas på engelska tas från svenskan."""
    if "sv" not in data:
        return data
    return {**data["sv"], **{k: v for k, v in data.get(lang, {}).items() if v not in (None, "", [])}}

def entries(folder):
    out = [(os.path.splitext(os.path.basename(f))[0], read(f)) for f in glob.glob(os.path.join(CONTENT, folder, "*.json"))]
    return sorted(out, key=lambda e: (e[1].get("sv", e[1]).get("ordning") or 999, e[0]))

JOBS = entries("jobb")
CLIENTS = entries("kunder")
SIDOR = {n: read(os.path.join(CONTENT, "sidor", n + ".json")) for n in ("allmant", "start", "vara-jobb", "kunder", "om-oss", "kontakt")}
SLUGS = [s for s, _ in JOBS]


# --- hjälpare -------------------------------------------------------------

def e(s): return html.escape(s or "", quote=False).replace('"', "&quot;")
def lines(s): return e((s or "").strip()).replace("\n", "<br>")
def paras(s): return "".join(f"<p>{lines(p)}</p>" for p in re.split(r"\n\s*\n", s or "") if p.strip())
def url(lang, kind, slug=None): return PATHS[lang][kind].format(slug) if slug else PATHS[lang][kind]
def asset(p):
    # "/ny/uppladdat/x.jpg" från admin blir en relativ sökväg, så att sidan funkar både lokalt och live
    return "{A}" + p[1:] if p and p.startswith("/") else (p or "")

def tel(nr): return "+46" + re.sub(r"\D", "", nr)[1:] if nr.strip().startswith("0") else re.sub(r"[^\d+]", "", nr)
def intl(nr): return "+46 " + nr.strip()[1:].replace("-", " ") if nr.strip().startswith("0") else nr

def embed(link):
    m = re.search(r"open\.spotify\.com/(?:embed/)?(track|album|playlist|artist|episode)/(\w+)", link)
    if m: return f"https://open.spotify.com/embed/{m[1]}/{m[2]}", "spotify"
    m = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([\w-]+)", link)
    if m: return f"https://www.youtube-nocookie.com/embed/{m[1]}", "wide"
    m = re.search(r"vimeo\.com/(\d+)", link)
    if m: return f"https://player.vimeo.com/video/{m[1]}", "wide"
    m = re.search(r"instagram\.com/(reel|p)/([\w-]+)", link)
    if m: return f"https://www.instagram.com/{m[1]}/{m[2]}/embed/", "reel"
    return link, "wide"


# --- sidmall --------------------------------------------------------------

def page(lang, kind, title, desc, body, slug=None, current=None, home=False):
    S = {n: localize(d, lang) for n, d in SIDOR.items()}
    g, kontakt = S["allmant"], S["kontakt"]
    path = url(lang, kind, slug)
    depth = path.count("/")
    R = "../" * depth                  # till /ny/
    A = "../" * (depth + 1)            # till repots rot
    links = [("work", S["vara-jobb"]["rubrik"]), ("clients", S["kunder"]["rubrik"]), ("about", S["om-oss"]["rubrik"]), ("contact", kontakt["rubrik"])]
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{R}{url(lang, k)}"{cur if current == k else ""}>{e(label)}</a>' for k, label in links)
    # samma sida på andra språket
    alt = {l: url(l, kind, slug) for l in LANGS}
    on = ' class="on"'
    switch = " / ".join(f'<a href="{R + alt[l] or "./"}" hreflang="{l}" lang="{l}"{on if l == lang else ""}>{l.upper()}</a>' for l in LANGS)
    hreflang = "\n".join([f'<link rel="alternate" hreflang="{l}" href="{SITE}{alt[l]}">' for l in LANGS] +
                         [f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt["sv"]}">'])
    snap = ' class="snap"' if home else ''
    mail = e(kontakt["epost"])
    social = "<br>".join(f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s.get("namn"))}</a>' for s in g.get("sociala") or [] if s.get("url"))
    logo = asset(g.get("logga"))
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
<link rel="icon" href="{logo}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500&family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}style.css">
</head>
<body>

<nav class="nav">{nav}<span class="lang">{switch}</span></nav>
<a class="mark" href="{R + url(lang, "home") or "./"}"><img src="{logo}" alt="{e(g["foretagsnamn"])}"></a>

<main>
{body.replace("{LOGO}", logo)}
</main>

<footer>
  <div class="giant" aria-hidden="true">V</div>
  <div class="cols">
    <p>{e(g["foretagsnamn"])}<br>{lines(kontakt["adress"])}</p>
    <p><a href="mailto:{mail}">{mail}</a><br><a href="{R}{url(lang, "contact")}">{e(kontakt["rubrik"])}</a></p>
    <p>{social}</p>
  </div>
  <p class="copy">© {datetime.date.today().year} {e(g["foretagsnamn"])}</p>
</footer>

<script src="{R}main.js"></script>
</body>
</html>
'''.replace("{A}", A).replace("{R}", R)
    full = os.path.join(NY, path, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(out)


# --- delar ----------------------------------------------------------------

def meta(j, g):
    return f'{e(g["kund_etikett"])}: {e(j.get("kund"))}<br>{e(g["uppdrag_etikett"])}: {e(j.get("uppdrag"))}'

def media_html(block):
    typ = block.get("type")
    if typ == "bildtext":
        return f'<p class="cap">{lines(block.get("text", ""))}</p>'
    if typ == "inbaddning":
        src, kind = embed(block.get("url", ""))
        if kind == "spotify":
            frame = f'<iframe src="{e(src)}" title="Spotify" height="352" loading="lazy" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
        else:
            ratio = "9/16" if kind == "reel" else "16/9"
            frame = f'<iframe src="{e(src)}" title="{e(block.get("alt") or "Video")}" style="aspect-ratio:{ratio}" loading="lazy" allow="autoplay; encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>'
        if block.get("bild"):
            return (f'<div class="row" style="--n:2">{frame}<img src="{asset(block["bild"])}" alt="{e(block.get("alt"))}" loading="lazy" '
                    'style="max-width:300px;justify-self:center;background:none"></div>')
        return f'<div class="row one" style="--n:1">{frame}</div>'
    # rad med bilder och/eller videor
    stil = block.get("stil", "vanlig")
    items = [o for o in block.get("objekt") or [] if o.get("bild") or o.get("video")]
    if not items:
        return ""
    cls = {"staende": ' class="tall"', "ruta": ' class="sq"'}.get(stil, "")
    cells = []
    for o in items:
        bg = f' style="background:{e(o["bakgrund"])}"' if stil == "ruta" and o.get("bakgrund") else ""
        if o.get("video"):
            poster = f' poster="{asset(o["bild"])}"' if o.get("bild") else ""
            cells.append(f'<video{cls}{bg} controls playsinline preload="none"{poster}><source src="{asset(o["video"])}" type="video/mp4"></video>')
        else:
            cells.append(f'<img{cls}{bg} src="{asset(o["bild"])}" alt="{e(o.get("alt"))}" loading="lazy">')
    one = " one" if len(cells) == 1 else ""
    return f'<div class="row{one}" style="--n:{len(cells)}">{"".join(cells)}</div>'


# --- sidor ----------------------------------------------------------------

def build(lang):
    S = {n: localize(d, lang) for n, d in SIDOR.items()}
    g = S["allmant"]
    seo = lambda n: (S[n].get("seo_titel") or S[n].get("rubrik") or g["foretagsnamn"], S[n].get("seo_beskrivning", ""))
    jobs = [(s, localize(d, lang)) for s, d in JOBS]
    ju = lambda slug: "{R}" + url(lang, "job", slug) if slug in SLUGS else "{R}" + url(lang, "work")

    # start
    start = S["start"]
    teasers = "\n".join(f'''<a class="full teaser" href="{ju(s)}">
  <img class="bg" src="{asset(j.get("bild"))}" alt="" loading="lazy">
  <div class="inner rise">
    <h2 class="big">{e(j.get("titel"))}</h2>
    <div class="meta"><p>{meta(j, g)}</p><p>{e(j.get("ingress"))}<br><span class="go">{e(g["se_jobbet"])}</span></p></div>
  </div>
  <img class="logo" src="{{LOGO}}" alt="">
</a>''' for s, j in jobs)
    sources = ""
    if start.get("film_mobil"):
        sources += f'<source src="{asset(start["film_mobil"])}" type="video/mp4" media="(max-width: 760px)">'
    if start.get("film"):
        sources += f'<source src="{asset(start["film"])}" type="video/mp4">'
    poster = f' poster="{asset(start["stillbild"])}"' if start.get("stillbild") else ""
    hero = (f'<video class="bg" autoplay muted loop playsinline{poster}>{sources}</video>' if sources
            else f'<img class="bg" src="{asset(start["stillbild"])}" alt="">' if start.get("stillbild") else "")
    page(lang, "home", *seo("start"), f'''<section class="full intro">
  {hero}
  <div class="inner"><h1 class="big">{lines(start.get("rubrik"))}</h1></div>
  <img class="logo" src="{{LOGO}}" alt="">
</section>
{teasers}''', home=True)

    # våra jobb
    rows = "\n".join(f'''  <a class="job rise" href="{ju(s)}">
    <div class="pic"><img src="{asset(j.get("bild"))}" alt="" loading="lazy"></div>
    <div><h2 class="mid">{e(j.get("titel"))}</h2><div class="who"><p>{meta(j, g)}</p></div><p class="txt">{e(j.get("ingress"))}</p></div>
  </a>''' for s, j in jobs)
    page(lang, "work", *seo("vara-jobb"),
         f'<section class="page">\n<h1 class="big">{e(S["vara-jobb"]["rubrik"])}</h1>\n<div class="jobs">\n{rows}\n</div>\n</section>', current="work")

    # jobbsidor
    for i, (s, j) in enumerate(jobs):
        ns, nj = jobs[(i + 1) % len(jobs)]
        text = f'<h2>{e(g["brief_rubrik"])}</h2>{paras(j.get("brief"))}<h2>{e(g["arbete_rubrik"])}</h2>{paras(j.get("arbete"))}'
        links = [l for l in j.get("lankar") or [] if l.get("url")]
        if links:
            text += "<p>" + "&nbsp;&nbsp; ".join(f'<a class="u" href="{e(l["url"])}" target="_blank" rel="noopener">{e(l.get("text") or l["url"])} →</a>' for l in links) + "</p>"
        media = "\n  ".join(filter(None, (media_html(b) for b in j.get("media") or [])))
        page(lang, "job", f'{j.get("titel")} – {g["foretagsnamn"]}', j.get("ingress", ""), f'''<article class="page case">
<h1 class="big">{e(j.get("titel"))}</h1>
<div class="text">{text}<p>{meta(j, g)}</p></div>
<div class="media">
  {media}
</div>
<a class="next" href="{ju(ns)}"><small>{e(g["nasta_jobb"])}</small><span class="mid" style="font-family:var(--serif)">{e(nj.get("titel"))} →</span></a>
</article>''', slug=s, current="work")

    # kunder
    cells = []
    for _, k in CLIENTS:
        inner = (f'<img src="{asset(k["logga"])}" alt="{e(k.get("namn"))}">' if k.get("logga")
                 else f'<span class="name">{e(k.get("namn"))}</span>')
        cells.append(f'  <a class="rise" href="{ju(k.get("jobb"))}">{inner}</a>')
    if S["kunder"].get("sista_rutan"):
        cells.append(f'  <a class="rise" href="{{R}}{url(lang, "contact")}"><span class="ask">{lines(S["kunder"]["sista_rutan"])}</span></a>')
    page(lang, "clients", *seo("kunder"),
         f'<section class="page">\n<h1 class="big">{e(S["kunder"]["rubrik"])}</h1>\n<div class="logos">\n' + "\n".join(cells) + '\n</div>\n</section>', current="clients")

    # om oss
    about = S["om-oss"]
    cols = "\n".join(f"  <p>{lines(p)}</p>" for p in re.split(r"\n\s*\n", about.get("text", "")) if p.strip())
    svc = "\n".join(f'  <a href="{ju(x.get("jobb"))}"><h3 class="mid">{e(x.get("namn"))}</h3><p>{e(x.get("text"))}</p></a>'
                    for x in about.get("tjanster") or [])
    page(lang, "about", *seo("om-oss"), f'''<section class="full"><img class="bg" src="{asset(about.get("bild"))}" alt="{e(about.get("bild_alt"))}"></section>
<section class="page">
<p class="lead rise" style="font-family:var(--serif)">{lines(about.get("ingress", ""))}</p>
<div class="cols rise">
{cols}
</div>
<div class="list rise">
  <h2>{e(about.get("tjanster_rubrik"))}</h2>
{svc}
</div>
</section>''', current="about")

    # kontakt
    k = S["kontakt"]
    mail = e(k["epost"])
    people = "\n".join(f'  <p>{e(p.get("namn"))}<br><a href="tel:{tel(p["telefon"])}">{e(p["telefon"] if lang == "sv" else intl(p["telefon"]))}</a></p>'
                       for p in k.get("personer") or [] if p.get("telefon"))
    karta = k.get("kartadress") or k["adress"].replace("\n", ", ")
    page(lang, "contact", *seo("kontakt"), f'''<div class="map"><iframe src="https://www.google.com/maps/embed?origin=mfe&pb=!1m3!2m1!1s{quote_plus(karta)}!6i15" title="{MAP[lang]}: {e(karta)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<section class="contact">
  <p>{lines(k["adress"])}</p>
  <p>{lines(k.get("boka_text"))}<br><a href="mailto:{mail}?subject={quote(k.get("mejlamne", ""))}">{mail}</a></p>
{people}
</section>''', current="contact")


# gamla genererade jobbsidor som inte längre finns i innehållet tas bort
for lang in LANGS:
    base = os.path.join(NY, url(lang, "job", "x")[:-2])
    for f in glob.glob(os.path.join(base, "*", "index.html")):
        if os.path.basename(os.path.dirname(f)) not in SLUGS:
            os.remove(f)
            os.rmdir(os.path.dirname(f))

for lang in LANGS:
    build(lang)
print("ok")
