if __name__ == "main":
    
        try:
            import defs
            from colorama import Back, Fore, Style, init, deinit
            init(autoreset=True)
        except:
            print(f"\n[!] Error: Import of modules failed")
            exit(None)


        print("\n")


        print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Hop hop hop, arrêtez vous içi, avant d'aller plus loin, j'aurais besoin d'une piéce d'identité.\n\n")

        print("\033[4mPiéce d'identité\033[0m\n")
        nom_prenom = defs.demander_nom_prenom()
        age = defs.demander_age()
        nationalite = defs.demander_nationatlite()
        raison_venue = defs.demander_raison_venue(nom_prenom)
        print(f"{Fore.MAGENTA + Style.NORMAL}Garde{Style.RESET_ALL} : Tout me semble bon, vous pouvez passé.\n")


        pensee_une = defs.demander_pensee_une()


        print("\n")

