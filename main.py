import pygame

# Initilize the pygame
pygame.init()

# Creating the pygame window of size 500x500
window = pygame.display.set_mode((500,500));

# Overriding the default title of the window
pygame.display.set_caption("First Pygame")

# Overriding the logo of the window --------
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Making sure the window running for a time until we close the window
running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Adding background color -- Here windom mean which window or screen we are targeting
    window.fill((255,0,0))
    pygame.display.update()