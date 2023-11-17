class CompteBancaire:
    def __init__(self, titulaire: str, solde: float):
        self.titulaire = titulaire
        self.solde = solde

    def crediter(self, montant: float):
        self.solde += montant

    def debiter(self, montant: float) -> bool:
        if self.solde >= montant:
            self.solde -= montant
            return True
        else:
            return False

    def __repr__(self):
        return f"Le compte de {self.titulaire} est de {self.solde} €"
"""
class CompteCheque(CompteBancaire):
    def __init__(self,nom,sommeInitiale,decouvert):
        super().__init__(nom,sommeInitiale)
        self.decouvertAutorise=decouvert

    def changerDecouvert(self,nouveauDecouvert):


    def debiter(self,montant): #surcharge
"""
compte=CompteBancaire("dupond",100)
compte.crediter(10)
print(compte)
print(compte.debiter(20)) # <--- UTILISE ça POUR LE Q4
print(compte)

comptes=[]
comptes.append(CompteBancaire("Stark",1000))
comptes.append(CompteBancaire("Banner",500))
comptes.append(CompteBancaire("Parker",700))
comptes.append(CompteBancaire("Rogers",600))
comptes.append(CompteBancaire("Wayne",1500))
comptes.append(CompteBancaire("Prince",2500))
