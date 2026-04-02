import pygame #import the library
from sys import exit
pygame.init() #initiates all pygame functions
width,height = 670,675
screen = pygame.display.set_mode((width,height)) #display surface, your 'canvas'
pygame.display.set_caption("ZentinelY2K")
clock = pygame.time.Clock()
running = True
test_surface = pygame.Surface((25,25))
test_surface.fill('Red')
while running:
    for event in pygame.event.get(): #get events
        if event.type == pygame.QUIT:
            print("You closed the game")
            exit()
    screen.blit(test_surface,(width/2,height/2))
    pygame.display.update()
    clock.tick(60) 
    