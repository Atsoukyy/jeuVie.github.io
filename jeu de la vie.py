"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import *
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 6
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

FPS=144   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)
BLEU=(0,0,255)
cellcolor=BLEU
grillecolor=NOIR
background_color=NOIR


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
        pygame.draw.line(fenetre,grillecolor,(0+i,0),(0+i,700),1)
    for j in range(0,WINDOWHEIGHT+1,CELLSIZE):
        pygame.draw.line(fenetre,grillecolor,(0,0+j),(1366,0+j),1)
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    vie = {}
    
    for i in range(0,nbCellWidth,1):
        for j in range(0,nbCellHeight,1):
            vie[(i,j)]=0
           
   
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
            pygame.draw.rect(fenetre, background_color, (x, y, CELLSIZE, CELLSIZE))
        if vie[item] == 1:
            pygame.draw.rect(fenetre, cellcolor, (x, y, CELLSIZE, CELLSIZE))

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
'''''
def voisins(item,vie):
    nbVoisins = 0
    for x in range (-1,2):
        for y in range (-1,2):
            xv=item[0]+x
            yv=item[1]+y

            
    return nbVoisins
    '''
def voisins(item, vie):
 
    nbVoisins = 0
    xv=item[0]
    yv=item[1]
    for li in (xv - 1, xv, xv + 1):
        for lj in (yv - 1, yv, yv + 1):
            if li>=0 :
                if lj>=0 :
                    if li<=nbCellWidth-1:
                        if lj<=nbCellHeight-1:
                            if vie[li,lj] == 1 :
                                
                                nbVoisins += 1
                            else:
                                pass
    if vie[item]==1:
        nbVoisins-=1
    
 
    return nbVoisins

#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaineEtape(vie):
    nouvelleVie = {}
    p=1
    for item in vie:
        nbv=voisins(item,vie)
        if nbv>=4:
            nouvelleVie[item]=0
        elif nbv<=1:
            nouvelleVie[item]=0
        elif nbv==3: #                     Ne marche pas, ne donne pas vie ?????
            nouvelleVie[item]=p
        elif nbv==2:
            nouvelleVie[item]=vie[item]
        
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
            if event.key == pygame.K_UP:    #est-ce la touche UP si animation est DéSACTIVER
                #vie=generationAleatoire(vie)
                vie=prochaineEtape(vie)     #manuel
            if event.key ==pygame.K_w:
                loop=False

    fenetre.fill(background_color)
    remplirGrille(vie)
    tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    vie=prochaineEtape(vie)  #pour une animation !!!!!!
    clock.tick(FPS)

pygame.quit()

#endregion