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

# Creating the Player
player_image = pygame.image.load('game/images/player.png')  
player_x = 450  # X co-ordinate
player_y = 640  # Y co-ordinate
player_x_change = 0  # new co-ordinate
player_y_change = 0  # new co-ordinate

def player():
    screen.blit(player_image, (player_x, player_y))

running = True

while running:
    screen.blit(full_background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:  # Checks if a keystroke is pressed
            if event.key == pygame.K_LEFT:  # Checks if the left keystroke is pressed
                player_x_change = -0.7
            if event.key == pygame.K_RIGHT:  # Checks if the left keystroke is pressed
                player_x_change = 0.7
        
        if event.type == pygame.KEYUP:  # Checks if the keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # Checks if the left or right keystroke was pressed
                player_x_change = 0  # The player will stop moving
                
    player_x += player_x_change
    
    # Adding the boundary of the player
    if player_x < 0:
        player_x = 0
    elif player_x >= 936:
        player_x = 936
            
    player()
    
    pygame.display.update()
