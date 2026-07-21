class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree
        self.prix = prix
        self.actif = actif

    def afficher(self):
        print(f"ID: {self.numero} | Nom: {self.nom} | Succursale: {self.succursale} | Durée: {self.duree} mois | Prix: {self.prix}$/mois | Actif: {self.actif}")
        class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree 
        self.prix = prix        
        self.actif active   

    @property
    def numero(self):
        return self._numero

    @property
    def nom(self):
        return self._numero

    @property
    def succursale(self):
        return self._succursale

    @property
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self, valeur):
        if valeur > 0:
            self._duree = valeur
        else:
            print("Erreur : Durée invalide.")

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, valeur):
        if valeur > 0:
            self._prix = valeur
        else:
            print("Erreur : Prix invalide.")

    @property
    def actif(self):
        return self._actif

    @actif.setter
    def actif(self, valeur):
        if str(valeur).strip().lower() in ['oui', 'non']:
            self._actif = str(valeur).strip().capitalize()
        else:
            print("Erreur : Statut actif invalide.")

    def afficher(self):
        print(f"ID: {self.numero} | Nom: {self.nom} | Succursale: {self.succursale} | Durée: {self.duree} mois | Prix: {self.prix}$/mois | Actif: {self.actif}")
        class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier
        
        class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach
        class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach


Python
class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        super().afficher()
        print(f" Casier ": {self.casier}")

class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach

    def afficher(self):
        super().afficher()
        print(f"  Coach personnel" : {self.coach}")
        

