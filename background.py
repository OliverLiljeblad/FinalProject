import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Background(pygame.sprite.Sprite):
    def __init__(self, picture):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.image.convert()
        self.rect = self.image.get_rect()

    def moveLeft(self):
        self.rect.centerx -= 5
        
    def update(self, x, y):
        screen.blit(self.image, (x, y))