# Verifica prima della consegna

Un deck non si consegna senza averlo guardato passo per passo. Le foto si aprono con lo strumento Read e
si guardano davvero: è l'unico modo di vedere sovrapposizioni, testo tagliato, loghi sgranati, cose che
restano accese quando non dovrebbero.

Gli script sono in `scripts/` della skill. Le foto vanno in una cartella temporanea (scratchpad), mai
nella cartella del deck o in una cartella sincronizzata (OneDrive, iCloud, Dropbox).

```bash
python3 scripts/controlla.py <deck>                     # errori e avvisi, e tutto il testo visibile per slide
python3 scripts/foto.py elenco <deck>                   # i passi: numero, slide, passo, etichetta
python3 scripts/foto.py passi <deck> <tmp> [DA-A]       # una foto per passo + foglio.png (3 per riga, ~come su Teams)
python3 scripts/foto.py movimento <deck> <N> <tmp>      # il movimento verso il passo N, avanti e indietro
python3 scripts/foto.py pdf <deck> <tmp>                # il PDF e le sue pagine
python3 scripts/foto.py provini <deck> <tmp>            # se ci sono opzioni: tutte affiancate
```

Nell'indirizzo del deck: `#7` apre il passo 7, `?still` toglie il movimento, `?play=500#7` ferma a 500 ms
il movimento verso il passo 7 (`&back` arrivando dal passo dopo), `?print` è la versione da stampare,
`?provini` il confronto delle opzioni, `?o=b` l'opzione b.

## Cosa guardare

1. `controlla.py` senza errori. Gli avvisi si leggono uno per uno: una frase lunga va accorciata, una
   foto piccola non va ingrandita.
2. Ogni passo nel foglio piccolo: si capisce in tre secondi? C'è un solo posto dove guardare?
3. A grandezza piena: allineamenti, niente sovrapposizioni, niente fuori dall'area utile (y 150-960),
   niente testo tagliato, loghi nitidi.
4. Il movimento dei passi che hanno un'entrata o un cambio: parte e arriva dove deve, avanti e
   indietro. Le scene a tutto schermo e l'apertura del cliente vanno guardate sempre.
5. Il PDF: le pagine da sole raccontano il deck, senza chi presenta.
6. Il testo visibile stampato da `controlla.py`, riletto parola per parola: ogni frase è vera, viene dai
   concetti della persona, non promette niente che non ci sia.

Se un elemento non si comporta come previsto, ricontrolla prima gli attributi (`data-from`,
`data-until`, `data-spot`, `data-slide`, `data-beat`) con `foto.py elenco`: quasi sempre è un numero di
passo sbagliato.
