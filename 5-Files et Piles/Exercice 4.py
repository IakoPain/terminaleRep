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

p=Pile()
def polonaise(txt):
    for i in range (len(txt)):
        if txt[i] == "+":
            b=p.depiler()
            a=p.depiler()
            r=a+b
            p.empiler(r)
        elif txt[i] == "-":
            b=p.depiler()
            a=p.depiler()
            r=a-b
            p.empiler(r)
        elif txt[i] == "*":
            b=p.depiler()
            a=p.depiler()
            r=a*b
            p.empiler(r)
        elif txt[i] == "/":
            b=p.depiler()
            if b == 0:
                return p.sommet
            else:
                a=p.depiler()
                r=a/b
                p.empiler(r)
        else:
            p.empiler(txt[i])
    return p.sommet()

print(polonaise([2,3,'-']))
print(polonaise([2,3,'*']))
print(polonaise([2,3,'+',4,'*']))
print(polonaise([4,3,2,'*','/']))