# Loghi, foto, font, colori, icone

Le immagini sono la credibilità del deck: devono essere quelle ufficiali e vere. Tutto finisce nella
cartella del deck (`img/`, `font/`), così la presentazione si apre anche senza rete.

## Loghi

Dove prenderli, in quest'ordine:
1. I file della persona (cartella del marchio, kit stampa, repo).
2. Il sito ufficiale: spesso il logo è un `<svg>` dentro la pagina (barra in alto o fondo pagina) o un
   file `.svg` collegato. Scarica la pagina con `curl -sL -A "Mozilla/5.0" <url>`, cerca `<svg` vicino a
   `logo`, `brand`, `navbar`, `aria-label`, e salva l'SVG così com'è. Se il logo è fatto di due pezzi
   (simbolo e scritta), componili in un SVG solo senza toccare i tracciati.
3. La pagina "brand", "press" o "media kit" del sito.
4. Wikimedia Commons (`File:<Marchio> logo.svg`), scaricando l'originale.

Regole:
- Mai ridisegnare, deformare, ritagliare o ricolorare un logo. Se serve la versione per fondo scuro si
  usa quella ufficiale; se il logo è tutto di un colore va bene la classe `mono` del template.
- Si può solo ripulire il `viewBox` se il file ha margini enormi (si cambia il riquadro, non i tracciati).
- **Per ogni logo di terzi chiedi che rapporto c'è** (cliente, premio, programma, evento, partner) e
  scrivilo sotto il logo con le parole giuste. Un logo di un'azienda con cui non si è lavorato non va nel
  deck. Se il logo è di un partner, chiedi se il partner ha detto di sì a usarlo.

## Foto

- **Dal computer della persona:** chiedi dove sono (o cerca, con il suo permesso, in Scrivania,
  Download, Immagini, sito del progetto). Ritaglia con ImageMagick (`magick in.jpg -crop LxA+X+Y`) e
  salva in `img/`. Una foto piccola non va a tutto schermo: riquadro con gli angoli arrotondati.
- **Generate con l'AI:** ammesse per l'atmosfera e le illustrazioni (un ambiente, un oggetto, uno
  sfondo). Mai per persone vere, eventi, premi, prodotti, schermate o risultati: lì una foto finta è
  una bugia. Se nella sessione non c'è uno strumento per generare immagini, chiedi alla persona di
  generarla e dirti dove l'ha salvata.
- **Persone senza foto:** cerchio con le iniziali (`data-ph` + `onerror="ph(this)"`), mai una foto presa
  a caso o generata.
- **Schermate del prodotto:** vere, dal prodotto acceso, con dati inventati; si toglie quello che
  distrae (versioni, nomi interni).

## Font

- Se il marchio ha un font, cercalo nel CSS del sito (`font-family`). Se è su Google Fonts:
  `python3 scripts/font.py "<Famiglia>" <deck>/font/display.woff2` (o `ospite.woff2` per il cliente).
  Se è a pagamento usa il più simile su Google Fonts e dillo alla persona.
- Se il marchio non ha un font, sceglilo per il tono (vedi `stile.md`).

## Colori

Dal sito ufficiale: scarica il CSS (`curl` della pagina, poi dei file `.css` collegati) e conta i colori
(`grep -oE '#[0-9a-fA-F]{6}' | sort | uniq -c | sort -rn`) e le variabili (`--…-color`, `--brand…`). Il
più frequente scuro è l'inchiostro, quello vivo del logo è l'accento. Mettili nei token del template
(`--ink`, `--accent`, oppure `--g-ink`, `--g-accent`, `--g-drop` per il cliente).

## Icone (soprattutto nel tema scuro, stile keynote)

- Una sola famiglia, a tratto, con lo stesso spessore. Lucide va bene (licenza ISC): si scarica il
  singolo SVG da `https://unpkg.com/lucide-static@0.469.0/icons/<nome>.svg`, si incolla nel deck con
  `stroke="currentColor"`, e si dimensiona grande (96-160 px).
- Un'icona per idea, mai una griglia di icone. Mai emoji.
