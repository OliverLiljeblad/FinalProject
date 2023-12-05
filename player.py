import pygame

width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pictures/frog-2644410_1280.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = 7

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
            if self.rect.right >= width:
                print("")

        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
        elif self.rect.top < 0:
            self.rect.top = 0

