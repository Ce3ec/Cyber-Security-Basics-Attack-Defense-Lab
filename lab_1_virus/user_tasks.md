## Task 1 - Spyware visibile

Imposta la variabile 
```python
HIDDEN = False.
```

Genera uno “spyware”.

Questo tipo di malware punta a rubare informazioni. È facile pensare che debba
sempre utilizzare trucchi complessi per nascondersi, ma non è sempre così.

Molti malware non sono né offuscati né nascosti: spesso si limitano a infilarsi
in cartelle specifiche del sistema, dove risiedono già altri file con permessi
simili. In questo modo riescono a eludere anti-virus molto semplici senza troppo
sforzo.

---

## Task 2 - Spyware nascosto

Imposta la variabile 
```python
HIDDEN = True.
```

Genera uno “spyware nascosto”.

Questa è la forma più basilare che introduce il concetto di “nascosto”.
Nella realtà, però, i malware tendono più spesso a nascondersi tramite
offuscamento del codice, cioè distorcendo il proprio contenuto in modo che non
sia facilmente riconoscibile.

Questa strategia mira a eludere i controlli basati su funzioni, accessi o pattern
utilizzati dagli anti-virus.

Verifica:
- se il file esiste
- se è visibile nel file manager

---

## Task 3 - Manipolazione della sandbox

Crea manualmente almeno 3 sottocartelle in sandbox/test_environment.

Genera uno spyware (a tua scelta).

Facciamo finta che questo ambiente di test rappresenti un sistema reale.
In un PC vero esistono moltissime cartelle, ognuna con tantissimi file.

Cercare un singolo file che agisce in modo sospetto o che contiene codice
malevolo diventa una vera e propria sfida per un anti-virus. In alcuni casi può
anche essere una corsa contro il tempo per cercare di fermarne l’esecuzione.

Per questo molti malware, soprattutto quelli amatoriali, cercano di nascondersi
in cartelle profonde, spesso creando anche copie nascoste in luoghi completamente
differenti.

---

## Task 4 - Rootkit base

Imposta
```python
NUMERO_DELLE_COPIE a 1
RANDOM_HIDE a False
```

Genera un rootkit.

A volte i malware possono usare dei “bait”, cioè malware facilmente
identificabili che servono a distrarre l’anti-virus, mentre altri componenti
rimangono nascosti o continuano a operare indisturbati.

---

## Task 5 - Rootkit avanzato

Imposta
```python
NUMERO_DELLE_COPIE a 2
RANDOM_HIDE a True
```

Esegui il rootkit.

Esistono malware che hanno il compito di facilitare l’accesso di altri malware
o di migliorarne l’elusione. Questo è particolarmente problematico perché
l’anti-virus deve individuare malware diversi tra loro, in luoghi differenti e
con tecniche di occultamento differenti.

---

## Task 6 - Hash e firme statiche

- Calcola l’hash di due malware dello stesso tipo
- Verifica se coincidono
- Modifica una sola riga del contenuto
- Ricalcola l’hash

Come abbiamo visto, due file identici hanno lo stesso hash. Per questo i malware
tendono a distorcere il proprio codice in modi differenti, rendendo più difficile
il riconoscimento di pattern, firme e funzioni note.

---

## Task 7 - Trojan

DA FARE

---

## Task 9 - Design task

Modifica il contenuto dei “malware”. Se riesci, utilizza stringhe randomiche o
prova a criptare una parola o una frase a tua scelta in modi differenti.

Questo simula una forma base di offuscamento di un virus. Con queste modifiche
diventa molto più difficile per un anti-virus basilare riconoscere il malware
utilizzando solo firme statiche.
