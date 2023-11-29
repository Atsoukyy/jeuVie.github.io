"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import *
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
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
global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE

clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)
#endregion





#Trace la grille
def tracerGrille():
    for i in range(0,WINDOWWIDTH+1,CELLSIZE):
        pygame.draw.line(fenetre,ROUGE,(0+i,0),(0+i,480),1)
    for j in range(0,WINDOWHEIGHT+1,CELLSIZE):
        pygame.draw.line(fenetre,ROUGE,(0,0+j),(640,0+j),1)
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    vie = {}
    
    for i in range(0,nbCellWidth,1):
        for j in range(0,nbCellHeight,1):
            vie[(i,j)]=[0]
           
   
    return vie



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(vie):
    for i in range(0,nbCellWidth):
        for j in range(0,nbCellHeight):
            vie[(i,j)]=randint(0,1)
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

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
def voisins(item,vie):
    nbVoisins = 0
    for x in range (-1,2):
        for y in range (-1,2):
            #A complÃ©ter
            pass
    return nbVoisins

#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaineEtape(vie):
    nouvelleVie= {}
    for item in vie:
        #recupÃ¨re le nombre de voisins d'une cellule
        #A complÃ©ter
        pass

    return nouvelleVie



vie=initialiserCellules()
vie=generationAleatoire(vie)

#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                vie=prochaineEtape(vie)     #manuel

    fenetre.fill(NOIR)
    remplirGrille(vie)
    tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    vie=prochaineEtape(vie)  #pour une animation
    clock.tick(FPS)

pygame.quit()

#endregion