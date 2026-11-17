#!/usr/bin/env python3
"""Foto del deck, per guardarlo davvero prima di consegnarlo. Usa Chrome in modalità headless.

  python3 foto.py elenco    <deck>                         tabella dei passi: numero, slide, passo nella slide, etichetta
  python3 foto.py passi     <deck> <cartella> [DA-A]       una foto 1920x1080 per passo (stato finale) + foglio.png
  python3 foto.py movimento <deck> <passo> <cartella>      il movimento verso quel passo fermato a 150/350/600/900/1400 ms,
                                                           arrivando in avanti e tornando indietro
  python3 foto.py pdf       <deck> <cartella>              il PDF (?print) e le sue pagine in piccolo
  python3 foto.py provini   <deck> <cartella>              la pagina di confronto delle opzioni (?provini)

<deck> è la cartella con index.html. I passi si contano da 1, come nell'indirizzo (index.html#7).
Opzioni: --o b  per guardare l'opzione b quando una slide ne ha più di una.
"""
import os, re, shutil, subprocess, sys, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def sections(deck, opt=None):
    html = open(os.path.join(deck, "index.html"), encoding="utf-8").read()
    out, first_opt = [], None
    for m in re.finditer(r"<section\b[^>]*>", html):
        tag = m.group(0)
        if not re.search(r'class="[^"]*\bslide\b', tag):
            continue
        g = lambda k: (re.search(r'\b%s="([^"]*)"' % k, tag) or [None, None])[1]
        o = g("data-opt")
        if o and first_opt is None:
            first_opt = o
        out.append({"id": g("id") or "?", "beats": int(g("data-beats") or 1), "label": g("data-label") or "",
                    "opt": o, "print": g("data-print") or "", "tag": tag})
    want = opt or first_opt
    return [s for s in out if not s["opt"] or s["opt"] == want]


def steps(deck, opt=None):
    rows, n = [], 1
    for s in sections(deck, opt):
        for b in range(s["beats"]):
            lab = s["label"]
            for j in range(b + 1):
                mm = re.search(r'\bdata-label-%d="([^"]*)"' % j, s["tag"])
                if mm:
                    lab = mm.group(1)
            rows.append((n, s["id"], b, lab))
            n += 1
    return rows


def chrome(args):
    if not os.path.exists(CHROME):
        raise SystemExit("Chrome non trovato in " + CHROME)
    prof = tempfile.mkdtemp(prefix="aura-foto-")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                        "--force-device-scale-factor=1", "--user-data-dir=" + prof] + args,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    finally:
        shutil.rmtree(prof, ignore_errors=True)


def shot(deck, query, step, out):
    if os.path.exists(out):
        os.remove(out)
    chrome(["--window-size=1920,1080", "--virtual-time-budget=3000", "--screenshot=" + out,
            "file://%s/index.html?%s#%d" % (deck, query, step)])
    if not os.path.exists(out):
        raise SystemExit("foto non riuscita: " + out)


def sheet(files, out, width, per_row):
    rows = []
    for i in range(0, len(files), per_row):
        r = "%s.riga%d.png" % (out, i // per_row)
        subprocess.run(["magick"] + files[i:i + per_row] + ["-resize", "%dx" % width, "-bordercolor", "#d9d6cf",
                        "-border", "2", "+append", r], check=True)
        rows.append(r)
    subprocess.run(["magick"] + rows + ["-background", "#d9d6cf", "-append", out], check=True)
    for r in rows:
        os.remove(r)


def main(argv):
    opt = None
    if "--o" in argv:
        i = argv.index("--o"); opt = argv[i + 1]; del argv[i:i + 2]
    q = ("&o=" + opt) if opt else ""
    if len(argv) >= 2 and argv[0] == "elenco":
        for n, sid, b, lab in steps(os.path.abspath(argv[1]), opt):
            print("%3d  %-22s passo %d  %s" % (n, sid, b, lab))
        return
    if len(argv) >= 3 and argv[0] == "passi":
        deck, out = os.path.abspath(argv[1]), os.path.abspath(argv[2])
        os.makedirs(out, exist_ok=True)
        rows = steps(deck, opt)
        a, z = 1, len(rows)
        if len(argv) > 3:
            a, z = [int(x) for x in argv[3].split("-")]
        files = []
        for n, sid, b, lab in rows[a - 1:z]:
            f = os.path.join(out, "passo-%02d.png" % n)
            shot(deck, "still" + q, n, f)
            files.append(f)
            print("passo %d (%s, %d): %s" % (n, sid, b, f))
        sheet(files, os.path.join(out, "foglio.png"), 640, 3)
        print("foglio: " + os.path.join(out, "foglio.png"))
        return
    if len(argv) >= 4 and argv[0] == "movimento":
        deck, n, out = os.path.abspath(argv[1]), int(argv[2]), os.path.abspath(argv[3])
        os.makedirs(out, exist_ok=True)
        total = len(steps(deck, opt))
        for name, extra, ok in (("avanti", "", n > 1), ("indietro", "&back", n < total)):
            if not ok:
                continue
            files = []
            for ms in (150, 350, 600, 900, 1400):
                f = os.path.join(out, "m%02d-%s-%d.png" % (n, name, ms))
                shot(deck, "play=%d%s%s" % (ms, extra, q), n, f)
                files.append(f)
            o = os.path.join(out, "movimento-%02d-%s.png" % (n, name))
            sheet(files, o, 640, 5)
            for f in files:
                os.remove(f)
            print("movimento %s verso il passo %d: %s" % (name, n, o))
        return
    if len(argv) >= 3 and argv[0] == "pdf":
        deck, out = os.path.abspath(argv[1]), os.path.abspath(argv[2])
        os.makedirs(out, exist_ok=True)
        pdf = os.path.join(out, "deck.pdf")
        chrome(["--no-pdf-header-footer", "--virtual-time-budget=4000", "--print-to-pdf=" + pdf,
                "file://%s/index.html?print%s" % (deck, q)])
        if not os.path.exists(pdf):
            raise SystemExit("PDF non riuscito")
        pre = os.path.join(out, "pagina")
        subprocess.run(["pdftoppm", "-r", "40", "-png", pdf, pre], check=True)
        pages = sorted([os.path.join(out, f) for f in os.listdir(out) if f.startswith("pagina") and f.endswith(".png")],
                       key=lambda p: int(re.search(r"-(\d+)\.png$", p).group(1)))
        sheet(pages, os.path.join(out, "pdf.png"), 640, 3)
        for p in pages:
            os.remove(p)
        print("PDF: %s (%d pagine)\npagine: %s" % (pdf, len(pages), os.path.join(out, "pdf.png")))
        return
    if len(argv) >= 3 and argv[0] == "provini":
        deck, out = os.path.abspath(argv[1]), os.path.abspath(argv[2])
        os.makedirs(out, exist_ok=True)
        f = os.path.join(out, "provini.png")
        if os.path.exists(f):
            os.remove(f)
        chrome(["--window-size=1900,3200", "--virtual-time-budget=4000", "--screenshot=" + f, "file://%s/index.html?provini" % deck])
        print("provini: " + f)
        return
    print(__doc__)
    sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
