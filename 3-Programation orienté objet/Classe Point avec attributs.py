
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


p=Point(8,18)
print("A(", p.x, ",", p.y, ")")
p.translater(2,-3)
print("A(", p.x, ",", p.y, ")")
