from math import pi,sqrt
class Cercle:
    def __init__(self,centre,rayon):
        self.CentreCercle=centre
        self.RayonCercle=rayon

    def perimetre(self):
        return pi*2*self.RayonCercle
    def aire(self):
        return pi*self.RayonCercle**2
    def testAppartenance(self,point):
        x=point[0]
        y=point[1]
        a=self.CentreCercle[0]
        b=self.CentreCercle[1]

        if sqrt((x-a)**2+(y-b)**2) <= self.RayonCercle:
            return "Vrai"
        else:
            return "False"

c1=Cercle((2,2),3)
print(c1.aire())
print(c1.testAppartenance((0,0)))
print(c1.testAppartenance((0,-1)))