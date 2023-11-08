import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:
    def __init__(self, screen, items, font, font_size, item_spacing=50):
        self.screen = screen
        self.items = items
        self.font = pygame.font.Font(None, font_size)
        self.selected_item = 0
        self.item_spacing = item_spacing

    def draw(self):
        for i, item in enumerate(self.items):
            text = self.font.render(item, True, WHITE if i == self.selected_item else BLACK)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + i * self.item_spacing))
            self.screen.blit(text, text_rect)

    def select(self):
        # Handle the action for the currently selected menu item
        if self.selected_item == 0:
            print("Start Game")
        elif self.selected_item == 1:
            print("Options")
        elif self.selected_item == 2:
            pygame.quit()
            sys.exit()

    def navigate(self, direction):
        # Update the selected menu item based on the direction (1 for down, -1 for up)
        self.selected_item = (self.selected_item + direction) % len(self.items)


def main():
    pygame.init()
    # Display configuration
    screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
    
    pygame.display.set_caption("Final Project")
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # Draw the background on the screen before the loop to start with a fresh view
    screen.blit(background, (0,0))

    items = ["Start Game", "Options", "Exit"]
    font_size = 36
    menu = Menu(screen, items, None, font_size)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_UP:
                    menu.navigate(-1)
                if event.key == pygame.K_DOWN:
                    menu.navigate(1)
                if event.key == pygame.K_RETURN:
                    menu.select()

        screen.fill(BLACK)
        menu.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()