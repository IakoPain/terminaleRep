# Créé par iako.pain, le 16/11/2023 en Python 3.7
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

def calculer(a,b,op):
    if op=='+':
        resultat=a+b
    elif op=='-':
        resultat=a-b
    elif op=='*':
        resultat=a*b
    elif op=='/':
        if a!=0:
            resultat=a/b
        else:
            print("erreur division par zéro")
    return resultat

p=Pile()
def polonaise(txt):
    for i in range (len(txt)):
        if txt[i] == "+" or txt[i] == "-" or txt[i] == "*" or txt[i] == "/":
            b=p.depiler()
            a=p.depiler()
            r=calculer(a,b,txt[i])
            p.empiler(r)
        else:
            p.empiler(txt[i])
    return p.sommet()

print(polonaise([2,3,'-']))
print(polonaise([2,3,'*']))
print(polonaise([2,3,'+',4,'*']))
print(polonaise([4,3,2,'*','/']))
