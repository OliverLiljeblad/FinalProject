import pygame
import sys
from button import Button
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
speed = 5

class Char(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, speed):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


def menu_loop(menu):
    while not menu.game_started:
        menu.update()
        pygame.display.flip()


# Main function
def main():
    # Display configuration
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")

    buttons = [
        Button(screen, "Start Game", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT-30), FONT_SIZE),
        Button(screen, "Instructions", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - 15), FONT_SIZE),
        Button(screen, "Quit", (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + BUTTON_HEIGHT), FONT_SIZE),
    ]

    # Create a menu instance
    menu = Menu(screen, buttons, FONT_SIZE)

    char = Char(WIDTH//2, HEIGHT//2, 20, speed)

    all_sprites = pygame.sprite.Group(char)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    

        all_sprites.update()
        screen.fill(WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
