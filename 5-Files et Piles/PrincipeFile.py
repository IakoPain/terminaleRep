def creer():
    enAttente=[]
    return enAttente

def longueur(enAttente):
    return len(enAttente)

def enfiler(enAttente,avion):
    enAttente.append(avion)

def defiler(enAttente):
    return enAttente.pop()

def estVide(enAttente):
    vide = "Faux"
    if enAttente == [] :
        vide == "Vrai"
    return (vide)

enAttente = creer()
enfiler(enAttente,'LH713')
enfiler(enAttente,'HP856')
enfiler(enAttente,'FR1745')
enfiler(enAttente,'AF644')
print(enAttente)
print('La liste est vide',estVide(enAttente))
print('Longueur =',longueur(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print('La liste est vide',estVide(enAttente))
print('Longueur =',longueur(enAttente))