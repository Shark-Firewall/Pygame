import pygame
import random

# ctrl+alt+l --- To Format the code

# Initilize the pygame
pygame.init()

# Creating the pygame window of size 500x500 --> width x Height
window = pygame.display.set_mode((500, 500));

# Overriding the default title of the window
pygame.display.set_caption("Space Invader")

# Overriding the logo of the window --------
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# ------------------------------- BACKGROUND IMAGE ----------------------------------

backgroundImg = pygame.image.load("space_invader_background.jpg")

# ------------------------------- PLAYER SECTION -------------------------------------
# Adding player on the screen
playerImg = pygame.image.load("player.png")

# Adding Player coordinate
playerX = 230
playerY = 400

playerX_changes = 0
playerY_changes = 0


# Adding image on others
def Player(x, y):
    window.blit(playerImg, (x, y))


# ------------------------------ ENEMY SECTION -------------------------------------------
# Adding player on the screen
enemyImg = pygame.image.load("alien.png")

# Adding Player coordinate
enemyX = random.randint(0, 436)
enemyY = random.randint(40, 436)

enemyX_changes = 0.3
enemyY_changes = 40


# Adding image on others
def Enemy(x, y):
    window.blit(enemyImg, (x, y))  # parameters --> ( image, ( X Starting Point, Y Starting Point))



# Making sure the window running for a time until we close the window
running = True;
while running:

    # Adding background color -- Here window mean which window or screen we are targeting
    window.fill((0, 0, 0))
    # Ading background Image
    window.blit(backgroundImg,(0,0));

# ------------------------------- EVENT HANDLING ------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add Horizontal Movement
        if event.type == pygame.KEYDOWN:
            # Key Setting for Horizontal Movement
            if event.key == pygame.K_LEFT:
                print("Right Key pressed")
                playerX_changes = -0.4
            if event.key == pygame.K_RIGHT:
                print("Left key pressed")
                playerX_changes = 0.4
            # Key Setting for vertical Movement
            if event.key == pygame.K_UP:
                print("Up Key Pressed")
                playerY_changes = -0.4
            if event.key == pygame.K_DOWN:
                print("Down Key Pressed")
                playerY_changes = 0.4
        if event.type == pygame.KEYUP:
            print("Keystroke up")
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_changes = 0

# -------------------------------------- PLAYER MOVEMENT -------------------------
    # Creating boundary condition for horizontal Movement
    if (playerX <= 0):
        playerX = 0
    elif (playerX >= 436):
        playerX = 436

    # Creating boundary condition for vertical Movement
    if (playerY <= 0):
        playerY = 0
    elif (playerY >= 436):
        playerY = 436

    playerX += playerX_changes
    playerY += playerY_changes

# ------------------------------------- ENEMY MOVEMENT --------------------------------
    # Enemy Movement
    if (enemyX <= 0):
        enemyX_changes = 0.3
        enemyY += enemyY_changes
    elif (enemyX >= 436 ):
        enemyX_changes = -0.3
        enemyY += enemyY_changes

    enemyX += enemyX_changes

    Player(playerX, playerY);
    Enemy(enemyX, enemyY)
    pygame.display.update()
