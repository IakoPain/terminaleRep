# Recherche des chaînes entre 2 sommets d'un graphe
# sans passer 2 fois par le même sommet
# Créé par fmartin, le 29/04/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class File:
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defiler(self):
        if self.vide():
           return "File vide"
        else:
            return self.L.pop(0)

    def enfiler(self,x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        if self.vide():
           return "File vide"
        else:
            return self.L[0]

    def present(self,x):
        return x in self.L

    def afficher(self):
        print("   File f: ", end="")
        if not self.vide():
            for val in range (self.taille()):
                print(self.L[val], end=" ")
        else:
            print("File vide", end=" ")

def voisins(Graphe,sommet):
    return Graphe[sommet]

def rechercheChaine(Graphe, depart, fin):
    f = File()
    f.enfiler((depart, [depart]))

    while not f.vide():
        (tmp, path) = f.defiler()

        for voisin in voisins(Graphe,tmp):
            if ....... not in path:
                if voisin == ...... :
                    print("Chaîne :", path + [voisin])
                else:
                    f.enfiler((voisin, path + .........))

#Représentation avec matrice d'adjacence
M = [[0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]]

Graphe = nx.Graph(np.array(M))
nouveaux_noms = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
Graphe = nx.relabel_nodes(Graphe, nouveaux_noms) #Renomer les sommets d'un graphe

matrice = nx.adjacency_matrix(Graphe) #Créer un graphe avec une matrice d'adjacence
print("Matrice d'adjacence :")
print(matrice.todense())
print()

pos=nx.spring_layout(Graphe)
nx.draw_networkx(Graphe,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()

depart = 'B'
fin = 'G'
print("Liste des chemins entre ", depart, " et ", fin, ":")
rechercheChaine(Graphe, depart, fin)
