import pygame
import sys
from menuItems import Menu
from menuItems import Button
from enemy import Enemy
from player import Player
from label import Label

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
countdown_time = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MENU")

background_image = pygame.image.load("house-2022147_1280.jpg")

#MOVE BG
def move_bg(screen, image):
    screen_size = screen.get_size()
    bg_size = image.get_size()
    bg_x = ((bg_size[0]-screen_size[0])) // 2
    bg_y = ((bg_size[1]-screen_size[1])) // 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bg_x -= 10
    if keys[pygame.K_RIGHT]:
        bg_x += 10
    if keys[pygame.K_UP]:
        bg_y -= 10
    if keys[pygame.K_DOWN]:
        bg_y += 10
    bg_x = max(0, min(bg_size[0]-screen_size[0], bg_x)) 
    bg_y = max(0, min(bg_size[1]-screen_size[1], bg_y))

    screen.blit(image, (-bg_x, -bg_y))

#LEVEL 1
def start_game():
    print("Start Game")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 1")

    background = pygame.image.load("house-2022147_1280.jpg")
    background.convert()
    screen.blit(background, (0, 0))

    
    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()
    enemy = Enemy()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)
    otherSprites = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(enemy), False):
            print("Game Over!")
            running = False
            lose()

        if player.rect.top == 0:
           level2()
           running = False

        scoreboard.text = f"Remaining Time: "

        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        otherSprites.update(screen)
        player.update()
        enemy.update(player)

        otherSprites.draw(screen)
        all_sprites.draw(screen)
        
        pygame.display.flip()

        clock.tick(30)

#LEVEL 2
def level2():
    print()
    print("Level 2")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 2")

    background = pygame.image.load("bridge-2023956_1280.png")
    background.convert()
    screen.blit(background, (0, 0))

    
    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()
    enemy = Enemy()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)
    otherSprites = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(enemy), False):
            print("Game Over!")
            running = False
            lose()

        if player.rect.right == WIDTH:
           level3()
           running = False

        scoreboard.text = f"Remaining Time: "

        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        otherSprites.update(screen)
        player.update()
        enemy.update(player)

        otherSprites.draw(screen)
        all_sprites.draw(screen)
        
        pygame.display.flip()

        clock.tick(30)


#LEVEL 3
def level3():
    print()
    print("Level 3")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 3")

    background = pygame.image.load("moon-7264703_1280.jpg")
    background.convert()
    screen.blit(background, (0, 0))

    
    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()
    enemy = Enemy()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)
    otherSprites = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(enemy), False):
            print("Game Over!")
            running = False
            lose()

        if player.rect.bottom == HEIGHT:
            running = False
            win()

        scoreboard.text = f"Remaining Time: "

        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        otherSprites.update(screen)
        player.update()
        enemy.update(player)

        otherSprites.draw(screen)
        all_sprites.draw(screen)
        
        pygame.display.flip()

        clock.tick(30)

def win():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("You WIN!")

    background = pygame.image.load("")
    background.convert()
    screen.blit(background, (0, 0))

    playAgainLabel = Label( (WIDTH//2, 100), 50 )

    running = True
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        otherSprites.clear(screen, background)
        otherSprites.update(screen)
        otherSprites.draw(screen)

        pygame.display.flip()


def lose():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("You LOST!")

    background = pygame.image.load("Game-Over-Graphics-30114494-1-580x386.jpg")
    background.convert()
    screen.blit(background, (100, 100))

    playAgainLabel = Label( (WIDTH//2, 100), 50 )
    
    otherSprites = pygame.sprite.Group(playAgainLabel)

    running = True
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        playAgainLabel.text = f"Do you want to play again? Y/N "

        screen.blit(background, (100, 100))
        otherSprites.update(screen)
        otherSprites.draw(screen)

        pygame.display.flip()

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
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(background_image, (0, 0))
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

        screen.blit(background_image, (0, 0))
        menu.draw()
        pygame.display.flip()

    clock.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
