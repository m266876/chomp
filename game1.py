import pygame
import sys
import random

#initalize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A beautiful beach in San Diego")

#function to draw a background

def draw_background(screen):
    #load our tiles
    water = pygame.image.load('sprites/water.png').convert()
    sand = pygame.image.load('sprites/sand_top.png').convert()
    seagrass = pygame.image.load('sprites/seagrass.png').convert()

    #png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height-tile_size))

    #seagrass randomly at the bottom of the beach
    for _ in range(7):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height-tile_size*2))



#Main loop
running = True
background = screen.copy()
draw_background(background)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
 #update the display
    pygame.display.flip()

#quitpygame
pygame.quit()

