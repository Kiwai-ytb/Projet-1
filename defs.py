
# Importe les différentes bibliotèques requises ou différents modules
from colorama import Back, Fore, Style, init, deinit
import time
import sys


# Initialise les composant de la blibliothèque colorama
init(autoreset=True)


# Ce sont les différentes listes utilisaient dans ce module
list_non = ["non", "Non", "NON", "Non merci", "non merci", "NON MERCI"]


# Definit une écriture plus réaliste avec du délai entre chaque lettre
def print_avec_animation(texte, delai=0.1):
    for char in texte:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delai)
    print()


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
            print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : ~Vraiment pas très commode ces gens...\n")
            break
        else:
            print(f"{Fore.RED + Style.NORMAL}Pouvez vous être un peu plus précis svp Mr {reponse_nom_prenom}.{Style.RESET_ALL}")


# Définit la première pensée du joueur
def demander_pensee_une():
    reponse_pensee_une = ""
    while reponse_pensee_une == "":
        print(f"{Fore.LIGHTGREEN_EX + Style.NORMAL}Toi{Style.RESET_ALL} : ~Je me demande si je dois rester içi... Ce garde pose trop de questions.\n")
        reponse_pensee_une = input("Réponse n°1 : Continuer a avancé malgré tout. \nRéponse n°2 : Faire demi tour immédiatement et rentré chez toi")
        if reponse_pensee_une == "1":
            print(f"{Fore.LIGHTGREEN_EX + Style.NORMAL}Toi{Style.RESET_ALL} : Bon... Moi je vais y aller Mr, au revoir..")
            exit(None)
        elif reponse_pensee_une == "2":
            print(f"\n{Fore.LIGHTGREEN_EX + Style.NORMAL}Toi{Style.RESET_ALL} : Finalement moi je vais rentré chez moi...\n")
            time.sleep(3)
            print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Ah bon ? Bien, au revoir Mr alors.")
        else:
            print(f"{Fore.RED + Style.NORMAL}Erreur 404{Style.RESET_ALL} : La réponse entrée n'existe pas.")
    return reponse_pensee_une
