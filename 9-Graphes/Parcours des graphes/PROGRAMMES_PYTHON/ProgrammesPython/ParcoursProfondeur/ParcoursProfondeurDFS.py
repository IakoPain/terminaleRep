# Parcours en profondeur d'un graphe
# Créé par fmartin, le 09/04/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Pile:
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def depiler(self):
        if self.vide():
           return "Pile vide"
        else:
            return self.L.pop()

    def empiler(self,x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        if self.vide():
           return "Pile vide"
        else:
            return self.L[-1]

    def present(self,x):
        return x in self.L

    def afficher(self):
        print("   Pile p: ", end="")
        if not self.vide():
            for val in range (self.taille()):
                print(self.L[val], end=" ")
        else:
            print("Pile vide", end=" ")

def voisins(graphe,sommet):
    print("   Voisins:", end=" ")
    for edge in graphe[sommet]:
        print(edge,end=" ")
    return graphe[sommet]

def parcoursDFS(graphe,sommet):
    sommets_visites = []
    p = Pile()
    sommets_visites.append(sommet)
    p.empiler(sommet)
    print("Avant la boucle :",end="")
    print("  Sommets visités:",sommets_visites, end="")
    p.afficher()
    print()

    print("Dans la boucle :")
    while not p.vide():
        tmp = p.sommet()
        print("  tmp =", tmp, end="")
        listeVoisinsNonVisites = [y for y in voisins(graphe,tmp) if y not in sommets_visites]
        print("   Voisins non visités:", listeVoisinsNonVisites, end="")
        if listeVoisinsNonVisites != []:
            v=listeVoisinsNonVisites[0]
            sommets_visites.append(v)
            p.empiler(v)
            print("   v =", v, end="")
            print("   Sommets visités:", sommets_visites, end="")
        else:
            p.depiler()
            print("   v =", v, end="")
            print("   Sommets visités:", sommets_visites, end="  ")

        p.afficher()
        print()
        print()
    return sommets_visites


#Représentation avec dictionnaire
dict = {
'A': ['B','C'],
'B': ['A','D','E'],
'C': ['A','D'],
'D': ['B','C','E'],
'E': ['B','D','F','G'],
'F': ['E','G'],
'G': ['E','F','H'],
'H': ['G']
}

graphe=nx.Graph(dict) #Créer un graphe avec le dictionnaire

matrice = nx.adjacency_matrix(graphe)
print("Matrice d'adjacence :")
print(matrice.todense())
print()

pos=nx.spring_layout(graphe)
nx.draw_networkx(graphe,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()

parcoursProfondeur=parcoursDFS(graphe,'D')
print()
print("Parcours en profondeur : ", parcoursProfondeur)
