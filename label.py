import pygame

FONT_COLOR = (0,0,255)

class Label(pygame.sprite.Sprite):
    # This class puts a message on the screen
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", size)
        self.text = " " 
        self.position = position
        
    def update(self, screen):
        self.image = self.font.render(self.text, 1, FONT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position