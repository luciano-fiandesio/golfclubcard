# Golf card generator

## Installazione

```
brew install pdftk-java

pip3 install pypdftk
```

## Come lanciare il programma

`fill.py [arg1] [arg2]`

esempio:

`./fill.py names.txt card.pdf`

Il programma accetta due argomenti.
Il **primo** argomento è il nome del file contenente i nominativi da usare per riempire il campo del file pdf.
Il file di nomi deve contenere solo linee con nome e cognome. Esempio:

```
Marco Rossi
Paolo Verdi
...
```

Il programma converte tutti i nomi in lettere maiuscole.

Il **secondo** argomento è il nome del file pdf da modificare.

Nota bene: il programma si aspetta che il campo da modificare all'interno del pdf abbia il nome `name_lastname`.

