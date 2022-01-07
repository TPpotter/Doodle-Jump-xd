import os

import pygame
import sys


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


FPS = 50


class StartingScreen(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = load_image('Default.png')
        self.rect = self.image.get_rect()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    start = StartingScreen(start_sprite)
    start_sprite.draw(screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


size = width, height = 320, 480
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

running = True
pygame.display.set_caption('Doodle Test')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
start_sprite = pygame.sprite.Group()
start_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
