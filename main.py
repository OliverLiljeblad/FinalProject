import pygame
import sys
from button import Button
from game import SimpleGame
from menu import Menu

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Main function
def main():
    # Display configuration
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Button Menu")

    # Create buttons for the menu
    buttons = [
        Button(screen, "Start Game", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT-30), FONT_SIZE),
        Button(screen, "How to Play", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - 15), FONT_SIZE),
        Button(screen, "Quit", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + BUTTON_HEIGHT), FONT_SIZE),
    ]

    # Create a menu instance
    menu = Menu(screen, buttons, FONT_SIZE)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu.navigate(-1)
                elif event.key == pygame.K_DOWN:
                    menu.navigate(1)
                elif event.key == pygame.K_RETURN:
                    menu.select()

        screen.fill(BLACK)
        menu.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
