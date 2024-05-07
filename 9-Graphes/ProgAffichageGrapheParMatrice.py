# Créé par Famille, le 28/02/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Représentation avec matrice d'adjacence
M = [[0,1,1,1,0,0],
     [1,0,0,1,0,0],
     [1,0,0,1,1,0],
     [1,1,1,0,1,1],
     [0,0,1,1,0,1],
     [0,0,0,1,1,0]] # Acompléter


G = nx.Graph(np.array(M))

#Changement des sommets identifiés par des chiffres en lettres
nouveaux_noms = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F'}
G = nx.relabel_nodes(G, nouveaux_noms)

matrice = nx.adjacency_matrix(G)

#Affichage de la matrice d'adjacence
print("Matrice d'adjacence : ")
print(matrice.todense())
print()

#Affichage des sommets reliés par une arrête
print("Sommets reliés par une arrête :")
for edge in G.edges(data = True):
    print(edge)
print()

print("Nombre de noeuds et d'arrêtes : ",nx.info(G))

#Configuration et affichage de la représentation sagittale
pos=nx.spring_layout(G)
nx.draw_networkx(G,pos,node_size=3050,font_size = 35,font_family ='arial',node_color='#FF0000',edge_color='#00FF00')
plt.show()
