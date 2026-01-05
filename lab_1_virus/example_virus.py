import os
import random as rand
import platform
import subprocess
import sys

# TODO: se i file sono già presenti la creazione da errore, creare sia un fallback e un check
# TODO: loggare le path di tutti i malware creati in virus.log
# TODO: creare una funzione che prende le path da virus.log ed elimina quei file (se li trova)

PERCORSO_DELLA_CARTELLA = './sandbox/test_environment' # Il "malware" non uscira da questa cartella, consigliamo di NON cambiarla.

NUMERO_DELLE_COPIE = 1 # Questo è il numero di copie che farà il "malware", STATE MOLTO ATTENTI A QUANTE NE METTETE, soprattuto se lo eseguite nel vostro sistema.

HIDDEN = False
RANDOM_HIDE = False
ATTRIBUTO_NASCOSTO = 0x02

def nascondi_malware(percorso_file)->None:
    '''
    Nasconde i file dal gestore file
    
    :param percorso_file: il percorso specifico del "malware"
    '''

    sistema = platform.system()

    if sistema == "Windows":
        subprocess.run(["attrib", "+h", percorso_file], shell=True)
    else:
        directory, nome = os.path.split(percorso_file)

        if not nome.startswith("."):
            os.rename(percorso_file, os.path.join(directory, "." + nome))

def lista_cartelle()->list:
    '''
    Ritorna la lista di tutte le cartelle all'interno di sandbox/test_environment
    '''
    cartelle = []

    for root, dirs, _ in os.walk(PERCORSO_DELLA_CARTELLA):
        for d in dirs:
            cartelle.append(os.path.join(root, d))

    return cartelle

def crea_malware(nome_malware:str, messaggio:str='', hide:bool=False)->str:
    '''
    Docstring for crea_malware
    
    :param nome_malware: il nome che avrà il file "malware"
    :type nome_malware: str
    :param messaggio: il testo all'interno del file "malware"
    :type messaggio: str
    '''

    cartelle = lista_cartelle()
    print(cartelle)
    print(len(cartelle))

    if not cartelle:
        percorso_completo = os.path.join(PERCORSO_DELLA_CARTELLA, nome_malware) + '.txt'
    else:
        percorso_completo = os.path.join(rand.choice(cartelle), nome_malware) + '.txt'

    with open(percorso_completo, "w", encoding="utf-8") as file:
        file.write(messaggio)

    if hide:
        nascondi_malware(percorso_completo)

    return percorso_completo

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

    code = f"""
from your_module import crea_malware

for x in range({NUMERO_DELLE_COPIE}):
    crea_malware(f"malware_{{x}}")
"""

    with open(f"{random_name}.py", "w") as f:
        f.write(code)

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
    
    percorso_completo = crea_malware('Spyware', 'Ti sto spiando 👀', hidden)

    with open("./virus.log", "a") as f:
            f.write(percorso_completo)

def rootkit(hidden:bool=True, hide_children:bool=True)->None:
    '''
    Crea un "malware" il quale genera NUMERO_DELLE_COPIE malware per poi nasconderle all'interno di 'test_environment'
    
    :param hidden: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hidden: bool
    :param hide_children: Se True i malware generati da quello principale saranno invisibili al gestore file (se non è attivata l'opzione elementi nascosti)
    :type hide_children: bool
    '''

    percorso_completo = crea_malware('RootKit', 'Shhhhh non fatevi sentire...', hidden)

    with open("./virus.log", "a") as f:
            f.write(percorso_completo)

    for x in range(NUMERO_DELLE_COPIE):
        percorso_completo = crea_malware(f'Virus_{x}', 'Shhhhh...', hide_children)

        with open("./virus.log", "a") as f:
            f.write(percorso_completo)

def main()->None:

    funzioni = [trojan, spyware, rootkit]

    while True:
        print('Inserisci la tipologia di "malware" che vuoi creare:')
        print('1. Trojang')
        print('2. Spyware')
        print('3. RootKit')
        print('4. Esci')
        print('\n')
        x = input(">")

        try:
            x = int(x)

            if x == 4:
                exit(0)

            elif x>4:
                print("Errore: Inserire un valore fra 1 e 4")
                continue

            break

        except:
            print("Errore: Inserire un valore valido")
    
    malware = funzioni[x-1]

    # TODO: modificare la logica che usano le funzioni per nascondere i file
    if RANDOM_HIDE:
        malware(RANDOM_HIDE)
    else:
        malware() #HIDDEN

if __name__ == '__main__':

    with open("./virus.log", "w") as f:
        f.write("")
    
    os.makedirs(PERCORSO_DELLA_CARTELLA, exist_ok=True)

    main()