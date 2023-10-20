class Equipe:
    def __init__(self,nom,nb_point):
        self.nom=nom
        self.point=nb_point

    def ajouter(self,point):
        self.point+=point

    def enleve_point(self,point):
        self.point-=point

    def __repr__(self):
        return self.nom+" "+str(self.point)

e=[]
e.append(Equipe("COP",10))
e.append(Equipe("RCM",0))
e.append(Equipe("Le Mans",14))
for n in range(0,len(e)):
    e[n].ajouter(1)
    print(e[n])