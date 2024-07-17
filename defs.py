
# Importe les différentes bibliotèques requises ou différents modules
from colorama import Back, Fore, Style, init, deinit


# Initialise les composant de la blibliothèque colorama
init(autoreset=True)


# Ce sont les différentes listes utilisaient dans ce module
list_non = ["non", "Non", "NON", "Non merci", "non merci", "NON MERCI"]


# Définit la demande de nom et de prénom du joueur
def demander_nom_prenom():
    while True:
        reponse_nom_prenom = input(f"   {Fore.CYAN + Style.NORMAL}Nom et Prénom : {Style.RESET_ALL}")
        mots = reponse_nom_prenom.split()
        if len(mots) >= 2:
            return reponse_nom_prenom
        else:
            print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Fore.RED} : Mhmm, n'avez vous pas de nom Mr {reponse_nom_prenom} ?{Style.RESET_ALL}")


# Définit la demande d'age du joueur
def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input(f"   {Fore.CYAN + Style.NORMAL}Age : {Style.RESET_ALL}")
        try:
            age_int = int(age_str)
        except ValueError:
            print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Fore.RED} : Mhmm, sur votre carte d'identité, il est inscrit que vous avez {age_str} ans.{Style.RESET_ALL}")
    return age_int


# Définit la demande de natoinalité du joueur
def demander_nationatlite():
    reponse_demander_nationalite = ""
    while reponse_demander_nationalite == "":
        reponse_demander_nationalite = input(f"   {Fore.CYAN + Style.NORMAL}Nationalité : {Style.RESET_ALL}")
    return reponse_demander_nationalite


# Définit la demande de la raison de la venue du joueur
def demander_raison_venue(reponse_nom_prenom):
    while True:
        reponse_raison_venue = input(f"\n{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Puis-je demander la raison de vôtre venue ? ")
        mots = reponse_raison_venue.split()
        if len(mots) >= 10:
            return reponse_raison_venue
        elif reponse_raison_venue in list_non:
            print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : ~Vraiment pas très commode ces gens...")
            break
        else:
            print(f"{Fore.RED + Style.NORMAL}Pouvez vous être un peu plus précis svp Mr {reponse_nom_prenom}.{Style.RESET_ALL}")