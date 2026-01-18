import os
import random as rand
import subprocess
import sys

from pathlib import Path
from helpers import lista_cartelle, nascondi_malware, codice_dentro, rimuovi_malware

# TODO: creare una funzione che prende le path da virus.log ed elimina quei file (se li trova)

# Percorsi
PERCORSO_DELLA_CARTELLA = './sandbox/test_environment' # Il "malware" non uscira da questa cartella, consigliamo di NON cambiarla.
LOG_PATH = './lab_1_virus/virus.log'

# Costanti
NUMERO_DELLE_COPIE = 1 # Questo è il numero di copie che farà il "malware", STATE MOLTO ATTENTI A QUANTE NE METTETE, soprattuto se lo eseguite nel vostro sistema.

HIDDEN = False
RANDOM_HIDE = True

# Attributi
ATTRIBUTO_NASCOSTO = 0x02

# Funzioni malware
def crea_malware(nome_malware:str, messaggio:str='', hide:bool=False, estensione:str='.txt')->None:
    '''
    Questa funzione crea un file con un'estensione e un contenuto con la possibilità di nasconderlo dall'esplora file per simulare tecniche di camuffamento o di elusione avanzate
    
    :param nome_malware: Il nome che avrà il file "malware"
    :type nome_malware: str
    :param messaggio: Il testo all'interno del file "malware"
    :type messaggio: str
    :param hide: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hide: bool
    :param estensione: L'estensione del file
    :type estensione: str
    '''

    cartelle = lista_cartelle(PERCORSO_DELLA_CARTELLA)
    print(cartelle)
    print(len(cartelle))

    if not cartelle:
        base_percorso = os.path.join(PERCORSO_DELLA_CARTELLA, nome_malware)
    else:
        base_percorso = os.path.join(rand.choice(cartelle), nome_malware)

    percorso_completo = Path(f"{base_percorso}{estensione}")

    i = 0
    while percorso_completo.exists():
        percorso_completo = Path(f"{base_percorso}_{i}{estensione}")
        i += 1

    print(percorso_completo)
    with open(percorso_completo, "w", encoding="utf-8") as file:
        file.write(messaggio)

    with open(LOG_PATH, "a") as f:
            f.write(str(percorso_completo)+'\n')

    if hide:
        nascondi_malware(percorso_completo)

# ---

# Funzioni comportamento malware

# TODO: da migliorare, la struttura è fragile e l'esecuzione a runtime può rompersi, in oltre generare un .exe in runtime è lento e creerebbe cartelle aggiuntive con le risorse
def trojan(hidden:bool=False, hide_children:bool=False)->None:
    '''
    Crea un file 'infetto' che all'apertura genera NUMERO_DELLE_COPIE "malware"
    
    :param hidden: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hidden: bool
    :param hide_children: Se True i malware generati da quello principale saranno invisibili al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hide_children: bool
    '''
    names = ['Tseam', 'Witch', 'NotFreeGame', 'TrustMe']
    random_name = rand.choice(names)

    # Questo è il codice che verrà passato ai "malware" generati 
    code = codice_dentro(NUMERO_DELLE_COPIE, hide_children)

    crea_malware(random_name, code, hidden, estensione='.py')

    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        f"{random_name}.py"
    ])

def spyware(hidden:bool=False)->None:
    '''
    Crea un "malware" che si nasconde all'interno della cartella 'test_environment'
    
    :param hidden: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hidden: bool
    '''
    
    crea_malware('Spyware', 'Ti sto spiando 👀', hidden)

def rootkit(hidden:bool=True, hide_children:bool=True)->None:
    '''
    Crea un "malware" il quale genera NUMERO_DELLE_COPIE malware per poi nasconderle all'interno di 'test_environment'
    
    :param hidden: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hidden: bool
    :param hide_children: Se True i malware generati da quello principale saranno invisibili al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hide_children: bool
    '''

    crea_malware('RootKit', 'Shhhhh non fatevi sentire...', hidden)

    for _ in range(NUMERO_DELLE_COPIE):
        if hide_children:
            if rand.randrange(0,10) > 5:
                crea_malware(f'Virus', 'Shhhhh...', hide_children)
                continue

        crea_malware(f'Virus', 'Shhhhh...')

def main()->None:

    funzioni = [
            lambda: trojan(HIDDEN, RANDOM_HIDE), 
            lambda: spyware(HIDDEN), 
            lambda: rootkit(True, RANDOM_HIDE)
            ]

    while True:
        print('Inserisci la tipologia di "malware" che vuoi creare:')
        print('1. Trojang')
        print('2. Spyware')
        print('3. RootKit')
        print('4. Distruggi tutti i "malware"')
        print('5. Esci')
        print('\n')
        x = input(">")

        try:
            x = int(x)

            if x>5 or x<=0:
                os.system('cls')
                print("Errore: Inserire un valore fra 1 e 4")
                continue

            if x == 4:
                os.system('cls')
                rimuovi_malware(LOG_PATH)
                continue

            elif x == 5:
                exit(0)

            else:
                os.system('cls')
                malware = funzioni[x-1]
                malware()
                continue

            break

        except:
            os.system('cls')
            print("Errore: Inserire un valore valido")
    
    

if __name__ == '__main__':

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("Questo file tiene traccia dei percorsi dei virus che hai generato in qualsiasi contesto (in caso non li riuscissi a trovare)\n")
    
    os.makedirs(PERCORSO_DELLA_CARTELLA, exist_ok=True)

    main()