import pygame

width, height = 800, 600

# Key class
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pictures/key-2674073_640.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)