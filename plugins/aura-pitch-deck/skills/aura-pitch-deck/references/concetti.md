# Concetti complessi: dall'intervista all'animazione

Un concetto complesso è quello che la persona ha segnato come tale nella struttura (o quello per cui hai
chiesto "questo vuoi animarlo?" e ha detto sì). Per questi non basta una frase: serve uno schema che si
muove e che, alla fine, rappresenta la soluzione su cui la persona parla.

## 1. L'intervista (prima di disegnare qualsiasi cosa)

Chiedi una descrizione dettagliata, in un messaggio solo. Le domande:

1. Cos'è, in due o tre frasi, con parole tue.
2. Chi o cosa c'è in gioco (persone, ruoli, oggetti, sistemi) e come lo chiamano loro.
3. Com'è oggi e com'è dopo, oppure come funziona passo per passo.
4. L'unica cosa che chi guarda deve ricordarsi.
5. Numeri veri, con la fonte, o nessun numero.
6. Cosa non deve sembrare o promettere (per esempio: "non è ancora un prodotto finito").
7. Dopo la slide c'è una demo? Se sì, cosa mostra (lo schema deve preparare la demo, non ripeterla).

Se la risposta è vaga su un punto che cambia il disegno, chiedi di nuovo su quel punto solo. Non
riempire i buchi con ipotesi tue: un concetto inventato dall'AI è proprio quello che questa skill evita.

## 2. Una o più opzioni

Poi chiedi: **"Vuoi più opzioni o ti fidi della prima?"**

- **Una:** costruisci la migliore che hai in mente.
- **Più opzioni:** tre, costruite davvero (non descritte), come slide alternative con `data-opt`
  (schema 10 in `schemi.md`). Devono essere tre idee diverse, non tre varianti della stessa. Metafore che
  funzionano: una mappa che si collega (rete), una storia nel tempo (una settimana, un giorno), un prima
  e dopo nello stesso disegno, un oggetto solo che si trasforma, tre domande che trovano risposta.
  Consegnale con i provini (tasto T) e fai scegliere. Dopo la scelta cancella le altre.

## 3. La grammatica degli schemi

Pochi segni, sempre gli stessi, così chi guarda impara a leggerli in un secondo:

| Cosa | Segno |
|---|---|
| Una persona | cerchio pieno con l'iniziale (`.av`) |
| Un'organizzazione, un'azienda | quadrato con gli angoli arrotondati |
| Un dato, un contatto | anello (cerchio vuoto) |
| Un'azione, una relazione | linea che si disegna |
| Qualcosa che passa (dati, richieste) | puntini che scorrono sulla linea |
| Quello che manca o non si sa | grigio chiaro, tratteggiato, "?" |
| Quello che c'è | inchiostro pieno |
| La risposta, la cosa di cui si parla | il colore d'accento |
| Il conflitto | rosso, un elemento solo in tutta la slide |
| Verificato | una piccola spunta verde |

Niente icone da libreria dentro gli schemi, niente scatole con testo collegate da frecce, niente
tabelle. Le parole negli schemi sono etichette di una o due parole.

## 4. Lo storyboard

Prima di scrivere il codice, fissa la sequenza (per te, non serve mostrarla):

| Passo | Cosa cambia (una cosa sola) | Parole a schermo | Cosa dice chi presenta |
|---|---|---|---|

Regole:
- 4-7 passi. Il problema prima, la soluzione dopo, nella stessa slide se il concetto è "collegare" o
  "trasformare" (il disegno che cambia è la spiegazione).
- Una didascalia in basso per passo (`.cap`), sotto le 7 parole, che cambia in dissolvenza.
- L'etichetta in alto può passare da "Il problema" a "L'idea" (`data-label-N`).
- Mentre si parla di una cosa, le altre del problema si attenuano.
- Nel PDF (`data-print`): il fotogramma con tutto il problema e quello con tutta la soluzione. Da soli,
  senza chi presenta, devono capirsi.

## 5. Controlli prima di consegnarlo

- Ogni passo si capisce in tre secondi nel foglio piccolo (`foto.py passi`).
- Il movimento di ogni passo ha un senso, avanti e indietro (`foto.py movimento`).
- Nessun elemento si sovrappone a un altro o esce dall'area utile; le linee arrivano ai bordi giusti.
- Ogni parola a schermo è vera e viene dai concetti della persona.
