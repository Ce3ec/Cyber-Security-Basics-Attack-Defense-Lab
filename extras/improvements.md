# Miglioramenti delle Prestazioni

### Caching dei Risultati di Scansione
Evitare la riconsiderazione di file immutati mantenendo un database persistente di hash verificati e timestamp di modifica per ridurre il carico I/O(Input/Output).

```text
SE il file non è stato modificato dall'ultima volta
ALLORA considera il file sicuro e non analizzarlo
ALTRIMENTI esegui la scansione completa del file e aggiorna la data dell'ultimo controllo
```

### Gestione Risorse Adattiva
Modulare l'utilizzo della CPU in base allo stato del sistema, riducendo la priorità dei thread di scansione durante l'uso intensivo da parte dell'utente.

```texta
SE l'utente sta giocando o usando programmi pesanti
ALLORA metti in pausa le scansioni automatiche
ALTRIMENTI esegui le scansioni in background e usa la velocità normale della CPU
```

### Offloading Analisi in Cloud
Demandare l'analisi pesante di euristica avanzata e sandbox a server remoti per minimizzare l'impatto sulle risorse locali.

```text
SE il file è troppo grande o complesso da analizzare
ALLORA invia i dati al server cloud per il controllo e attendi il verdetto dal cloud
ALTRIMENTI controlla il file direttamente sul computer
```

# Miglioramenti sulla Sicurezza

### Protezione Anti-Ransomware Proattiva
Implementare un sistema di monitoraggio del file system in tempo reale che intercetti operazioni di crittografia massiva e avvii procedure di backup shadow istantaneo.

```text
SE un programma inizia a cifrare molti file velocemente
ALLORA blocca immediatamente quel programma e crea una copia di sicurezza dei file avvisa subito l'utente
```

### Isolamento della Rete
Configurare il **firewall locale** per bloccare tutto il traffico in uscita tranne quello verso la console di gestione in caso di rilevamento di minacce critiche.

```text
SE viene rilevato un virus molto pericoloso
ALLORA blocca tutte le connessioni internet
MA mantieni attiva la connessione per l'amministratore e isola il computer dalla rete aziendale
```
