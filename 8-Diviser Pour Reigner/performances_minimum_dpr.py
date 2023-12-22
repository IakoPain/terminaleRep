# Comparaison des performances de deux algorithme de recherche du minimum dans
# un tableau

import time
import random

N=1000000       #longueur du tableau
VALEUR_MAX=50   #valeur maximale pouvant être contenue dans le tableau


def creationValeursNonTrie(N):  #fonction de génération d'un tableau de valeurs aléatoires
    tableau=[]
    for indice in range(0,N):
        tableau.append(random.randint(1,VALEUR_MAX))
    return tableau

def minimum_parcours(lst):
    min=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min:
            min=lst[i]
    return min

def minimum_dpr(lst,d,f):
    if d==f:
        return lst[d]
    else:
        m=(d+f)//2
        x=minimum_dpr(lst,d,m)
        y=minimum_dpr(lst,m+1,f)
        if x<y:
            return x
        else:
            return y

tab=creationValeursNonTrie(N)   #génération d'un tableau de valeur aléatoire
print("parcours d'une liste")
debut = time.time()             #mémorisation de l'heure de début
print(minimum_parcours(tab))
fin = time.time()               #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)


debut = time.time()             #mémorisation de l'heure de début
print("méthode diviser pour regner")
print(minimum_dpr(tab,0,len(tab)-1))
fin = time.time()               #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)




