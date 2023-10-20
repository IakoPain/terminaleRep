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

    def __repr__(self):
        """
        Affichage des attributs de la classe
        """
        return ("A( "+str(self.x)+" , "+str(self.y)+" )")

p=Point(2,14)
print(p)
p.translater(2,-3)
print(p)
