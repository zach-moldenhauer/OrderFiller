# Simple pygame program


# Import and initialize the pygame library

import pygame

from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONUP,
    K_w,
    K_a,
    K_s,
    K_d,
)

#variables for map creation

tileGap = 0
tileHeight =  100
tileWidth = 100
tileSize = (tileWidth,tileHeight)
truckSize = (int(tileWidth * .5), int(tileHeight * .5))

xPlace = 100
yPlace = 100

xTruck = 300
yTruck = 750

truckSpeed = 5


mapLevel = [["end","o","end","o","end"],
            ["mid","o","mid","o","mid"],
            ["mid","o","mid","o","mid"],
            ["mid","o","mid","o","mid"],
            ["beg","o","beg","o","beg"]]
            




def moveForward(x,y):

    position = palletTruck.get_rect()
    screen.blit(background, position, position)
    screen.blit(palletTruck, (x, y))

    
    print(y)
   


def pallet(x,y):
    screen.blit(palletImg, (x,y))
    
def endSteel(x,y):
    screen.blit(steelEnd, (x,y))
    
def midSteel(x,y):
    screen.blit(steelMid, (x,y))
    
def begSteel(x,y):
    screen.blit(steelBeg, (x,y))
    
def concreteFloor(x,y):
    screen.blit(concrete, (x,y))
    
def truck(x,y):
    screen.blit(palletTruck, (x,y))
    





pygame.init()


# Set up the drawing window

#images and display pieces

quitButton = pygame.Rect(0,0,20,20)    

palletTruck = pygame.image.load('Sprites/Pallet Truck.png')
palletTruck = pygame.transform.scale(palletTruck,truckSize)


palletImg = pygame.image.load('Sprites/Wood Pallet.png')
palletImg = pygame.transform.scale(palletImg,tileSize)

steelEnd = pygame.image.load('Sprites/Steel End.png')
steelEnd = pygame.transform.scale(steelEnd,tileSize)

steelMid = pygame.image.load('Sprites/Steel Middle.png')
steelMid = pygame.transform.scale(steelMid,tileSize)

steelBeg = pygame.image.load('Sprites/Steel Start.png')
steelBeg = pygame.transform.scale(steelBeg,tileSize)

concrete = pygame.image.load('Sprites/Concrete Floor.png')
    
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screen.fill((185, 180, 171))
    
pygame.draw.rect(screen, pygame.Color(255,0,0) , quitButton)
    

for row in mapLevel:
    for col in row:
    
        
        if(col == "end"):
            endSteel(xPlace,yPlace)
            
        if(col == "mid"):
            midSteel(xPlace,yPlace)
        
        if(col == "beg"):
            begSteel(xPlace,yPlace)
            
        if(col == "o"):
            concreteFloor(xPlace,yPlace)
        
        
        xPlace = xPlace + tileWidth + tileGap
        
        
    yPlace = yPlace + tileHeight
    xPlace = tileSize[0]


background = screen

#place truck
truck(xTruck, yTruck)

# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():
    
        if event.type == MOUSEBUTTONUP:
        
            if(pygame.mouse.get_pos()[0] <= 20 and pygame.mouse.get_pos()[1] <= 20):
                running = False
            print(pygame.mouse.get_pos())


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
                
    if keys[pygame.K_w]:
        yTruck = yTruck - truckSpeed
        moveForward(xTruck, yTruck)
    

    # Flip the display
    
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(100)

# Done! Time to quit.

pygame.quit()