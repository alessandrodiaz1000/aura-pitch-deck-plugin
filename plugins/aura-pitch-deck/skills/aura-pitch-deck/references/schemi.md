# Schemi pronti

Ogni schema qui sotto viene da un pitch vero e si vede all'opera in `assets/esempio/index.html` (marchi
inventati), che usa il motore del template. Si copia, si adatta, si guarda.

Indice: 1 copertina · 2 persone · 3 marchio al centro con frase · 4 frase grande · 5 fila di voci ·
6 scena a tutto schermo · 7 schermata del prodotto · 8 riquadro vuoto e apertura del cliente ·
9 schema di un concetto · 10 opzioni alternative.

Regole comuni:
- Ogni slide è una `<section class="slide">` con `id`, `data-beats`, `data-label`, `data-print`.
- Le cose entrano con `data-from` (e spariscono con `data-until`) più una classe di entrata
  (`fx`, `fx-zoom`, `fx-fade`) o un CSS proprio. Il ritardo si dà con `style="--d:.3s"`.
- Il CSS proprio di una slide va nella sezione 4 del template, con l'id della slide come prefisso
  (`#tappe .qualcosa`), così non tocca le altre.

## 1. Copertina: chi presenta × cliente

È già nel template. Il marchio grande è quello della cornice: al passo dopo vola in alto a sinistra. Le
posizioni le calcola lo script dalle misure dei loghi (`--cover-h` regola l'altezza dei due marchi).
Senza cliente si tolgono `.lock-x` e `.lock-guest`: il marchio resta da solo al centro.

## 2. Persone

```html
<section class="slide" id="team" data-beats="2" data-label="Chi siamo" data-print="1">
  <h1 class="say fx" data-from="0">Tre persone, uno studio.</h1>
  <figure class="person fx p1" data-from="0" style="left:420px;top:430px;--d:.2s">
    <span class="face"><img src="img/nome-cognome.jpg" alt="" data-ph="NC" onerror="ph(this)"></span>
    <figcaption><b>Nome Cognome</b><i>Ruolo</i></figcaption>
  </figure>
  <!-- p2, p3, p4 con left 780, 1140, 1500 e --d .28s, .36s, .44s -->
</section>
```
Per dire "su questo progetto ci siamo noi due" al passo 1 i primi due si ingrandiscono e gli altri si
rimpiccioliscono a destra (misure di partenza, da regolare guardando le foto):
```css
#team[data-b="1"] .p1 { transform: translate(30px, 30px) scale(1.36); }
#team[data-b="1"] .p3 { transform: translate(220px, -57px) scale(.66); }
#team .person i { opacity: 0; transition: opacity .5s ease; }
#team[data-b="1"] .p1 i, #team[data-b="1"] .p2 i { opacity: 1; transition-delay: .45s; }
```
Se una foto manca resta il cerchio con le iniziali (`data-ph`): mai una foto inventata.

## 3. Marchio al centro con una frase sotto

```html
<section class="slide" id="cosa" data-beats="1" data-label="Chi siamo" data-hero data-print="0">
  <p class="lede fx" data-from="0" style="--d:.6s">Una frase che dice cosa fate.</p>
</section>
```
`data-hero` porta il marchio della cornice grande al centro (`--hero-w`, `--hero-y`).

## 4. Frase grande

```html
<section class="slide" id="perche" data-beats="1" data-label="Perché" data-print="0">
  <p class="big" data-from="0">Una frase sola,<br>grande.</p>
</section>
```
Per la parola chiave: `<em style="color:var(--accent)">` solo se l'accento regge sul fondo (il giallo
su bianco no: meglio un blocco `.accent-block` dopo la frase, o il colore solo in tema scuro).

## 5. Fila di voci (tappe, loghi, prodotti)

Ogni voce entra grande al centro nel suo passo, poi va al suo posto; all'ultimo passo sono tutte in
fila. Con `data-peek` un clic sulla voce in fila la ingrandisce di nuovo (per rispondere a una domanda).
```html
<section class="slide" id="tappe" data-beats="4" data-label="Cosa abbiamo fatto" data-print="3">
  <div class="item" data-spot="0" data-peek="prog">
    <div class="art"><img src="img/programma.svg" alt="Nome del programma" style="height:170px"></div>
    <b>Nome del programma</b><i>Selezionati · città, mese anno</i>
  </div>
  <div class="item" data-spot="1" data-peek="premio">…</div>
  <div class="item" data-spot="2" data-peek="pilota" data-bleed>…</div>   <!-- questa ha una scena: schema 6 -->
</section>
```
Passi = numero di voci + 1. Senza `left` lo script le mette in fila da solo; per regolarle a mano:
`style="left:400px; --dx:560px; --s:1.7"` (`--dx` = 960 - left, `--s` = quanto è grande al centro).
Il didascalia sotto il logo dice il rapporto vero, in poche parole.

## 6. Scena a tutto schermo (il momento forte)

Il fondo copre tutta la finestra, i pezzi entrano a scalare. Si lega a una slide e a uno o più passi.
```html
<div class="bleed" id="scena-pilota" data-slide="tappe" data-beat="2" data-peek="pilota">
  <div class="fit over">
    <img class="photo" src="img/foto-vera.jpg" alt="Cosa si vede nella foto" style="left:760px;top:221px;width:1064px;height:638px;--d:.15s">
    <img src="img/partner-su-scuro.svg" alt="Partner" style="left:96px;top:356px;width:250px;--d:.35s">
    <p style="left:96px;top:452px;font:800 128px/1 var(--display);letter-spacing:-.05em;--d:.45s">Progetto</p>
    <p style="left:96px;top:634px;font:700 40px/1.1 var(--display);--d:.6s">Cosa è successo, in poche parole</p>
  </div>
</div>
```
Le scene vanno dopo `</main>`. Se la foto è a bassa risoluzione non va a tutto schermo: riquadro con gli
angoli arrotondati, come qui.

## 7. Schermata del prodotto

Una schermata vera (mai un mockup disegnato), in una voce della fila, con l'ombra leggera (l'unica ombra
ammessa) e `data-peek` per ingrandirla:
```css
#oggi .shot { height: 310px; width: auto; border-radius: 14px; box-shadow: 0 0 0 1px var(--line), 0 18px 50px rgba(21,22,26,.10); }
```
Si toglie dalla schermata tutto quello che distrae o che non deve vedersi (versioni, nomi interni,
dati veri di clienti: nelle schermate solo dati inventati).

## 8. Riquadro vuoto e apertura della sezione del cliente

Ultima voce di "cosa facciamo": un riquadro tratteggiato vuoto ("le cose su misura": quella per voi non
c'è ancora). Al clic il colore del cliente parte dal riquadro e riempie la finestra, con il suo logo
grande; il clic dopo apre la sua sezione.
```html
<div class="item" data-spot="2" data-dock>
  <div class="art"><span class="void"><svg viewBox="0 0 500 310" aria-hidden="true"><rect x="2" y="2" width="496" height="306" rx="28" fill="none" stroke="currentColor" stroke-width="4" stroke-dasharray="18 14" stroke-linecap="round"/></svg></span></div>
  <b>Prodotti su misura</b><i>Per le aziende</i>
</div>

<!-- dopo, nel <main>: la slide dell'apertura (vuota: si vede tutto nella scena) -->
<section class="slide" id="apre" data-beats="1" data-label="" data-ospite data-title="0" data-nocount data-print="0"></section>

<!-- dopo </main>: la scena che parte dal riquadro -->
<div class="bleed portal" id="apri" data-slide="apre"></div>
```
Da qui in poi le slide del cliente hanno `data-ospite`: colori `--g-*`, font `--g-display`, il suo logo in
alto a sinistra, il marchio di chi presenta come firma in basso.

## 9. Schema di un concetto (problema e soluzione nella stessa slide)

L'esempio completo è la slide `#problema` di `assets/esempio` (CSS con prefisso `.pp-`): tre elenchi dei
venditori storti e sparsi, il responsabile con un "?", i contatti che mancano; poi un blocco al centro che
li collega, riceve i contatti da fuori e dà a ognuno la sua vista. Sette passi, una didascalia per passo.

I mattoni sono già nel template:
```html
<svg class="wires" viewBox="0 0 1920 1080" aria-hidden="true" style="color:var(--g-ink)">
  <!-- un filo: la linea che si disegna (l), i puntini che scorrono (f), la punta (h) -->
  <g class="w" data-from="3">
    <path class="l" pathLength="1" d="M480 320 C 640 320 630 470 784 470"/>
    <path class="f" d="M480 320 C 640 320 630 470 784 470"/>
    <path class="h" d="M772 456 L786 470 L772 484"/>
  </g>
</svg>
<span class="av"><span>S</span></span>                                   <!-- una persona: cerchio con l'iniziale -->
<p class="cap" data-from="0" data-until="0">Ogni BM ha il suo elenco.</p>  <!-- una didascalia per passo -->
```
Punta di una freccia che arriva da sinistra in (x, y): `M x-14 y-14 L x y L x-14 y+14`. Le curve
finiscono in orizzontale, così la punta è sempre dritta. Per cambiare un elemento da un passo in poi:
un contenitore con `data-from` per l'entrata e uno interno con un altro `data-from` per il cambio
(nell'esempio: `.pp-sheet` entra al passo 0, `.pp-tilt` si raddrizza al passo 3). Per attenuare quello di
cui non si parla: `#id[data-b="1"] .cosa.on { opacity: .4 }`. L'etichetta in alto può cambiare a metà:
`data-label-3="L'idea"`. Nel PDF vanno il fotogramma del problema e quello della soluzione.

## 10. Opzioni alternative di una slide

Per far scegliere tra più versioni: la stessa slide scritta più volte con `data-opt="a"`, `"b"`, `"c"` e
`data-name="Nome breve"`. Se ne vede una alla volta; il tasto O cambia opzione, T apre i provini (tutte le
opzioni con tutti i passi, una riga ciascuna), `?o=b` nell'indirizzo apre la b. Quando la persona ha
scelto si cancellano le altre: in basso al centro non resta nessuna scritta.
