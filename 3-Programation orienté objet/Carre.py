class Carre:
    def __init__(self,longueur):
        self.longueurDuCote=longueur

    def aire(self):
        return self.longueurDuCote**2

    def perimetre(self):
        return self.longueurDuCote*4



c1=Carre(15)
print(c1.aire())
print(c1.perimetre())

