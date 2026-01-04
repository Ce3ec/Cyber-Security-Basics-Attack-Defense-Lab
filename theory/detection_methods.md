# Detection Methods

Questo documento descrive i principali metodi utilizzati dagli antivirus
per rilevare malware e attività sospette.

## Signature-Based Detection

### Descrizione
Metodo basato sul confronto tra file analizzati e un database di firme note.

### Vantaggi
- Veloce
- Preciso per malware conosciuti
- Basso consumo di risorse

### Svantaggi
- Inefficace contro malware nuovi o modificati
- Dipende dagli aggiornamenti

## Heuristic Detection

### Descrizione
Analizza la struttura e le istruzioni di un file per individuare pattern sospetti.

### Vantaggi
- Può rilevare malware sconosciuti
- Non dipende esclusivamente dalle firme

### Svantaggi
- Maggiore probabilità di falsi positivi
- Più costosa in termini di risorse

## Behavior-Based Detection

### Descrizione
Monitora il comportamento dei programmi durante l'esecuzione.

Esempi:
- Modifica del registro
- Accesso sospetto alla memoria
- Creazione di processi anomali

### Vantaggi
- Efficace contro zero-day
- Rileva attività malevole reali

### Svantaggi
- Richiede monitoraggio continuo
- Può rallentare il sistema

## Sandboxing

### Descrizione
Esecuzione del file in un ambiente isolato per osservarne il comportamento.

### Vantaggi
- Elevata sicurezza
- Analisi approfondita

### Svantaggi
- Lenta
- Alcuni malware rilevano il sandbox e si nascondono

## Machine Learning / AI-Based Detection

### Descrizione
Utilizza modelli statistici addestrati su grandi quantità di dati.

### Vantaggi
- Ottima contro malware sconosciuti
- Migliora nel tempo

### Svantaggi
- Complessità elevata
- Possibili bias o errori del modello

## Cloud-Based Detection

### Descrizione
Invia hash o campioni sospetti a server remoti per l'analisi.

### Vantaggi
- Database sempre aggiornato
- Ridotto carico locale

### Svantaggi
- Dipendenza dalla connessione internet
- Questioni di privacy

## Hybrid Detection

### Descrizione
Combina più tecniche di rilevamento.

### Vantaggi
- Maggiore accuratezza
- Migliore copertura delle minacce

### Svantaggi
- Maggiore complessità
- Possibile aumento del consumo di risorse

## Falsi positivi e falsi negativi

- **Falso positivo**: file legittimo rilevato come malware
- **Falso negativo**: malware non rilevato

Un buon antivirus cerca di bilanciare sicurezza e usabilità.

## Conclusione

Nessun metodo di rilevamento è sufficiente da solo.
L'efficacia di uno scanner anti-malware dipende dalla combinazione intelligente
di più tecniche.
