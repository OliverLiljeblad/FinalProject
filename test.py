import pygame

FPS = 60
screen = pygame.display.set_mode((1000, 1000))
bg = pygame.image.load('bridge-2023956_1280.png')

screen_size = screen.get_size()
bg_size = bg.get_size()
bg_x = (bg_size[0]-screen_size[0]) // 2
bg_y = (bg_size[1]-screen_size[1]) // 2

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

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

    screen.blit(bg, (-bg_x, -bg_y))
    pygame.display.flip()