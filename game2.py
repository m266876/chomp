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

#load our game font
custom_font = pygame.font.Font("assets/fonts/28 Days Later.ttf", 90)


def draw_background(surf):
    #load our tiles
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()


    #png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))

    #seagrass randomly at the bottom of the beach
    for _ in range(7):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height-tile_size*2))

#draw the text
        text = custom_font.render("Chomp", True, (255,0,0))
        surf.blit(text, (screen_width/3, screen_height/3-text.get_height()/.5))


def draw_fishes(surf):
    #load some fish tiles from sprites
    green_fish = pygame.image.load("assets/sprites/green_fish.png")
    green_fish.set_colorkey((0,0,0)) #set png transparency
    orange_fish = pygame.image.load("assets/sprites/orange_fish.png")
    orange_fish.set_colorkey((0,0,0))
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png")
    puffer_fish.set_colorkey((0,0,0))
    green_fish = pygame.transform.flip(green_fish, True, False)
    orange_fish = pygame.transform.flip(orange_fish, True, False)
    puffer_fish = pygame.transform.flip(puffer_fish, True, False)

    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(0, screen_height-tile_size)
        x1 = random.randint(0, screen_width - tile_size)
        y1 = random.randint(0, screen_height - tile_size)
        x2 = random.randint(0, screen_width - tile_size)
        y2 = random.randint(0, screen_height - tile_size)
        surf.blit(green_fish, (x,y))
        surf.blit(orange_fish, (x1,y1))
        surf.blit(puffer_fish, (x2,y2))


#Main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
 #update the display
    pygame.display.flip()


#quitpygame
pygame.quit()

