---
name: aura-pitch-deck
description: "Crea presentazioni HTML interattive in stile keynote alla Steve Jobs (\"aura\"): chi presenta parla, sullo schermo pochissimo testo, loghi e foto ufficiali che compaiono a ogni clic, animazioni con un senso, schemi animati per i concetti complessi, passaggio ai colori e al logo del cliente. Struttura e concetti li decide la persona: la skill li chiede prima di costruire e non li propone mai, poi li critica e fa la resa. Usala quando qualcuno chiede /aura-pitch-deck, una presentazione \"aura\" o \"stile Steve Jobs\", un pitch o un deck HTML animato o interattivo, slide con poco testo e loghi veri per un cliente, un investitore, una giuria o un evento, anche se non nomina la skill. Non per i file PowerPoint."
---

# Aura pitch deck

Fa presentazioni HTML che sembrano fatte su misura, non generate: fondo pulito, una cosa per clic, loghi
e foto ufficiali, movimenti che spiegano. Chi presenta parla sopra; lo schermo mostra la prova di quello
che dice. Il risultato è una cartella con `index.html` (più `img/` e `font/`) che si apre con un doppio
clic e funziona senza rete.

Il riferimento è `assets/esempio/` (rombo × marea, marchi inventati, nato da un pitch vero): aprilo nel
browser per vedere il ritmo. Il punto di partenza di ogni deck nuovo è `assets/template/`.

## La regola che viene prima di tutto

**La struttura e i concetti li decide la persona. L'AI fa solo la resa.**

Il motivo: appena l'AI propone una scaletta, chi la legge ci si attacca. La prima struttura che si vede
diventa quella giusta, anche se non è quella che la persona avrebbe scelto, e il pitch smette di essere
suo. Quindi non proponi mai l'ordine delle slide, quali slide fare o quali concetti mettere. Puoi (e
devi) criticare quello che la persona ti dà, con domande. Le parole sullo schermo invece le scrivi tu,
partendo dai suoi concetti e senza aggiungerne.

## Il flusso

### 1. Le domande, prima di qualsiasi file

Manda queste domande in un messaggio solo, numerate, e non costruire niente finché le prime sei non
hanno risposta:

1. **Chi guarda** e cosa deve decidere o fare alla fine. Quanto dura il pitch. Dove (sala, videochiamata).
2. **Fondo bianco o nero?** Bianco: pulito, da pagina prodotto. Nero: da keynote, con icone e foto.
3. **Chi presenta:** marchio (logo ufficiale, colori e font, se ci sono). Se il pitch è per un cliente,
   **chi è il cliente**: il suo marchio lo prendo dal suo sito per la seconda parte del deck.
4. **La struttura:** l'elenco ordinato delle slide e, per ognuna, una frase con quello che chi guarda
   deve capire.
5. **Le prove:** per ogni slide i loghi (e che rapporto c'è con ognuno), le foto (dove sono sul
   computer), i fatti e i numeri (con la fonte).
6. **I concetti complessi:** quali vuoi spiegare con un'animazione.
7. Dove salvo la cartella del deck.

La lingua del deck è quella della richiesta. Se la persona ha già scritto una scaletta da qualche parte,
quella è la sua struttura: usala e confermala con lei.

Se manca la struttura e la persona dice "proponila tu", non farlo. Spiega in due righe perché (sopra)
e aiutala a trovarla con domande che non suggeriscono contenuti: cosa deve fare chi guarda alla fine?
quali sono le tre cose che deve sapere per farlo? in che ordine le diresti a voce, senza slide?

### 2. La critica della struttura (sempre, e severa)

Leggi la struttura come la leggerebbe il pubblico più scettico. Rispondi con osservazioni numerate, ognuna
con la slide a cui si riferisce e una domanda. Cerca:

- due slide che dicono la stessa cosa, o una slide con più di un'idea;
- una slide senza una cosa precisa da capire;
- un'affermazione che non regge a una domanda di verifica ("davvero? con chi? quando?") o che manca di prova;
- troppa roba per il tempo (circa una slide al minuto, al massimo sei o sette passi per slide);
- un ordine che sembra non voluto (la soluzione prima del problema, una chiusura che non chiede niente);
- un logo di terzi senza un rapporto chiaro;
- quello che il pubblico chiederà di sicuro (prezzo, referenze, tempi): risposta a voce o slide?

Non scrivere una versione corretta, non riordinare, non aggiungere slide. Chiudi con "Cosa cambi?" e
aspetta la struttura definitiva. Se la persona dice che va bene così, si va avanti.

### 3. I concetti complessi

Per ogni concetto segnato fai l'intervista di `references/concetti.md` (descrizione dettagliata), poi
chiedi: **"Vuoi più opzioni o ti fidi della prima?"**. Con più opzioni ne costruisci tre, davvero diverse,
da sfogliare con il tasto O e confrontare con T; dopo la scelta cancelli le altre.

### 4. I materiali

Loghi ufficiali, foto vere, font e colori dei marchi: come si trovano e le regole in
`references/asset.md`. Per ogni logo di terzi chiedi che rapporto c'è, se non l'hai già saputo.

### 5. La costruzione

1. Copia `assets/template/` nella cartella scelta (`index.html`, `img/`, `font/`).
2. Sezione 1 del CSS: colori, font, misure dei marchi; `data-theme` su `<html>` (bianco o nero). Metti i
   loghi nella cornice: `img/logo.svg` e `img/logo-su-scuro.svg` per chi presenta, `img/cliente.svg` e
   `img/cliente-su-scuro.svg` per il cliente (senza cliente togli `.glogo` e il lockup in copertina).
3. Una `<section>` per ogni slide della struttura, nell'ordine dato. Gli schemi pronti sono in
   `references/schemi.md`, le regole di stile in `references/stile.md`.
4. Le parole: le scrivi tu, poche, vere. Una frase per passo, idealmente sotto le 8 parole. Sotto ogni
   logo di terzi il rapporto esatto. Nessun numero che la persona non ti abbia dato. Nessun trattino lungo.
5. Il CSS di ogni slide va nella sezione 4 del template, con l'id della slide come prefisso.

### 6. La verifica

Obbligatoria, con gli script e guardando le foto: `references/verifica.md`. Si consegna solo con
`controlla.py` senza errori e dopo aver visto ogni passo, il movimento dei passi importanti e il PDF.

### 7. La consegna

Nel messaggio finale:
- dove sta la cartella e come si apre (doppio clic su `index.html` in Chrome; F schermo intero; frecce,
  spazio o clic per andare avanti; P per il PDF; T e O se ci sono opzioni);
- una tabella: passo, cosa c'è sullo schermo, cosa dire a voce (frasi vere, nelle parole della persona);
- cosa manca (foto, permessi per i loghi, numeri da confermare);
- se ci sono opzioni, quali sono e come confrontarle.

## La verità

Un pitch "aura" regge solo se tutto quello che mostra è vero: chi guarda può controllare.
- Nessun cliente, premio, partner, numero o risultato che la persona non ti abbia dato.
- Nessun logo di un'azienda con cui non c'è un rapporto vero; la didascalia dice quale.
- Persona senza foto: cerchio con le iniziali, mai una foto inventata. Immagini generate con l'AI solo per
  l'atmosfera, mai per persone, eventi, prodotti o risultati.
- Se un'affermazione della persona ti sembra gonfiata, chiedi (fa parte della critica).

## File

| File | Quando leggerlo |
|---|---|
| `references/stile.md` | sempre, prima di costruire: principi, misure, bianco e nero, cosa evitare |
| `references/schemi.md` | durante la costruzione: copertina, persone, fila di loghi, scena, apertura del cliente, schemi, opzioni |
| `references/concetti.md` | quando c'è un concetto complesso: intervista, opzioni, grammatica degli schemi |
| `references/asset.md` | per loghi, foto, font, colori, icone |
| `references/verifica.md` | prima di consegnare |
| `assets/template/` | la base di ogni deck (motore, cornice, mattoni) |
| `assets/esempio/` | il deck di riferimento, completo (marchi inventati) |
| `scripts/foto.py`, `scripts/controlla.py`, `scripts/font.py` | foto dei passi, controllo automatico, font offline |
