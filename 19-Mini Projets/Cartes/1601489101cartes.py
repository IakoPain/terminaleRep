"""
Simulateur de jeu de 52 cartes
"""
from random import shuffle

class JeuDeCartes(object):

    def __init__(self):
        """Construction du jeu de carte"""
        self.carte = []  # Liste vide à remplir
        """Simulation d'un jeu de 52 cartes"""
        # Valeur des cartes
        self.valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
        # Couleur de la carte
        self.couleur = ["Pique", "Trèfle", "Carreau", "Coeur"]
        #A compléter

    def nomCarte(self, c):
        """Renvoie le nom de la carte (<c> doit être un tuple !!!)"""
        #A compléter

    def battre(self):
        """Mélange les cartes"""
        #A compléter

    def tirer(self):
        """Retire une carte du jeu"""
        #A compléter


#Q1 Initialisation de la classe « JeuDeCartes »
jeux = JeuDeCartes()
print(jeux.carte)

#Q2 Affichage du nom de la carte
jeux = JeuDeCartes()
jeux.nomCarte((1, 2))
jeux.nomCarte((12, 1))

#Q3 Battre les cartes
jeux = JeuDeCartes()
jeux.battre()
print(jeux.carte)

#Q4.1 Tirer une carte
jeux = JeuDeCartes()
jeux.battre()
print(jeux.carte)
c = jeux.tirer()
print(jeux.nomCarte(c))
print()
print(jeux.carte)

#Q4.2 Tirage de toutes le cartes
jeux = JeuDeCartes()
jeux.battre()
for n in range(53):
    """
    A compléter
    """


#Q5 Simuler un jeu de bataille entre 2 joueurs (robots)
jeuA = JeuDeCartes()
jeuB = JeuDeCartes()
jeuA.battre()
jeuB.battre()
comptA = 0
comptB = 0
#A compléter

