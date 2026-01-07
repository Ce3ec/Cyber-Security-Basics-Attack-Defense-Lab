# Malware Simulation Framework - Explanation

Questo file Python simula il comportamento di diverse categorie di malware
(spyware, rootkit, trojan) all’interno di un **ambiente isolato (sandbox)**.

I malware generati sono **file completamente innocui** (testo o script),
creati esclusivamente nella cartella `sandbox/test_environment`.

Lo scopo del progetto è **didattico**:
studiare il comportamento dei malware e preparare l’implementazione
di un anti-virus basato su **firme statiche (hash)**.

---

## 1. Sandbox e contenimento

```python
PERCORSO_DELLA_CARTELLA = './sandbox/test_environment'
LOG_PATH = './lab_1_virus/virus.log'
```

Tutti i file vengono creati solo all’interno della sandbox.
Questo garantisce:

- nessun impatto sul sistema reale
- possibilità di analisi controllata
- facilità di rimozione

Il file virus.log registra il percorso di ogni malware creato ed è
fondamentale per simulare attività di incident response.

---

## 2. Variabili di configurazione
```python
Copia codice
NUMERO_DELLE_COPIE = 1
HIDDEN = False
RANDOM_HIDE = True
```

Queste variabili permettono di modificare il comportamento del malware
senza cambiare la logica interna delle funzioni.

- NUMERO_DELLE_COPIE simula la proliferazione
- HIDDEN abilita l’occultamento del malware
- RANDOM_HIDE introduce comportamento non deterministico

---

## 3. Funzioni di supporto
lista_cartelle()
Scansiona ricorsivamente la sandbox e restituisce tutte le sottocartelle.
Serve a simulare la dispersione del malware nel file system.

nascondi_malware(percorso_file)
Simula tecniche basilari di occultamento:

Windows → attributo hidden
Unix → prefisso .

Queste tecniche non forniscono sicurezza reale, ma simulano
comportamenti comuni nei malware.

---

## 4. Creazione del malware
crea_malware()
È la funzione centrale del framework.

Caratteristiche:
1. seleziona una cartella casuale
2. evita la sovrascrittura dei file
3. scrive il percorso nel log
4. può nascondere il file

Ogni malware:
- ha contenuto statico
- è identificabile tramite hash
- è tracciabile tramite virus.log

---

## 5. Tipologie di malware simulate
### Spyware
crea un singolo file
può essere nascosto
simula presenza silenziosa

### Rootkit
crea un malware principale
genera malware secondari
può nascondere i figli
simula persistenza e proliferazione

### Trojan
crea un file apparentemente legittimo
contiene codice che genera malware
rappresenta il concetto di fiducia compromessa

---

## 6. Collegamento con l’anti-virus
Poiché il contenuto dei malware non varia:
- l’hash rimane stabile
- è possibile usare firme statiche
- si possono studiare limiti e vantaggi di questo approccio
