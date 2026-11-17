# Lo stile "aura"

Il modello è un keynote di Steve Jobs: chi presenta parla, lo schermo mostra la prova. Sullo schermo
non c'è quello che si dice, c'è quello che rende vero quello che si dice: un logo ufficiale, una foto
vera, uno schema che si muove, una frase sola. Ogni clic aggiunge una cosa.

## I principi

1. **Un'idea per passo.** A ogni clic l'occhio ha un solo posto dove andare. La cosa nuova è piena, il
   resto si toglie o si attenua (opacità 0,3-0,4). Chi guarda deve capire il passo in tre secondi, anche
   da uno schermo condiviso su Teams, cioè piccolo e compresso.
2. **Grande e con aria.** Il soggetto occupa almeno metà del palco. Tanto vuoto intorno. Niente
   riempitivi per "non lasciare spazio".
3. **Pochissime parole.** Al massimo una frase per passo, idealmente sotto le 8 parole, mai sopra 12.
   Etichette di una o due parole. Niente elenchi puntati, niente titoli dentro le slide (l'etichetta in
   alto a destra c'è già), niente paragrafi. Se una cosa si può dire a voce, si dice a voce.
4. **Prove, non decorazioni.** Le immagini sono loghi ufficiali, foto vere, schermate vere del prodotto.
   Sono loro a dare credibilità ("aura"): un logo vero di un premio vale più di qualsiasi illustrazione.
5. **Il movimento ha un senso.** Le cose entrano quando se ne parla, si mettono in fila quando sono
   dette, si collegano quando il concetto è "collegare". Un movimento senza significato è rumore.
6. **Un momento forte.** Una o due volte per deck una scena a tutto schermo (la foto del premio, il
   colore del cliente che riempie la finestra). Più di due e non è più un momento.

## Le misure (palco 1920x1080)

| Cosa | Valore |
|---|---|
| Margini del contenuto | 140-160 px ai lati; la cornice sta a 96 px |
| Area utile | y tra 150 e 960 (sopra c'è il marchio, sotto il numero) |
| Parole principali | 56-120 px, peso 700-800, spaziatura stretta (-0,03 / -0,05 em) |
| Testo più piccolo | 22 px; unica eccezione le etichette in maiuscoletto da 19 px, spaziate 0,16 em |
| Tratti negli schemi | 4 px (mai sotto 3); punti di almeno 16 px |
| Durate | 0,6-1,1 s, curva `--ease`; ritardi a scalare 60-150 ms |
| Primo elemento di una slide | entra con 0,15-0,3 s di ritardo (prima svanisce la slide di prima) |
| Colore d'accento | meno del 5% della superficie, sulla cosa di cui si parla |

Niente rimbalzi, rotazioni, lampeggi, zoom continui. Animazioni infinite solo leggere e con un senso (i
puntini che scorrono su un filo collegato). Il cursore che lampeggia solo se fa parte del marchio.

## Fondo bianco o nero (si chiede all'inizio)

- **Bianco** (`data-theme="light"`): pagina prodotto Apple. Inchiostro quasi nero, grigi caldi o freddi
  scelti apposta, un solo colore d'accento. Le scene forti sono nere.
- **Nero** (`data-theme="dark"`): keynote. Nero pieno, testo quasi bianco, icone sottili bianche, foto
  come riquadri con gli angoli arrotondati, un accento. Ogni logo deve avere la versione per fondo
  scuro (ufficiale); se il logo è tutto di un colore si usa la classe `mono`.

## Tipografia

- Un solo font da titoli (`--display`): quello del marchio se esiste, altrimenti uno scelto per
  l'occasione e con carattere (Bricolage Grotesque, Inter Tight, Space Grotesk, Manrope, Sora; un serif
  come Fraunces o Instrument Serif se il tono è editoriale). Si scarica con `scripts/font.py`.
- Per il testo piccolo il font di sistema (`--text`).
- Grandi e strette le parole importanti; piccole, maiuscole e spaziate le etichette.

## Due marchi: il passaggio al cliente

Quando il pitch è per qualcuno, la prima parte (chi siamo) ha il marchio di chi presenta, la seconda
(il vostro problema, la proposta) prende i colori, il font e il logo del cliente: la presentazione
"diventa sua". Il passaggio è un momento: il riquadro vuoto si apre nel colore del cliente con il suo
logo grande (schema in `schemi.md`). Nella sezione del cliente il marchio di chi presenta resta solo come
firma piccola in basso a sinistra.

I colori e il font del cliente si prendono dal suo sito (vedi `asset.md`), non si inventano.

## Cosa fa sembrare un deck "vibecoded" (da non fare)

- Gradienti, bagliori, ombre dappertutto, vetro smerigliato, bordi colorati.
- Emoji, icone a caso, una griglia di tre "feature" con icona e due righe sotto ciascuna.
- Elenchi puntati, titoli su ogni slide, paragrafi.
- Viola e blu "da startup", più di un colore d'accento.
- Illustrazioni generiche, foto di repertorio, persone finte.
- Scatole con il testo dentro collegate da frecce; tabelle prima/dopo.
- Ogni riga che entra in dissolvenza, tutto che si muove insieme.
- Frasi come "Rivoluzioniamo il modo in cui…", superlativi, numeri senza fonte.

## Le parole

Le scrive l'AI, partendo dai concetti della persona e mai aggiungendone. Corte, concrete, vere. Una frase
deve reggere a una domanda di verifica di chi guarda ("davvero? con chi?"). Sotto un logo di terzi si
scrive esattamente che rapporto c'è ("Programma di accelerazione, Parigi, 2026", non "partner"). I numeri
solo se la persona li ha dati, con la fonte. Nessun trattino lungo.
