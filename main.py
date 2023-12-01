import pygame
import sys
from menuItems import Menu
from menuItems import Button
from enemy import Enemy
from player import Player

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 155, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
FONT_SIZE = 36
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
speed = 5
health = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MENU")

def start_game():
    print("Start Game")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    screen.fill(WHITE)

    player = Player()
    enemy = Enemy()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)
    
    clock = pygame.time.Clock()

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
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(enemy), False):
            print("Game Over!")
            running = False

        background.fill(WHITE)
        
        player.update()

        enemy.update(player)

        all_sprites.clear(screen, background)
        all_sprites.draw(screen)

        pygame.display.flip()

        clock.tick(30)

def how_to_play():
    print("How to play")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("How to play")

    clock = pygame.time.Clock()
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
        clock.tick(30)


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
    button_options = Button("How to play", 300, 260, 200, 50, how_to_play)
    button_exit = Button("Exit", 300, 320, 200, 50, exit_game)

    buttons = [button_start, button_options, button_exit]

    # Create a menu instance
    menu = Menu(screen, buttons)
    
    clock = pygame.time.Clock()
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

        pygame.display.set_caption("MENU")

        screen.fill(BLUE)
        menu.draw()
        pygame.display.flip()

    clock.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
