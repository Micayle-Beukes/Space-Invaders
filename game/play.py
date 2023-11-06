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
    
    
# Creating the Enemies
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 12

for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('game/images/enemy.png'))
    enemy_x.append(random.randint(0, 1000))  # random X co-ordinate
    enemy_y.append(random.randint(40, 200))  # random Y co-ordinate
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))
    
    
# Creating enemy bullet
bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 640  # same position as the player
bullet_x_change = 0
bullet_y_change = 2
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

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
        
    for i in range(num_of_enemies): 
        if enemy_y[i] > 600:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            break
            
        enemy_x[i] += enemy_x_change[i]
        
        # Adding the boundary of the enemy
        if enemy_x[i] < 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 936:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i] 
        
        enemy(enemy_x[i], enemy_y[i], i)
            
    player()
    
    pygame.display.update()
