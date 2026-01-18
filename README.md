# ⚠️ Eng. DISCLAIMER & EDUCATIONAL USE ⚠️
This project is **for educational purposes only**. Please read the [full DISCLAIMER](DISCLAIMER.md) before using the code.
---

# Cyber Security Basics – Attack & Defense Lab 🛡

Questo progetto è un **laboratorio di cyber security** pensato per introdurre **le basi di malware e antivirus** attraverso la **pratica guidata**.

L’obiettivo è far comprendere come funziona un attacco informatico semplice e come una difesa basilare può individuarlo e contenerlo, **senza utilizzare codice dannoso reale**.

---

## Obiettivi del progetto

- Comprendere **cos’è un malware** e come è strutturato;
- Simulare il comportamento di un **virus innocuo**;
- Costruire un **antivirus base** (signature-based);
- Capire i **limiti delle difese semplici**;

Il progetto è pensato per appassionati di informatica con **conoscenze di base di programmazione**.

---

## ⚠️ Avvertenza importante ⚠️

Questo progetto ha **esclusivamente scopo educativo**.  
Il codice fornito **non è malware reale** e non deve essere modificato o utilizzato per scopi diversi da quelli didattici.

Si consiglia fortemente di:
- eseguire il codice **solo in un ambiente di test**;
- utilizzare una **cartella sandbox dedicata**;
- non eseguire script su sistemi di produzione.

Leggi attentamente il file [DISCLAIMER.md](DISCLAIMER.md) prima di iniziare.

---

## Struttura del progetto
```
cyber-attack-defense-lab/
│
├── lab_1_virus/ # Simulazione virus educativo
│   ├── example_virus.py
│   ├── explanation.md
│   └── user_tasks.md
│
├── lab_2_antivirus/ # Antivirus base
│   ├── example_antivirus.py
│   ├── explanation.md
│   ├── hash.bat
│   └── user_tasks.md
│
├── sandbox/ # Ambiente di test
│   └── test_environment/
│
├── theory/ # Concetti teorici
│   ├── malware_basics.md
│   ├── antivirus_basics.md
│   └── detection_methods.md
│
└── extras/
│   └── improvements.md
│
├── README.md
├── DISCLAIMER.md
```
---

## LAB 1 – Virus educativo (simulato)

In questo laboratorio l’utente imparerà:
- cos’è un malware e quali sono i suoi componenti principali;
- come funziona una **replicazione simulata**;
- cos’è una **firma** utilizzata per il riconoscimento.

Il “virus” creato:
- opera **solo all’interno della sandbox**;
- non si avvia automaticamente;
- non danneggia file reali;
- serve solo a **simulare comportamenti sospetti**.

---

## LAB 2 – Antivirus base

In questo laboratorio l’utente costruirà un antivirus molto semplice che:
- scansiona una directory;
- cerca firme note;
- identifica file sospetti;
- li sposta in quarantena.

Attraverso questo esercizio si comprenderà:
- come funziona il rilevamento a firme;
- perché gli antivirus possono fallire;
- il concetto di **false positive**.

---

## Estensioni possibili

- Migliorare il rilevamento antivirus;
- Aggiungere logging avanzato;
- Simulare tecniche di evasione;
- Confrontare diversi metodi di difesa;

Consulta la cartella `extras/` per idee future.
