import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600

# Display configuration
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption("Final Project")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill( (randint(0, 255),randint(0,255),randint(0,255)) )

# Draw the background on the screen before the loop to start with a fresh view
screen.blit(background, (0,0))

clock = pygame.time.Clock()
keepGoing = True

# The Game Loop
while keepGoing:
        
    # Set the timer to tick 30 times per second
    clock.tick(30)

    # The Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                keepGoing = False
            elif event.key == pygame.K_SPACE:
                background.fill( (randint(0, 255),randint(0,255),randint(0,255)) )  #### Replace with a random RGB color here 
                screen.blit(background, (0,0))


    pygame.display.flip()                 # Flip the screen to make the changes visible.
