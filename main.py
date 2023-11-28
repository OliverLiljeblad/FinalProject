import pygame
import sys
from menuItems import Menu
from menuItems import Button

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 155, 0)
FONT_SIZE = 36
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
speed = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MENU")

class Char(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, speed):
        pygame.sprite.Sprite.__init__(self)
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

        if self.rect.left > screen.get_width():
            self.rect.right = 0 # ... wrap it back on the screen.
        elif self.rect.right < 0:
            self.rect.left = screen.get_width()
        elif self.rect.top > screen.get_height():
            self.rect.bottom = 0 # ... wrap it back on the screen.
        elif self.rect.bottom < 0:
            self.rect.top = screen.get_height()

def start_game():
    print("Start Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")
    screen.fill(WHITE)

    char = Char(WIDTH//2, HEIGHT//2, 20, 1)
    all_sprites = pygame.sprite.Group(char)

    clock = pygame.time.Clock()
    clock.tick(30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        all_sprites.update()
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

def show_options():
    print("Options")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(ORANGE)
        pygame.display.flip()


def exit_game():
    print("Exit")
    pygame.quit()
    sys.exit()

def saveScore():
    inFile = open("log.txt", "r")
    log = inFile.read()
    print(log)
    inFile.close()


# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MENU")

    button_start = Button("Start Game", 300, 200, 200, 50, start_game)
    button_options = Button("Options", 300, 260, 200, 50, show_options)
    button_exit = Button("Exit", 300, 320, 200, 50, exit_game)

    buttons = [button_start, button_options, button_exit]

    # Create a menu instance
    menu = Menu(screen, buttons)
    
    clock = pygame.time.Clock()
    clock.tick(30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu.navigate(-1)
                if event.key == pygame.K_DOWN:
                    menu.navigate(1)
                if event.key == pygame.K_RETURN:
                    menu.select()
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill(BLACK)
        menu.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
