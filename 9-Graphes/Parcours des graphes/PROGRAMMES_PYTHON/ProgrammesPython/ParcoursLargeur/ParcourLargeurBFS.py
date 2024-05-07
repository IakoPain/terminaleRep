# Parcours en largeur d'un graphe
# Créé par fmartin, le 09/04/2024 en Python 3.7
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

def voisins(graphe,sommet):
    print("  Voisins:",end=" ")
    for edge in graphe[sommet]:
        print(edge,end=" ")
    return graphe[sommet]

def parcoursBFS(graphe,sommet):
    sommets_visites = []
    f = File()
    f.enfiler(sommet)
    print("Avant la boucle :",end="")
    print("  Sommets visités:",sommets_visites, end="")
    f.afficher()
    print()

    print("Dans la boucle :")
    while not f.vide():
        tmp = f.defiler()
        print("  tmp =", tmp, end="")
        if tmp not in sommets_visites:
            sommets_visites.append(tmp)
            print("   Sommets visités:", sommets_visites, end="  ")

        for voisin in voisins(graphe,tmp):
            if (voisin not in sommets_visites and not f.present(voisin)):
                f.enfiler(voisin)
        f.afficher()
        print()
    return sommets_visites

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
graphe = nx.relabel_nodes(graphe, nouveaux_noms)

matrice = nx.adjacency_matrix(graphe)
print("Matrice d'adjacence :")
print(matrice.todense())
print()

pos=nx.spring_layout(graphe)
nx.draw_networkx(graphe,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()

parcoursLargeur=parcoursBFS(graphe,'B')
print()
print("Parcours en largeur : ", parcoursLargeur)