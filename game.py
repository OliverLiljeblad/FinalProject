import pygame

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

class SimpleGame:
    def __init__(self, screen):
        self.screen = screen
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= 5
        if keys[pygame.K_RIGHT]:
            self.player_x += 5
        if keys[pygame.K_UP]:
            self.player_y -= 5
        if keys[pygame.K_DOWN]:
            self.player_y += 5

    def update(self):
        # Additional game logic can be added here
        pass

    def draw(self):
        pygame.draw.circle(self.screen, WHITE, (self.player_x, self.player_y), PLAYER_RADIUS)
