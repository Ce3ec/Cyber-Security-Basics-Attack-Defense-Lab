# Malware Scanner Script - Documentazione Tecnica

Benvenuti nella documentazione tecnica del **example-antivirus**. Questo script Python è progettato per eseguire un'analisi statica basata su firme (hash SHA256) all'interno della directory di esecuzione.

---

## 📖 Indice
1. [Panoramica](#panoramica)
2. [Architettura del Software](#architettura-del-software)
3. [Funzionalità Chiave](#funzionalità-chiave)
4. [Logica di Quarantena](#logica-di-quarantena)
5. [Specifiche Tecniche](#specifiche-tecniche)

---

## 🔍 Panoramica
Il software opera come un **motore di scansione basato su hash**. Invece di analizzare il comportamento di un file (analisi dinamica), ne calcola l'impronta digitale univoca e la confronta con un database di firme note (analisi statica, in questo caso, il nostro database è una semplice stringa).



---

## 🏗️ Architettura del Software

### 1. Calcolo dell'Hash (SHA-256)
La funzione `calculate_sha256` utilizza la libreria standard `hashlib` per generare una stringa esadecimale di 64 caratteri.
* **Gestione della memoria**: Il file viene letto in "chunks" (blocchi) di **4096 byte**. Questo permette di processare file di grandi dimensioni senza saturare la memoria RAM del sistema.

### 2. Filtri di Scansione
Per ottimizzare le prestazioni ed evitare errori, lo script implementa tre filtri principali:
* **Self-Exclusion**: Lo script identifica il proprio nome file e si esclude dalla scansione.
* **Zero-Byte Filter**: I file vuoti vengono saltati per evitare calcoli inutili e potenziali falsi positivi.
* **Error Handling**: Se un file è bloccato dal sistema o non è leggibile, lo script cattura l'eccezione e prosegue con il file successivo.

---

## ☣️ Logica di Quarantena
Quando un file viene identificato come malevolo (ovvero il suo hash coincide con `MALICIOUS_HASH`), viene attivata la procedura di isolamento:

1. **Creazione Ambiente**: Viene verificata l'esistenza della cartella `quarantine/`. Se assente, viene creata automaticamente.
2. **Prevenzione Conflitti**: Per evitare che due file con lo stesso nome si sovrascrivano, viene applicato un **Unix Timestamp** al nome del file spostato.
   * *Esempio:* `example_virus.py` ➔ `quarantine/example_virus_1704384000.py`
3. **Spostamento Atomico**: Viene utilizzata la funzione `shutil.move()` per spostare fisicamente il file, rendendolo inoffensivo nella sua posizione originale.

---

## 🛠️ Specifiche Tecniche

| Componente | Tecnologia / Metodo |
| :--- | :--- |
| **Linguaggio** | Python 3.x |
| **Algoritmo Hash** | SHA-256 |
| **Librerie Core** | `os`, `hashlib`, `shutil`, `time` |
| **Metodo di Analisi** | Signature-based Detection |
| **Compatibilità** | Cross-platform (Windows, macOS, Linux) |

---

## 🚀 Come Eseguirlo
1. Assicurati di avere Python installato.
2. Posiziona lo script nella cartella che desideri scansionare.
3. Esegui il comando:
   ```bash
   python example_antivirus.py

---

# 🧷 Strumento: Calcolo Hash SHA256

Lo script batch 'hash.bat' per Windows permette di calcolare rapidamente l'impronta digitale (**hash**) di un file utilizzando l'algoritmo **SHA256**. È estremamente utile per verificare l'integrità dei file scaricati e assicurarsi che non siano stati alterati.
