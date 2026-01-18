import os
import platform
import subprocess

from send2trash import send2trash

def codice_dentro(numero_delle_copie:int=1, hide_children:bool=False):
    '''
    Docstring for crea_malware
    
    :param nome_malware: Il nome che avrà il file "malware"
    :type nome_malware: str
    :param messaggio: Il testo all'interno del file "malware"
    :type messaggio: str
    '''

    return f"""
    import os
    import random as rand
    from pathlib import Path
    import platform
    import subprocess

    PERCORSO_DELLA_CARTELLA = './sandbox/test_environment'
    LOG_PATH = './lab_1_virus/virus.log'

    def nascondi_malware(percorso_file)->None:
        '''
        Nasconde i file dal gestore file
        
        :param percorso_file: Il percorso specifico del "malware"
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

    def crea_malware(nome_malware:str, messaggio:str='', hide:bool=False, estensione:str='.txt')->None:
        '''
        Docstring for crea_malware
        
        :param nome_malware: Il nome che avrà il file "malware"
        :type nome_malware: str
        :param messaggio: Il testo all'interno del file "malware"
        :type messaggio: str
        :param hide: Se True il malware sarà invisibile al gestore file (se non è attivata l'opzione elementi nascosti)
        :type hide: bool
        :param estensione: L'estensione del file
        :type estensione: str
        '''

        cartelle = lista_cartelle()
        print(cartelle)
        print(len(cartelle))

        if not cartelle:
            base_percorso = os.path.join(PERCORSO_DELLA_CARTELLA, nome_malware)
        else:
            base_percorso = os.path.join(rand.choice(cartelle), nome_malware)

        percorso_completo = Path(f"{{base_percorso}}{{estensione}}")

        i = 0
        while percorso_completo.exists():
            percorso_completo = Path(f"{{base_percorso}}_{{i}}{{estensione}}")
            i += 1

        print(percorso_completo)
        with open(percorso_completo, "w", encoding="utf-8") as file:
            file.write(messaggio)

        with open(LOG_PATH, "a") as f:
                f.write(str(percorso_completo)+'\\n')

        if hide:
            nascondi_malware(percorso_completo)


    for x in range({numero_delle_copie}):
        crea_malware("Virus", "Grazie per avermi fatto entrare {{random_name}} :)", {hide_children})
    """

def nascondi_malware(percorso_file:str)->None:
    '''
    Nasconde i file dal gestore file
    
    :param percorso_file: Il percorso specifico del "malware"
    :type percorso_file: str
    '''

    sistema = platform.system()

    if sistema == "Windows":
        subprocess.run(["attrib", "+h", percorso_file], shell=True)
    else:
        directory, nome = os.path.split(percorso_file)

        if not nome.startswith("."):
            os.rename(percorso_file, os.path.join(directory, "." + nome))

def lista_cartelle(percorso_della_cartella:str)->list:
    '''
    Ritorna la lista di tutte le cartelle all'interno di sandbox/test_environment

    :param percorso_della_cartella: Il percorso della cartella sandbox
    :type percorso_della_cartella: str

    :return: Lista delle cartelle list[str]
    '''
    cartelle = []

    for root, dirs, _ in os.walk(percorso_della_cartella):
        for d in dirs:
            cartelle.append(os.path.join(root, d))

    return cartelle

def rimuovi_malware(percorso_logs:str):
    '''
    Cerca nel file di log tutti i percorsi validi dei file generati e li mette nel cestino in modo sicuro
    (in modo da evitare di eliminare permanentemente file errati)

    :param percorso_logs: Percorso del file di log
    :type percorso_logs: str
    '''

    with open(percorso_logs, "r", encoding="utf-8") as f:
        righe = f.readlines()

    if len(righe) <= 1:
        return

    intestazione = righe[0]
    percorsi = [r.strip() for r in righe[1:] if r.strip()]

    for percorso in percorsi:
        try:
            if os.path.exists(percorso):
                send2trash(percorso)
        except Exception:
            pass

    with open(percorso_logs, "w", encoding="utf-8") as f:
        f.write(intestazione)