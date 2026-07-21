membres = [membre1, membre2, membre3, membre4]

for membre in membres:
    membre.afficher()
    print("---------------------------")
    def sauvegarder_membres(membres):

    fichier = open("membres.txt", "w")

    for membre in membres:

        if isinstance(membre, MembreStandard):
            type_membre = "STANDARD"
        else:
            type_membre = "PREMIUM"

        ligne = (
            f"{type_membre};"
            f"{membre.numero};"
            f"{membre.nom};"
            f"{membre.succursale};"
            f"{membre.duree_abonnement};"
            f"{membre.prix_mensuel};"
            f"{membre.actif};"
            f"{membre.acces_entraineur}"
        )

        fichier.write(ligne + "\n")

    fichier.close()

    print("Les membres ont ete sauvegardes dans membres.txt")
    
    def charger_membres():

    membres = []

    fichier = open("membres.txt", "r")

    for ligne in fichier:

        infos = ligne.strip().split(";")

        if infos[0] == "STANDARD":
            membre = MembreStandard(int(infos[1]), infos[2], infos[3], int(infos[4]), int(infos[5]), infos[6], infos[7])
        else:
            membre = MembrePremium(int(infos[1]), infos[2], infos[3], int(infos[4]), int(infos[5]), infos[6], infos[7])

        membres.append(membre)

    fichier.close()

    return membres
def afficher_membres_actifs(membres):

    for membre in membres:
        if membre.actif == "Oui":
            membre.afficher()
            def afficher_membres_premium(membres):

    for membre in membres:
        if isinstance(membre, MembrePremium):
            membre.afficher()