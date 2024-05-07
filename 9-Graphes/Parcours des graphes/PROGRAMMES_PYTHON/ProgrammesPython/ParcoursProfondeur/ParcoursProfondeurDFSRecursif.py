# Parcours en profondeur récursif d'un graphe
# Créé par fmartin, le 09/04/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def voisins(graphe,sommet):
    print("   Voisins:", end=" ")
    for edge in graphe[sommet]:
        print(edge,end=" ")
    return graphe[sommet]

def parcoursDFSrecursif(graphe,sommet,sommets_visites = None):
    if sommets_visites is None:
        sommets_visites = []
        print("Variables initiales:", end="")
        print("  Sommets visités:", sommets_visites, end="")
        print()

    if sommet not in sommets_visites:
        sommets_visites.append(sommet)
        print("  Sommet:", sommet, end="")
        print("  Sommets visités:", sommets_visites, end="")

        listeVoisinsNonVisites = [y for y in voisins(graphe,sommet) if y not in sommets_visites]

        print("   Voisins non visités:", listeVoisinsNonVisites, end="")
        print()
        print()
        for voisin in listeVoisinsNonVisites:
            parcoursDFSrecursif(graphe,voisin,sommets_visites)

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

parcoursProfondeur=parcoursDFSrecursif(graphe, 'D')
print()
print("Parcours en profondeur : ", parcoursProfondeur)

