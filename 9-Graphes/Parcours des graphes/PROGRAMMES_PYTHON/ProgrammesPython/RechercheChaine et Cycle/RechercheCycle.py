# Recherche des cycles d'un graphe à partir d'un sommet
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

def voisins(graphe,sommet) :
    return graphe[sommet]

def rechercheCycle(graphe) :
    etatCycle = False
    for key in graphe:
        depart = key
        f = ..........
        f.enfiler((depart, []))

        while not ........... :
            (tmp, path) = f.defiler()

            for voisin in voisins(graphe,tmp) :
                if voisin not in .......... :
                    if (voisin == depart and len(path) >= ......):
                        print("Cycle du graphe :", [depart] + path + [voisin])
                        etatCycle = True
                    else:
                        f.enfiler((voisin, path + [voisin]))
    return etatCycle


#Représentation avec matrice d'adjacence
M = [[0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]]


graphe = nx.Graph(np.array(M))
nouveaux_noms = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
graphe = nx.relabel_nodes(graphe, nouveaux_noms) #Renomer les sommets d'un graphe

matrice = nx.adjacency_matrix(graphe) #Créer un graphe avec une matrice d'adjacence
print("Matrice d'adjacence :")
print(matrice.todense())
print()

pos=nx.spring_layout(graphe)
nx.draw_networkx(graphe,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()

etatCycle = rechercheCycle(graphe)
if etatCycle == False:
    print("Le graphe n'a pas de cycle")
