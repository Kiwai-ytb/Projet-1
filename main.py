
# Importe les différentes bibliotèques requises ou différents modules
import defs
from colorama import Back, Fore, Style, init, deinit


# Initialise les composant de la blibliothèque colorama
init(autoreset=True)


# Créer un espace pour plus de visibilité
print("\n")


# Permet au joueur de créer son personnage
print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Hop hop hop, arrêtez vous içi, avant d'aller plus loin, j'aurais besoin d'une piéce d'identité.\n\n")

print("\033[4mPiéce d'identité\033[0m\n")
nom_prenom = defs.demander_nom_prenom()
age = defs.demander_age()
nationalite = defs.demander_nationatlite()
raison_venue = defs.demander_raison_venue(nom_prenom)
print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Tout me semble bon, vous pouvez passé.\n")


# Appelle la fonction créer dans le module defs appeller pensee_une
pensee_une = defs.demander_pensee_une()


# Créer un espace pour plus de visibilité
print("\n")
