class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueurDuCote=longueur
        self.largeurDuCote=largeur

    def aire(self):
        return self.longueurDuCote*self.largeurDuCote

    def perimetre(self):
        return self.longueurDuCote*2+self.largeurDuCote*2

    def __repr__(self):
        return ("A="+str(self.aire())+" , P="+str(self.perimetre())+" )")

c1=Rectangle(15,10)
print(c1.aire())
print(c1.perimetre())
