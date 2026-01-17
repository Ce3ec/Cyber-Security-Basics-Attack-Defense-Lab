import os
import hashlib
import shutil
import sys
import time

# TODO: creare le costanti per l'ambiente (cartelle ecc)
# TODO: fare un ciclo che va su tutta la cartella

PERCORSO_DELLA_CARTELLA = './sandbox/test_environment' 
CARTELLA_DI_QUARANTENA = "quarantine"
# Hash malevolo fornito (corrisponde al file example_virus.py della repository)
MALICIOUS_HASH = "1296c5120af205deb94461a82bd75fd8cc9a014c52bb13deb2d0135d07829ea7"

def lista_files()->list:
    '''
    Ritorna la lista di tutti i files all'interno di sandbox/test_environment
    '''
    files = []

    for root, _, filenames in os.walk(PERCORSO_DELLA_CARTELLA):
        for name in filenames:
            files.append(os.path.join(root, name))

    return files

def calculate_sha256(file_path:str):
    """Calcola l'hash SHA256 di un file"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Leggi il file in blocchi per gestire file grandi
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Errore nella lettura del file {file_path}: {e}")
        return None

def antivirus_scan(files:list[str], current_script:str, quarantine_dir:str):

    if len(files) == 0:
        print("Nella cartella non ci sono files")
        return 0, 0

    files_scanned = 0
    threats_found = 0
    
    for filename in files:
        # 1. Salta lo script stesso (in caso sia nella stessa cartella)
        if filename == current_script:
            continue
            
        # 2. Salta i file vuoti (0 byte) per evitare falsi positivi
        if os.path.getsize(filename) == 0:
            print(f"File: {filename} -> SALTATO (File vuoto)")
            print("-" * 30)
            continue

        file_hash = calculate_sha256(filename)
        
        if file_hash:
            files_scanned += 1
            print(f"File: {filename}")
            print(f"Hash SHA256: {file_hash}")
            
            # Controllo se l'hash corrisponde a quello malevolo
            if file_hash == MALICIOUS_HASH:
                print(f"ATTENZIONE: File {filename} è MALEVOLO!")
                
                # Sposta il file nella cartella quarantine
                try:
                    # Aggiungi timestamp al nome per evitare conflitti
                    base_name, extension = os.path.splitext(filename)
                    timestamp = time.strftime("%d_%m_%Y_%H_%M")
                    new_filename = f"{base_name}_{timestamp}{extension}"
                    os.rename(filename, new_filename)
                    quarantine_path = os.path.join(quarantine_dir, new_filename)
                    
                    shutil.move(new_filename, CARTELLA_DI_QUARANTENA)
                    print(f"File spostato in: {quarantine_path}")
                    threats_found += 1
                except Exception as e:
                    print(f"Errore nello spostamento del file: {e}")
            else:
                print("File sicuro")
            
            print("-" * 30)

    return files_scanned, threats_found

def main():

    # Nome del file di script corrente per non auto-scansionarsi
    current_script = os.path.basename(__file__)
    
    # Crea cartella quarantine se non esiste
    if not os.path.exists(CARTELLA_DI_QUARANTENA):
        os.makedirs(CARTELLA_DI_QUARANTENA)
    
    # Lista file nella directory
    files = lista_files()

    print("=" * 50)
    print(f"Path:", PERCORSO_DELLA_CARTELLA)
    print("SCANSIONE ANTIVIRUS IN CORSO...")
    print("=" * 50)
    
    files_scanned, threats_found = antivirus_scan(files, current_script, CARTELLA_DI_QUARANTENA)
    
    print("=" * 50)
    print("SCANSIONE COMPLETATA")
    print(f"File scansionati: {files_scanned}")
    print(f"Minacce rilevate: {threats_found}")
    print("=" * 50)
    
    if threats_found > 0:
        print(f"I file malevoli sono stati spostati nella cartella '{CARTELLA_DI_QUARANTENA}'")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScansione interrotta dall'utente.")
    
    # Impedisce la chiusura immediata della finestra su Windows
    if sys.platform.startswith('win'):
        print("\nPremi INVIO per uscire...")
        input()

