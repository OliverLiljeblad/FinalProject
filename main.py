import pygame
import sys
from random import randint
from menuItems import Menu
from menuItems import Button
from enemy import Enemy
from player import Player
from label import Label
from key import Key
from background import Background

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

background_image = pygame.image.load("pictures/house-2022147_1280.jpg")
collision_sound = pygame.mixer.Sound("584207__soundsnapfx__impact-short-ring-out.wav")

#LEVEL 1
def start_game():
    print("Level 1")

    remainingKeys = 1

    hasKey = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 1")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
 
    backgroundPicture = Background("pictures/house-2022147_1280.jpg")

    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()

    enemy = Enemy()

    key = Key(randint(30, 100), randint(50, 100))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(backgroundPicture, player, enemy, key)
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
            collision_sound.play()
            running = False
            lose()

        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key), False):
            print()
            print("KEY")
            all_sprites.remove(key)
            hasKey = True

        if hasKey == True:
            if player.rect.top == 0:
                level2()
                running = False
        
        if hasKey == False:
            scoreboard.text = f"Remaining Keys: 1"
        else:
            scoreboard.text = f"Remaining Keys: 0"
        
        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        player.update()
        enemy.update(player)
        otherSprites.update(screen)

        all_sprites.draw(screen)
        otherSprites.draw(screen)
        
        pygame.display.flip()

        clock.tick(30)

#LEVEL 2
def level2():
    print()
    print("Level 2")

    hasKey = False
    hasKey1 = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 2")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
 
    backgroundPicture = Background("pictures/bridge-2023956_1280.png")

    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()
    enemy = Enemy()
    enemy1 = Enemy()
    key = Key(randint(600,750), randint(50, 150))
    key1 = Key(randint(50, 150), randint(400, 550))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(backgroundPicture, key, key1, player, enemy, enemy1)
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
            collision_sound.play()
            running = False
            lose()
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key), False):
            print()
            print("KEY")
            all_sprites.remove(key)
            hasKey = True
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key1), False):
            print()
            print("KEY")
            all_sprites.remove(key1)
            hasKey1 = True

        if hasKey and hasKey1 == True:
            scoreboard.text = f"Remaining Keys: 0"
            if player.rect.right == WIDTH:
                level3()
                running = False
        elif hasKey == False and hasKey1 == False:
            scoreboard.text = f"Remaining Keys: 2"
        elif hasKey == True and hasKey1 == False:
            scoreboard.text = f"Remaining Keys: 1"
        elif hasKey == False and hasKey1 == True:
            scoreboard.text = f"Remaining Keys: 1"
            

        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        
        player.update()
        enemy.update(player)
        enemy1.update(player)
        otherSprites.update(screen)
        
        all_sprites.draw(screen)
        otherSprites.draw(screen)

        pygame.display.flip()

        clock.tick(30)


#LEVEL 3
def level3():
    print()
    print("Level 3")

    hasKey = False
    hasKey1 = False
    hasKey2 = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 3")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
 
    backgroundPicture = Background("pictures/moon-7264703_1280.jpg")
    
    scoreboard = Label( (WIDTH//2, 20), 30 )

    player = Player()

    key = Key(randint(600,750), randint(0, 150))
    key1 = Key(randint(0, 150), randint(400, 550))
    key2 = Key(850, randint(50,750))
    enemy = Enemy()
    enemy1 = Enemy()
    enemy2 = Enemy()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(backgroundPicture, key, key1, key2, player, enemy, enemy1, enemy2)
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
            collision_sound.play()
            running = False
            lose()

        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key), False):
            print()
            print("KEY")
            all_sprites.remove(key)
            hasKey = True
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key1), False):
            print()
            print("KEY")
            all_sprites.remove(key1)
            hasKey1 = True
        
        if pygame.sprite.spritecollide(player, pygame.sprite.Group(key2), False):
            print()
            print("KEY")
            all_sprites.remove(key2)
            hasKey2 = True

        if hasKey and hasKey1 and hasKey2 == True:
            scoreboard.text = f"Remaining Keys: 0"
            if player.rect.top == 0:
                running = False
                win()
        elif hasKey == False and hasKey1 == False and hasKey2 == False:
            scoreboard.text = f"Remaining Keys: 3"
        elif hasKey == True and hasKey1 == False and hasKey2 == False:
            scoreboard.text = f"Remaining Keys: 2"
        elif hasKey == False and hasKey1 == True and hasKey2 == False:
            scoreboard.text = f"Remaining Keys: 2"
        elif hasKey == False and hasKey1 == False and hasKey2 == True:
            scoreboard.text = f"Remaining Keys: 2"
        elif hasKey == True and hasKey1 == True and hasKey2 == False:
            scoreboard.text = f"Remaining Keys: 1"
        elif hasKey == True and hasKey1 == False and hasKey2 == True:
            scoreboard.text = f"Remaining Keys: 1"
        elif hasKey == False and hasKey1 == True and hasKey2 == True:
            scoreboard.text = f"Remaining Keys: 1"

        if player.rect.right == WIDTH:
            backgroundPicture.moveLeft()
            key.moveLeft()
            key1.moveLeft()
            key2.moveLeft()

        otherSprites.clear(screen, background)
        all_sprites.clear(screen, background)
        
        player.update()
        enemy.update(player)
        enemy1.update(player)
        enemy2.update(player)
        otherSprites.update(screen)
        
        all_sprites.draw(screen)
        otherSprites.draw(screen)

        pygame.display.flip()

        clock.tick(30)

def win():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("You WIN!")

    background = pygame.image.load("pictures/business-5459692_1280.png")
    background.convert()
    
    resized_image = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(resized_image, (0, 0))

    playAgainLabel = Label( (WIDTH//2, 100), 50 )
    otherSprites = pygame.sprite.Group(playAgainLabel)

    running = True
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    running = False
                if event.key == pygame.K_n:
                    thanksForPlaying()

        playAgainLabel.text = f"Do you want to play again? Y/N "

        otherSprites.clear(screen, background)
        otherSprites.update(screen)
        otherSprites.draw(screen)

        pygame.display.flip()


def lose():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("You LOST!")

    background = pygame.image.load("pictures/Game-Over-Graphics-30114494-1-580x386.jpg")
    background.convert()
    background.set_colorkey(background.get_at((1,1)))
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
                if event.key == pygame.K_y:
                    running = False
                if event.key == pygame.K_n:
                    thanksForPlaying()

        playAgainLabel.text = f"Do you want to play again? Y/N "

        screen.blit(background, (100, 100))
        otherSprites.update(screen)
        otherSprites.draw(screen)

        pygame.display.flip()

def thanksForPlaying():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Thanks for playing!")

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    screen.fill((125, 125, 125))

    print()
    print("Thanks For Playing")

    thanks = Label( (WIDTH//2, 100), 50 )
    name = Label( (WIDTH//2, 160), 50 )
    year = Label( (WIDTH//2, 220), 50 )
    key = Label( (WIDTH//2, 300), 50 )

    otherSprites = pygame.sprite.Group(thanks, name, year, key)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                running = False
                exit_game()
        
        thanks.text = f"Thanks for playing!"
        name.text = f"Created By: Oliver Liljeblad"
        year.text = f"2023"
        key.text = f"Press any key to exit"
        
        screen.blit(background, (WIDTH, HEIGHT))
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
    print()
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

    button_start = Button("Start Game", 300, 200, 200, 50, level3)
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
