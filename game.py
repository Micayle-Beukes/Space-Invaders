import pygame
import random
import math


# Initializing pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((1000, 750))

# Creating a background image
background = pygame.image.load('images/background-image.jpg')
full_background = pygame.transform.scale(background, (1000, 750))

# Creating the title
pygame.display.set_caption("Space Invaders")

# Creating the icon
icon = pygame.image.load('images/game-icon.png')
pygame.display.set_icon(icon)

# Creating the Player
player_image = pygame.image.load('images/player.png')  
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
    enemy_image.append(pygame.image.load('images/enemy.png'))
    enemy_x.append(random.randint(0, 1000))  # random X co-ordinate
    enemy_y.append(random.randint(40, 200))  # random Y co-ordinate
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))
    
    
# Creating enemy bullet
bullet_image = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 640  # same position as the player
bullet_x_change = 0
bullet_y_change = 2
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))


# Collision detection    
def isCollison(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))  # calculates distance between 2 points
    if distance < 27:
        return True
    else:
        return False
    
    
# Displaying score on screen 
score_value = 0
font = pygame.font.Font('images/score-font.ttf', 40)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
    
# Displaying "GAME OVER" on the screen
game_over_font = pygame.font.Font('images/game-over-font.ttf', 120)

def game_over_text():
    game_over = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (160, 300))
    
    
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
                
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        
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
            game_over_text()
            break
            
        enemy_x[i] += enemy_x_change[i]
        
        # Adding the boundary of the enemy
        if enemy_x[i] < 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 936:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i] 
            
        # Collision     
        collision = isCollison(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 630
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 936) 
            enemy_y[i] = random.randint(40, 200)
        
        enemy(enemy_x[i], enemy_y[i], i)
        
        
    # Adding the bullet movement
    if bullet_y <= 0:
        bullet_y = 630
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y) 
        bullet_y -= bullet_y_change
            
    player()
    
    show_score(text_x, text_y)
    
    pygame.display.update()
