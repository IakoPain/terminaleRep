# Comparaison des performances de deux algorithme de tris (insersion et fusion)
# un tableau

import time
import random
import sys

N=5000         #longueur du tableau
VALEUR_MAX=50   #valeur maximale pouvant être contenue dans le tableau
sys.setrecursionlimit(10000)

def creationValeursNonTrie(N):  #fonction de génération d'un tableau de valeurs aléatoires
    tableau=[]
    for indice in range(0,N):
        tableau.append(random.randint(1,VALEUR_MAX))
    return tableau


def tri_insersion(lst):
    for i in range(0,len(lst)):
        j=i
        while j>0 and lst[j-1]>lst[j]:
            lst[j-1], lst[j]= lst[j],lst[j-1]
            j-=1


def fusion(lst_gauche,lst_droit):
    if lst_gauche==[]:
        return lst_droit
    if lst_droit==[]:
        return lst_gauche
    if lst_gauche[0]<lst_droit[0]:
        return [lst_gauche[0]]+fusion(lst_gauche[1:],lst_droit)
    else:
        return [lst_droit[0]]+fusion(lst_gauche,lst_droit[1:])



def triFusion (lst):
    if len(lst)==1:
        return (lst)
    else:
        milieu=len(lst) // 2
        lst_gauche=triFusion(lst[:milieu])
        lst_droit=triFusion(lst[milieu:])
        return (fusion(lst_gauche, lst_droit))


tab=creationValeursNonTrie(N)   #génération d'un tableau de valeur aléatoire
print("tri par insersion")
debut = time.time()             #mémorisation de l'heure de début
tri_insersion(tab)
fin = time.time()               #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)

debut = time.time()             #mémorisation de l'heure de début
print("tri fusion")
triFusion(tab)
fin = time.time()               #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)





