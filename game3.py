import pygame
import sys
import random

from fish import Fish, fishes #importing a class and a Sprite group

#initalize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A beautiful beach in San Diego")

#load our game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf", 128)

def draw_background(surf):
    #load our tiles
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()

    green_fish=pygame.transform.flip(green_fish, True, False)
    orange_fish=pygame.transform.flip(orange_fish, True, False)
    puffer_fish=pygame.transform.flip(puffer_fish, True, False)


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
        surf.blit(text, (screen_width/2, screen_height/2-text.get_height()/2))

running = True
background = screen.copy()
draw_background(background)
#draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(0, screen_width-tile_size), random.randint(0, screen_height-tile_size)))

while running:
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
screen.blit(background, (0, 0))
fishes.draw(background)
# update the display
pygame.display.flip()

# quitpygame
pygame.quit()

