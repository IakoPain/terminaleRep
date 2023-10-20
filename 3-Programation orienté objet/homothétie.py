class Point:
    """
    Manipulation de points.
    """
    def __init__(self, abscisse, ordonnee):
        """
        Initialise le point avec les coordonnées indiquées
        """
        self.x, self.y = abscisse, ordonnee

    def translater(self, dx, dy):
        """
        Translate le point selon le vecteur (dx,dy)
        """
        self.x += dx
        self.y += dy

    def homothetie(self, k):
        """
        homothétie de centre (0,0) et de rapport k
        """
        self.x *= k
        self.y *= k

    def __repr__(self):
        """
        Affichage des attributs de la classe
        """
        return ("A( "+str(self.x)+" , "+str(self.y)+" )")

p=Point(3,4)
print(p)
p.homothetie(2)
print(p)
