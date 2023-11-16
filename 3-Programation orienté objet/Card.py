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
        return f"CompteBancaire(titulaire='{self.titulaire}', solde={self.solde})"
