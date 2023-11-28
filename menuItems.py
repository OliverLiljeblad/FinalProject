import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button:
    def __init__(self, text, x, y, width, height, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen, selected=False):
        color = WHITE if not selected else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Menu:
    def __init__(self, screen, buttons):
        self.screen = screen
        self.buttons = buttons
        self.selected_button = 0

    def draw(self):
        for i, button in enumerate(self.buttons):
            button.draw(self.screen, selected=i == self.selected_button)

    def select(self):
        self.buttons[self.selected_button].action()

    def navigate(self, direction):
        self.selected_button = (self.selected_button + direction) % len(self.buttons)