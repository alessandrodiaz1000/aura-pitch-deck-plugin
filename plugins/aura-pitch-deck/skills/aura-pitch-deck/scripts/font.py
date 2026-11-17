#!/usr/bin/env python3
"""Scarica un font da Google Fonts nella cartella font/ del deck, così la presentazione funziona senza rete.

  python3 font.py "<Famiglia>" <deck>/font/<nome>.woff2

Prende la versione variabile (tutti i pesi in un file) e solo i caratteri latini (italiano compreso).
Se la famiglia non ha la versione variabile scarica i pesi 400, 600, 700 e 800 in file separati
(<nome>-400.woff2, ...) e stampa le righe @font-face da incollare nel deck.
"""
import re, sys, urllib.error, urllib.parse, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def latin_blocks(css):
    out = []
    for m in re.finditer(r"/\*\s*([\w-]+)\s*\*/\s*@font-face\s*\{(.*?)\}", css, re.S):
        if m.group(1) == "latin":
            w = re.search(r"font-weight:\s*([\d ]+);", m.group(2)).group(1).strip()
            u = re.search(r"url\((https://[^)]+\.woff2)\)", m.group(2)).group(1)
            out.append((w, u))
    return out


def main(family, out):
    fam = urllib.parse.quote(family).replace("%20", "+")
    try:
        css = get("https://fonts.googleapis.com/css2?family=%s:wght@100..900&display=swap" % fam).decode()
        blocks = latin_blocks(css)
    except urllib.error.HTTPError:
        blocks = []
    if len(blocks) == 1:
        open(out, "wb").write(get(blocks[0][1]))
        print("scaricato %s (pesi %s): %s" % (family, blocks[0][0], out))
        return
    css = get("https://fonts.googleapis.com/css2?family=%s:wght@400;600;700;800&display=swap" % fam).decode()
    blocks = latin_blocks(css)
    if not blocks:
        raise SystemExit("famiglia non trovata su Google Fonts: %r" % family)
    base = out[:-6] if out.endswith(".woff2") else out
    name = base.rsplit("/", 1)[-1]
    for w, u in blocks:
        f = "%s-%s.woff2" % (base, w)
        open(f, "wb").write(get(u))
        print('@font-face { font-family: "%s"; font-weight: %s; font-display: block; src: url("font/%s-%s.woff2") format("woff2"); }'
              % (family, w, name, w))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    main(sys.argv[1], sys.argv[2])
