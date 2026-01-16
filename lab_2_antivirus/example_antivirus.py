import os
import hashlib
import shutil
import sys
import time

def calculate_sha256(file_path):
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

def main():

    # Hash malevolo fornito (corrisponde al file example_virus.py della repository)
    MALICIOUS_HASH = "f2139741036927659321599a111931aa53b015f684980e57bd328b96fea00817"
    
    # Nome del file di script corrente per non auto-scansionarsi
    current_script = os.path.basename(__file__)
    
    # Crea cartella quarantine se non esiste
    quarantine_dir = "quarantine"
    if not os.path.exists(quarantine_dir):
        os.makedirs(quarantine_dir)
    
    # Lista file nella directory corrente
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    print("=" * 50)
    print("SCANSIONE ANTIVIRUS IN CORSO...")
    print("=" * 50)
    
    files_scanned = 0
    threats_found = 0
    
    for filename in files:
        # 1. Salta lo script stesso
        if filename == current_script:
            continue
            
        # 2. FIX: Salta i file vuoti (0 byte) per evitare falsi positivi
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
                    timestamp = int(time.time())
                    new_filename = f"{base_name}_{timestamp}{extension}"
                    quarantine_path = os.path.join(quarantine_dir, new_filename)
                    
                    shutil.move(filename, quarantine_path)
                    print(f"File spostato in: {quarantine_path}")
                    threats_found += 1
                except Exception as e:
                    print(f"Errore nello spostamento del file: {e}")
            else:
                print("File sicuro")
            
            print("-" * 30)
    
    print("=" * 50)
    print("SCANSIONE COMPLETATA")
    print(f"File scansionati: {files_scanned}")
    print(f"Minacce rilevate: {threats_found}")
    print("=" * 50)
    
    if threats_found > 0:
        print(f"I file malevoli sono stati spostati nella cartella '{quarantine_dir}'")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScansione interrotta dall'utente.")
    
    # Impedisce la chiusura immediata della finestra su Windows
    if sys.platform.startswith('win'):
        print("\nPremi INVIO per uscire...")
        input()

