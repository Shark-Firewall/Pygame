import pygame

# Initilize the pygame
pygame.init()

# Creating the pygame window of size 500x500 --> width x Height
window = pygame.display.set_mode((500,500));

# Overriding the default title of the window
pygame.display.set_caption("Space Invader")

# Overriding the logo of the window --------
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Adding player on the screen
playerImg =  pygame.image.load("player.png")

# Adding Player coordinate
playerX = 230
playerY = 400

def Player():
    window.blit(playerImg, (playerX, playerY))



# Making sure the window running for a time until we close the window
running = True;
while running:

    # Adding background color -- Here windom mean which window or screen we are targeting
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Player();
    pygame.display.update()