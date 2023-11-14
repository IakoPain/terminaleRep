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
def parentheses(txt):
    for i in range(len(txt)):
        if txt[i] == "(":
            p.empiler("(")
        if txt[i] == ")":
            p.depiler
    if p.estVide() == False:
        return "False"
    else:
        return"True"

parentheses("())))()()()()()(")

