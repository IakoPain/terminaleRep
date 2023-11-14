class Pile:
    def __init__(self):
        self.pile = []

    def __len__(self):
        return len(self.pile)

    def __repr__(self):
        return ' '.join([str(i) for i in self.pile])

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def estVide(self):
        vide=False
        if self.pile==[]:
            vide=True
        return vide

    def sommet(self):
        if not self.estVide():
            return self.pile[-1]
p = Pile()

p.empiler('A')
p.empiler('B')
p.empiler('C')
p.empiler('D')
print(p)
print('Le sommet de la pile est',p.sommet())
print('La liste est vide ?',p.estVide())
print('La longueur de la liste est :',len(p))
p.depiler()
p.depiler()
print(p.depiler())
p.empiler('C')
p.empiler('D')
print('La liste est vide ?',p.estVide())
print('La longueur de la liste est :',len(p))
print(p)