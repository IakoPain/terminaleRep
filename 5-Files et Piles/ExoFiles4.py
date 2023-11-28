from random import randint
class File:
    def __init__(self):
        self.file = []

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        return ' '.join([str(i) for i in self.file])

    def enfiler(self, element):
        self.file.append(element)

    def defiler(self):
        return self.file.pop(0)

    def estVide(self):
        vide=False
        if self.file==[]:
            vide=True
        return vide

    def sommet(self):
        if not self.estVide():
            return self.file[0]

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

def inversionFile(f):
    p=Pile()
    for i in range(len(f.file)):
        p.empiler(f.defiler())

    for i in range (len(p)):
        f.enfiler(p.depiler())

    return f


f=File()
f.enfiler(5)
f.enfiler(9)
f.enfiler(1)
f.enfiler(3)
print(f)
print(inversionFile(f))