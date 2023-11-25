import pygame
import sys
from button import Button

pygame.init()

#Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
FONT_SIZE = 36
PLAYER_RADIUS = 20

# Menu class
class Menu:
    def __init__(self, screen, buttons, font_size):
        self.screen = screen
        self.buttons = buttons
        self.selected_button = 0
        self.game_started = False

    def draw(self):
        for i, button in enumerate(self.buttons):
            button.draw(i == self.selected_button)

    def update(self):
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

    def select(self):
        # Handle the action for the currently selected button
        if self.selected_button == 0:
            print("Start Game")
            pygame.display.set_caption("GAME")
            self.game_started = True
        elif self.selected_button == 1:
            pygame.display.set_caption("INSTRUCTIONS")
            print("Instructions")
            # Add your "How to Play" logic here
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def navigate(self, direction):
        # Update the selected button based on the direction (1 for down, -1 for up)
        self.selected_button = (self.selected_button + direction) % len(self.buttons)