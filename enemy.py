import pygame
import sys


white = (255, 255, 255)
black = (0, 0, 0)
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Enemy:
    def __init__(self, x, y, width, height, speedX, speedY):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.speedX = speedX
        self.speedY = speedY

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)
    
    def update(self):
        self.rect.y -= self.speedY
        self.rect.x += self.speedX

        if self.rect.right > screen.get_width() or self.rect.left <= 0:
            self.speedX = -self.speedX

        if self.rect.bottom > screen.get_height() or self.rect.top <= 0:
            self.speedY = -self.speedY
