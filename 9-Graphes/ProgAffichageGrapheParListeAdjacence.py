# Créé par Famille, le 28/02/2024 en Python 3.7
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Représentation avec dictionnaire
dict = { ʹAʹ : [B,C,D],
ʹBʹ : [A,D],
ʹCʹ : [A,D,E],
ʹDʹ : [A,B,C,E,F],
ʹEʹ : [C,D,F],
ʹFʹ : [D,E]
}





#création  d'un graphe avec le dictionnaire
G=nx.Graph(dict)

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
