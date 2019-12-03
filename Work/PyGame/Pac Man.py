### SRC - Nearly there, just need to fix the direction and add colour attribute.

import pygame
import random
import math

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (46,204,113)
ORANGE = (211,84,0)
PURPLE = (125,60,152)
AQUA = (22,160,133)
PINK = (255,89,222)
COLOUR = [WHITE,BLUE,YELLOW,RED,GREEN,ORANGE,PURPLE,AQUA,PINK]

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen

size = (500,500)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("PAC MAN")

# -- My Classes

        

##class Wall(pygame.sprite.Sprite):
##    def __init__():
        




class PacMan(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.surface = screen
        self.colour = YELLOW
        self.x = x
        self.y = y
        self.radius = 5
        self.direction_x = 0
        self.direction_y = 0

    def create_pac(self):
        self.character = pygame.draw.circle(self.surface,self.colour, (self.x,self.y), self.radius, 0)

    def direction_x(self,val):
        val = int(val)
        self.direction_x = val
    def direction_y(self,val):
        val = int(val)
        self.direction_y = val
    

player = PacMan(250,300)




    
game_over = False


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
               player.direction_x(-1)
            elif event.key == pygame.K_RIGHT:
                player.direction_x(1)
            elif event.key == pygame.K_UP:
                player.direction_y(-1)
            elif event.key == pygame.K_DOWN:
                player.direction_y(1)
            #end if
        elif event.type == pygame.KEYUP:
            player.direction_x(0)
            player.direction_y(0)
                
        #End If
    
                 
    # -- Game logic goes after this comment
   
    # -- Text
    font = pygame.font.Font('freesansbold.ttf',15)
        
    

    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Display text
    
    # -- Draw here
    player.create_pac()
    


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()

##while not game_over:

