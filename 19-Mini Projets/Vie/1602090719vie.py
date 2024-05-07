"""
Programme jeu de la vie réalisé par nom, prénom, classe
"""
import pygame
from random import *

#variables de l'écran
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 32
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

FPS=1   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)

clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)

#Trace la grille
def tracerGrille():
    #A compléter
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    vie = {}
    #A compléter
    return vie



#active aléatoirement les cellules (mise à 1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(vie):
    #A compléter
    return vie


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    for item in vie:
        x = item[0]
        y = item[1]
        y = y * CELLSIZE
        x = x * CELLSIZE
        if vie[item] == 0:
            pygame.draw.rect(fenetre, NOIR, (x, y, CELLSIZE, CELLSIZE))
        if vie[item] == 1:
            pygame.draw.rect(fenetre, VERT, (x, y, CELLSIZE, CELLSIZE))

#Détermine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
def voisins(item,vie):
    nbVoisins = 0
    for x in range (-1,2):
        for y in range (-1,2):
            #A compléter
            pass
    return nbVoisins

#calcule la prochaine étape, retourne un nouveau dictionnaire
def prochaineEtape(vie):
    nouvelleVie= {}
    for item in vie:
        #recupère le nombre de voisins d'une cellule
        #A compléter
        pass

    return nouvelleVie



vie=initialiserCellules()
vie=generationAleatoire(vie)

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                vie=prochaineEtape(vie)     #manuel

    fenetre.fill(NOIR)
    remplirGrille(vie)
    tracerGrille()
    pygame.display.update() #mets à jour la fentre graphique
    vie=prochaineEtape(vie)  #pour une animation
    clock.tick(FPS)

pygame.quit()


