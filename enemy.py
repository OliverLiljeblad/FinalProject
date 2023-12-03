import pygame
import random

width, height = 800, 600
red = (255, 0, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, width), 0)
        self.speed = 3

    def update(self, target):
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y
        dist = pygame.math.Vector2(dx, dy)
        dist.normalize_ip()
        self.rect.x += dist.x * self.speed
        self.rect.y += dist.y * self.speed