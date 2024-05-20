import pygame
import time

WIDTH = 700
HEIGHT = 500
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PhilOng")
clock = pygame.time.Clock()
f1 = pygame.font.SysFont('inkfree', 45)
s1x = 0
s1y = 100
s2x = 600
s2y = 0
s1 = 0
s2 = 0
x = 150
y = 150
val_x = 5
val_y = 5
deg = 90
flag_y = 1
flag_x = 1
bounce = 0
fail = 0
time_past = 0
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing screen
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    
    # Рендеринг
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        s2y -= 10
    if keys[pygame.K_DOWN]:
        s2y += 10
    if keys[pygame.K_w]:
        s1y -= 10
    if keys[pygame.K_s]:
        s1y += 10
    background = pygame.transform.scale(pygame.image.load("background.jpg"), (700, 500))
    screen.blit(background, (0, 0))
    sprite1 = pygame.transform.scale(pygame.image.load("sprite1.png"), (100, 100))
    sprite1.set_colorkey(WHITE)
    screen.blit(sprite1, (s1x, s1y))
    sprite2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (100, 100))
    sprite2.set_colorkey(WHITE)
    screen.blit(sprite2, (s2x, s2y))
    x += val_x
    y += val_y
    pygame.draw.circle(screen, WHITE, (x, y), 10)
    surf = pygame.Surface((20, 20))
    crect = surf.get_rect(topleft=(x - 10, y - 10))
    if (y <= 10 or y >= 480 or bounce == 1) and flag_y == 1:
        val_y = 0 - val_y
        flag_y = 0
        time_past = pygame.time.get_ticks()
    if (crect.colliderect(sprite1.get_rect(topleft=(s1x, s1y))) or crect.colliderect(sprite2.get_rect(topleft=(s2x, s2y)))) and flag_x == 1:
        val_x = 0 - val_x
        flag_x = 0
        time_past = pygame.time.get_ticks()
    if (pygame.time.get_ticks() - time_past >= 100):
        flag_x = 1
        flag_y = 1
    if (x >= 680) and flag_x == 1:
        s1 += 1
        x = 150
        y = 150
    if (x <= 0) and flag_x == 1:
        s2 += 1
        x = 150
        y = 150
    if (s1 > 9):
        text1 = f1.render('Кот победил!', True, WHITE)
        screen.blit(text1, (230, 10))
        pygame.display.flip()
        time.sleep(3)
        break
    if (True):
        text1 = f1.render('Свинья победила!', True, WHITE)
        screen.blit(text1, (200, 10))
        pygame.display.flip()
        time.sleep(3)
        break
    text1 = f1.render(str(s1) + ' : ' + str(s2), True, WHITE)
    screen.blit(text1, (300, 10))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
