import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Paintris')


white=(255,255,255)
pink=(223, 3, 252)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
turq=(0,206,209)
yello=(255,236,0)
purp=(101, 0, 207)

gravity = 1
forceDrop = False
#currYCoord=10

tetrominoList=["I","Z","S","T"]


floor = pygame.draw.line(gameDisplay, white, (0,520),(800,520),3)



nxtPc=random.choice(tetrominoList)

"""
while True:
    if """


"""
while True:
    gameDisplay.blit(tBlock,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update() 

"""

"""
tetrominoDict = {
    "T_Piece" : 8,
    "I_Piece" : 4,  
    "Z_Piece" : 8,
    "S_Piece" : 8
}
"""

#square = pygame.draw.polygon(gameDisplay, blue, ((20,20),(40,20),(40,40),(20,40)))

def tetroPlacer(piece,currYCoord):
    if piece == "I":
        IPiece=((20,20),(40,20),(40,100),(20,100))
        drawI = pygame.draw.polygon(gameDisplay, turq, IPiece)
    elif piece == "Z":
        ZPiece=((20,20),(60,20),(60,40),(80,40),(80,60),(40,60),(40,40),(20,40))
        drawZ = pygame.draw.polygon(gameDisplay, pink,ZPiece)
    elif piece == "S":
        SPiece=((20,40),(40,40),(40,20),(80,20),(80,40),(60,40),(60,60),(20,60),(20,40))
        drawS = pygame.draw.polygon(gameDisplay, green,SPiece)
    elif piece == "T":
        TPiece=((20,20),(80,20),(80,40),(60,40),(60,60),(40,60),(40,40),(20,40))
        drawT = pygame.draw.polygon(gameDisplay, red,TPiece)
    else:
        print(piece)
        
#for pixel cut-offs, can draw another shape in the same shape in black pen, and update everytime piece updates? update frame after that?





def pieceMover(gravity,forceDrop):
    #change y axis of tetromino by size of 1 'pixel' (gravity) number of times per second
    #for as long as forceDrop is true, and gravity is less than or equal to 5, set gravity to 5
    tetroPlacer(nxtPc,gravity)







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update() 
