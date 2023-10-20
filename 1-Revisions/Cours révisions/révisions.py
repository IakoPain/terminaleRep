#Exercice 2.2.1
'''
operande=int(7)
for n in range(1,21):
    print(operande,"*",n,"=",n*operande)
'''
#Exercice 2.2.2
"""
operande=int(7)
for n in range(1,21):
    if n*operande%3==0:
        print(operande,"*",n,"=",n*operande,"*")
    else:
        print(operande,"*",n,"=",n*operande)
"""
#Exercice 2.2.3
"""
euro=1
dollar=1.12
while euro<=1024:
    print(euro,"€ =",dollar, "$")
    euro=euro*2
    dollar=dollar*2
"""
#Exercice 2.2.4
"""
o=int(input("nombre svp"))
for i in range (0,15):
    print(o)
    o=o*3
"""
#Exercice 3.2.3
"""
o=int(input(""))
for n in range(1,13):
    print(o)
    o=o*3
"""
#Exercice 3.3
"""
def triangle(hauteur):
for h in range(1,hauteur+1): for c in range(1,h+1):
print('*',end='') print()

triangle(5)
"""
"""
def triangle(hauteur):
    for h in range(hauteur+1,1,-1):
         for c in range(h+1,2,-1):
            print('*',end='')
         print()

triangle(5)
"""
#Exercice 4.2
"""
def rechercheMin(lst):
    a=0
    for n in range(1,len(lst)):
        a+=lst[n]
    return a/len(lst)

lst=[20,8,9,2,35,49]
print(rechercheMin(lst))
"""
#Excercice 5.2.1
"""
noms= ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

for n in range(len(noms)):
    print(noms[n],len(noms[n]))

"""
#-------------------------------------------------------------------------------
#                               Révisions
#-------------------------------------------------------------------------------

# Exercice 3

"""
euro=int(input("Montant a convertir"))
dollar=1.07310
print(euro,"€ =",dollar*euro, "$")
"""
"""
# Exercice 4
heure =int(input("HEURE"))
minute=int(input("MINUTE (stp)"))
secondes=int(input("secondeS"))

heure=heure*60*60
minute=minute*60
total=heure+minute+secondes
print(total)
"""
# Exercice 5
"""
menu="0"
nb1=int(input("Nombre1"))
nb2=int(input("Nombre2"))
while menu!='q':
    print("------------------------------------------------------------")
    print("1 : Addition")
    print("2 : Soustraction")
    print("3 : Multiplication")
    print("4 : Division")
    print("q : Quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    if menu== "1":
        print("------------------------------------------------------------")
        print(nb1 + nb2)
        print("------------------------------------------------------------")
    if menu== "2":
        print("------------------------------------------------------------")
        print(nb1 - nb2)
        print("------------------------------------------------------------")
    if menu== "3":
        print("------------------------------------------------------------")
        print(nb1 * nb2)
        print("------------------------------------------------------------")
    if menu== "4":
        if nb2 == 0:
            print("------------------------------------------------------------")
            print ("errur")
            print("------------------------------------------------------------")
        else :
            print("------------------------------------------------------------")
            print(nb1 / nb2)
            print("------------------------------------------------------------")

"""
#Exercice 6
from math import *
a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
d=b*b-4*a*c
if d>0:
    s1=(-b-sqrt(d))//(2*a)
    s2=(-b+sqrt(d))//(2*a)
    print("Soluce 1 -> ",s1,", Soluce 2 -> ",s2,)
elif d==0:
    s=-b/(2*a)
    print("Solution -> ",s)
else :
    print("ya pas")

"""
#Exercice 7
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 3, 4, 6], [2, 3, 5, 1])

plt.show()
"""
"""
# Exercice 8
a=int(input("Point A"))
b=int(input("Point B"))
a2=int(input("Point A\'"))
b2=int(input("Point B\'"))
x=-((b2-b)/(a2-a))
y=a*x+b
print("les coordonnées sont",x, y)
"""
"""
# Exercice 11
genre=input("Genre ??")
taille=(int(input("Taille ?")))
if genre =="m":
    print("Poids idéal",taille -100-(taille-150)/4)
if genre =="f":
    print("Poids idéal",taille -100-(taille-150)/2.5)
"""
# Exericice 12
"""
decimal = int(input("NOMBRE ICI" ))
binaire = bin(decimal)
print(binaire)
"""