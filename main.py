import pygame

# Initilize the pygame
pygame.init()

# Creating the pygame window of size 500x500 --> width x Height
window = pygame.display.set_mode((500, 500));

# Overriding the default title of the window
pygame.display.set_caption("Space Invader")

# Overriding the logo of the window --------
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Adding player on the screen
playerImg = pygame.image.load("player.png")

# Adding Player coordinate
playerX = 230
playerY = 400

playerX_changes = 0
playerY_changes = -1


def Player(x, y):
    window.blit(playerImg, (x, y))


# Making sure the window running for a time until we close the window
running = True;
while running:

    # Adding background color -- Here windom mean which window or screen we are targeting
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add Horizontal Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Right Key pressed")
                playerX_changes = -0.1
            if event.key == pygame.K_RIGHT:
                print("Left key pressed")
                playerX_changes = 0.1
        if event.type == pygame.KEYUP:
            print("Keystroke up")
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_changes = 0

    # Creating boundary condition
    if (playerX <= 0):
        playerX = 0
    elif (playerX >= 436):
        playerX = 436

    playerX += playerX_changes
    Player(playerX, playerY);
    pygame.display.update()
