import pygame
import random
from settings import *
from sprites import *

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound effects
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()  # handles the speed

# Game loop
running = True
while running:
    clock.tick(FPS)
    # Process input ( events )
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update

    # Draw / render
    screen.fill(BLACK)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
