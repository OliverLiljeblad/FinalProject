import pygame
import sys
from char import Char

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

# Button class
class Button:
    def __init__(self, screen, text, position, font_size):
        self.screen = screen
        self.text = text
        self.position = position
        self.font = pygame.font.Font(None, font_size)
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT

    def draw(self, selected):
        rect_color = WHITE if not selected else (200, 200, 200)
        pygame.draw.rect(self.screen, rect_color, (*self.position, self.width, self.height))
        text = self.font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=(self.position[0] + self.width // 2, self.position[1] + self.height // 2))
        self.screen.blit(text, text_rect)

# Menu class
class Menu:
    def __init__(self, screen, buttons, font_size):
        self.screen = screen
        self.buttons = buttons
        self.selected_button = 0

    def draw(self):
        for i, button in enumerate(self.buttons):
            button.draw(i == self.selected_button)

    def select(self):
        # Handle the action for the currently selected button
        if self.selected_button == 0:
            print("Start Game")
            # Add "Start Game" logic here
        elif self.selected_button == 1:
            print("How to Play")
            # Add "How to Play" logic here
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def navigate(self, direction):
        # Update the selected button based on the direction (1 for down, -1 for up)
        self.selected_button = (self.selected_button + direction) % len(self.buttons)

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
