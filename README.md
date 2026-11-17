# Aura Pitch Deck

Un plugin di Claude Code che fa presentazioni HTML in stile keynote alla Steve Jobs: chi presenta parla,
sullo schermo c'è pochissimo testo, a ogni clic compare una cosa sola. Loghi e foto sono quelli ufficiali,
le animazioni hanno un senso e i concetti difficili diventano schemi che si muovono. Quando il pitch è per
un cliente, la seconda parte prende i suoi colori e il suo logo.

La struttura e i concetti li decidi tu. Il plugin li chiede prima di costruire e non li propone mai,
perché la prima scaletta che leggi diventa quella giusta anche quando non è la tua. Poi la critica, con
domande, e fa la resa.

## Come funziona

1. **Domande.** Chi guarda, quanto dura, fondo bianco o nero, i marchi, la struttura (le slide in ordine,
   con quello che chi guarda deve capire da ognuna), le prove (loghi, foto, numeri con fonte), i concetti
   complessi.
2. **Critica della struttura.** Osservazioni slide per slide: doppioni, affermazioni gonfiate, prove che
   mancano, troppa roba per il tempo. Non riscrive la tua scaletta.
3. **Concetti complessi.** Ti chiede di spiegarli bene, poi se vuoi più opzioni o ti fidi della prima. Le
   opzioni sono costruite davvero e si sfogliano con il tasto O.
4. **Costruzione e verifica.** Parte da un template collaudato, fotografa ogni passo e lo controlla prima
   di consegnarti la cartella.

Il risultato è una cartella con `index.html` che si apre con un doppio clic, funziona senza rete e si
stampa in PDF (tasto P).

## Installazione

Serve Claude Code. Dentro Claude Code:

```
/plugin marketplace add alessandrodiaz1000/aura-pitch-deck-plugin
/plugin install aura-pitch-deck@aura-pitch-deck
```

Poi riavvia Claude Code. Per le versioni nuove: `/plugin marketplace update aura-pitch-deck`.

Gli script di controllo girano su Mac e usano Google Chrome, ImageMagick e Poppler:

```
brew install imagemagick poppler
```

## Uso

Scrivi per esempio "mi serve una presentazione aura per il pitch di giovedì", oppure lancia
`/aura-pitch-deck:aura-pitch-deck`.

Nella presentazione: frecce, spazio o clic per andare avanti; F schermo intero; P versione da stampare;
O e T per sfogliare e confrontare le opzioni di una slide.

## Cosa c'è dentro

- `skills/aura-pitch-deck/SKILL.md`: il flusso.
- `references/`: stile, schemi pronti, concetti complessi, loghi e foto, verifica.
- `assets/template/`: la base di ogni deck (motore, cornice, mattoni).
- `assets/esempio/`: un deck completo con marchi inventati (rombo × marea).
- `scripts/`: foto dei passi, controllo automatico, font scaricati per l'uso senza rete.

I font dell'esempio (Bricolage Grotesque, Urbanist) hanno licenza SIL Open Font License; le icone vengono
da Lucide (licenza ISC).
