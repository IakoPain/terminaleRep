
"""
import time
n=200
start=time.perf_counter()
while n>0:
    n=n//2
    print(n)
stop=time.perf_counter()

print (round(stop-start,6))
"""
#Exercice 1
"""
def moyenne(tab):
    total=0
    for n in range(len(tab)):
        total+=tab[n]
    total/=len(tab)
    return total

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5
"""
#Exercice 3

from math import *
Terrain=input("Terrain")
if Terrain == "Sec":
    def total(v):
        distance_r = v/3.6
        distance_f =(v**2)/200
        distance=distance_f+distance_r
        return distance
if Terrain == "Mouillé":
    def total(v):
        distance_r = v/3.6
        distance_f =(v**2)/200
        distance=distance_f+distance_r
        return distance*2
print(total(int(input("Vitesse"))))

# Exercice 4
"""
calcul la surface d'un disque en fonction du rayon

import doctest
from math import pi
def surfaceDisque(rayon):
---
    fonction qui retourne la surface d'un disque en fonction du rayon
    argument:
    rayon -- nombre
    >>> surfaceDisque(5)
    78.53981633974483
---
    return pi*rayon**2
print(surfaceDisque(5))
doctest.testmod()
"""
#Exercice 5
"""
Calcul de volume
"""
"""
import doctest
from math import pi

def volumeCylindre(rayon,hauteur):
    return hauteur*pi*rayon**2

def volumeSphere(rayon):
    return (4*pi*rayon**3)/3

doctest.testmod()

volumeRestantSansBille=volumeCylindre(30,58-50)

bille=0
volumeBilles=0

while volumeRestantSansBille>volumeBilles:
    bille+=1
    volumeBilles+=volumeSphere(bille)
    print("Nb de billes:",bille," Volume restant sans bille:",volumeRestantSansBille,"Volume des billes:", volumeBilles)
print("\n Il faut ",bille, " bille(s) pour que le récipient déborde.")
"""