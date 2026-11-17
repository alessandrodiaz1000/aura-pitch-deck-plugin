#!/usr/bin/env python3
"""Controllo automatico di un deck prima di consegnarlo.

  python3 controlla.py <deck>

Controlla: file mancanti (immagini, font), risorse esterne (il deck deve aprirsi senza rete), segnaposto del
template rimasti, trattini lunghi, attributi delle slide (passi, stampa, etichette), scene collegate a slide
che non esistono, e quanto testo c'è sullo schermo. Stampa il testo visibile di ogni slide, così si rilegge.
Esce con 1 se trova ERRORI (gli AVVISI non bloccano, ma vanno letti).
"""
import html as H
import os, re, subprocess, sys

SEGNAPOSTO = ["TITOLO DEL DECK", "CLIENTE", "MARCHIO", "DATA O OCCASIONE", "ETICHETTA", "Una frase sola, grande.",
              "{{", "}}", "lorem ipsum", "TODO"]
MAX_PAROLE_FRASE = 12      # una frase sullo schermo
MAX_PAROLE_SLIDE = 30      # tutto il testo di una slide, sommando i passi


def visible_text(fragment):
    s = re.sub(r"<!--.*?-->", " ", fragment, flags=re.S)
    s = re.sub(r"<(script|style|title|desc)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>", " ", s)
    parts = [H.unescape(x).strip() for x in re.findall(r">([^<>]+)<", s)]
    return [re.sub(r"\s+", " ", x) for x in parts if x.strip()]


def img_width(path):
    try:
        r = subprocess.run(["sips", "-g", "pixelWidth", path], capture_output=True, text=True, timeout=20)
        m = re.search(r"pixelWidth:\s*(\d+)", r.stdout)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def main(deck):
    deck = os.path.abspath(deck)
    p = os.path.join(deck, "index.html")
    t = open(p, encoding="utf-8").read()
    err, warn = [], []

    # 1. file citati che non esistono, risorse esterne
    refs = re.findall(r'\b(?:src|href)="([^"#?]+)', t) + re.findall(r"url\(\s*['\"]?([^'\")]+)", t)
    for r in sorted(set(refs)):
        if r.startswith("data:") or r.startswith("#"):
            continue
        if re.match(r"https?://", r):
            if "www.w3.org" not in r:
                err.append("risorsa esterna (senza rete non si vede): %s" % r)
            continue
        f = os.path.join(deck, r)
        if not os.path.exists(f):
            onerr = re.search(r'src="%s"[^>]*onerror=' % re.escape(r), t)
            (warn if onerr else err).append("file mancante: %s%s" % (r, " (c'è il segnaposto con le iniziali)" if onerr else ""))
        elif re.search(r"\.(jpe?g|png|webp)$", r, re.I):
            size = os.path.getsize(f)
            if size > 3_000_000:
                warn.append("immagine pesante (%.1f MB): %s" % (size / 1e6, r))
            w = img_width(f)
            if w and w < 900:
                warn.append("immagine piccola (%d px di larghezza): %s. Se è grande sullo schermo si vede sgranata" % (w, r))

    # 2. segnaposto e trattini lunghi
    body = t[t.find("<body"):]
    # i segnaposto si cercano solo dove si vedono: testo, alt, etichette (non nei commenti o nel codice)
    seen = " | ".join(visible_text(body) + re.findall(r'\balt="([^"]*)"', body) + re.findall(r'\bdata-label(?:-\d+)?="([^"]*)"', body))
    for s in SEGNAPOSTO:
        hit = (s.lower() in seen.lower()) if s.islower() or not s.isupper() and s[0].islower() else (s in seen)
        if hit:
            err.append("è rimasto il segnaposto del template: %r" % s)
    if "—" in body:
        err.append("c'è un trattino lungo (—): non si usa")
    if re.search(r"<title>\s*TITOLO", t):
        err.append("manca il titolo del deck (<title>)")

    # 3. slide
    secs = list(re.finditer(r"(<section\b[^>]*>)(.*?)</section>", t, re.S))
    ids = []
    for m in secs:
        tag, inner = m.group(1), m.group(2)
        if not re.search(r'class="[^"]*\bslide\b', tag):
            continue
        sid = (re.search(r'\bid="([^"]*)"', tag) or [None, None])[1]
        if not sid:
            err.append("una slide non ha id: %s" % tag[:80]); sid = "?"
        if sid in ids:
            err.append("id ripetuto: %s" % sid)
        ids.append(sid)
        nb = re.search(r'\bdata-beats="(\d+)"', tag)
        if not nb:
            err.append("%s: manca data-beats" % sid); continue
        n = int(nb.group(1))
        if 'data-label="' not in tag:
            warn.append("%s: manca data-label (l'etichetta in alto a destra)" % sid)
        pr = re.search(r'\bdata-print="([^"]*)"', tag)
        if not pr:
            warn.append("%s: manca data-print (la slide non finisce nel PDF)" % sid)
        else:
            for b in pr.group(1).split():
                if not b.isdigit() or int(b) >= n:
                    err.append("%s: data-print contiene %r ma i passi vanno da 0 a %d" % (sid, b, n - 1))
        for attr in ("data-from", "data-until", "data-spot"):
            for v in re.findall(r'\b%s="([^"]*)"' % attr, inner):
                if not v.lstrip("-").isdigit() or int(v) >= n:
                    warn.append("%s: %s=%r fuori dai passi della slide (0-%d)" % (sid, attr, v, n - 1))
        words = visible_text(inner)
        tot = sum(len(x.split()) for x in words)
        if words:
            print("== %s (%d passi, %d parole)" % (sid, n, tot))
            for x in words:
                print("   · " + x)
        if tot > MAX_PAROLE_SLIDE:
            warn.append("%s: %d parole sullo schermo. Si può dire a voce una parte?" % (sid, tot))
        for x in words:
            if len(x.split()) > MAX_PAROLE_FRASE:
                warn.append("%s: frase lunga (%d parole): %r" % (sid, len(x.split()), x[:70]))

    # 4. scene collegate a slide che non esistono
    for sl in re.findall(r'class="bleed[^"]*"[^>]*\bdata-slide="([^"]*)"', t):
        if sl not in ids:
            err.append("una scena .bleed punta alla slide %r, che non esiste" % sl)

    for w in warn:
        print("AVVISO:", w)
    for e in err:
        print("ERRORE:", e)
    print("ESITO:", ("%d errori" % len(err)) if err else "nessun errore", "· %d avvisi" % len(warn))
    return 1 if err else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))
