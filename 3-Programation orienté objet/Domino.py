class Domino:
    def __init__ (self,domino):
        self.face1=domino[0]
        self.face2=domino[1]

    def affichePoints(self):
        return self.face1 + self.face2

    def _repr_(self):
        return ("Face 1 :"+str(self.face1())+", Face 2 ="+str(self.face2()))

d1=Domino((2,6))
d1.affichePoints()
d2=Domino((4,3))
d2.affichePoints()
print("total des points :", d1.valeur() + d2.valeur())
print(d1)
