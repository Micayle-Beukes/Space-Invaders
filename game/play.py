import pygame
import random
import math


# Initializing pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((1000, 750))

# Creating a background image
background = pygame.image.load('game/images/background-image.jpg')
full_background = pygame.transform.scale(background, (1000, 750))

# Creating the title
pygame.display.set_caption("Space Invaders")

# Creating the icon
icon = pygame.image.load('game/images/game-icon.png')
pygame.display.set_icon(icon)

running = True

while running:
    screen.blit(full_background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.display.update()
