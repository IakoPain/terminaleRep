# Créé par Famille, le 28/02/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Représentation avec ajout sommets et arrêtes
G=nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_edge('A','B')
G.add_edge('A','C')
G.add_edge('A','D')
G.add_edge('B','A')
G.add_edge('B','D')
G.add_edge('C','A')
G.add_edge('C','D')
G.add_edge('C','E')
G.add_edge('D','A')
G.add_edge('D','B')
G.add_edge('D','C')
G.add_edge('D','E')
G.add_edge('D','F')
G.add_edge('E','C')
G.add_edge('E','D')
G.add_edge('E','F')
G.add_edge('F','D')
G.add_edge('F','E')

#A compléter



matrice = nx.adjacency_matrix(G)

#Affichage de la matrice d'adjacence
print("Matrice d'adjacence : ")
print(matrice.todense())
print()

#Affichage des sommets reliés par une arrête
print("Sommets reliés par une arrête :")
for edge in G.edges(data = False):
    print(edge)
print()

print("Nombre de noeuds et d'arrêtes : ",nx.info(G))

#Configuration et affichage de la représentation sagittale
pos=nx.spring_layout(G)
nx.draw_networkx(G,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()
