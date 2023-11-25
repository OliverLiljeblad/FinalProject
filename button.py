import pygame

pygame.init()

#Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

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