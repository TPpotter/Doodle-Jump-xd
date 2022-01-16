import os
import sys

import pygame

import doodle
from platforms import COLOUR


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


FPS = 50
start_sprite = pygame.sprite.Group()
pause_sprite = pygame.sprite.Group()


class StartingScreen(pygame.sprite.Sprite):
    image = load_image('Default.png')
    image = pygame.transform.scale(image, (500, 900))

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = StartingScreen.image
        self.rect = self.image.get_rect()


class Pause(pygame.sprite.Sprite):
    image = load_image('pause.png')
    image = pygame.transform.scale(image, (200, 200))

    def __init__(self):
        super().__init__(pause_sprite)

        self.image = Pause.image
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 350


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    start = StartingScreen(start_sprite)
    start_sprite.draw(screen)
    pygame.display.flip()

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT or (ev.type == pygame.KEYDOWN and ev.key == pygame.K_f):
                terminate()
            elif ev.type == pygame.KEYDOWN or \
                    ev.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


size = width, height = 500, 900
screen = pygame.display.set_mode(size)
screen.fill((COLOUR, COLOUR, COLOUR))

running = True
pygame.display.set_caption('Doodle Test')
clock = pygame.time.Clock()

pause = Pause()
pause_sprite.add(pause)

start_screen()

hero = doodle.Doodle()
hero_sprite = pygame.sprite.Group()
hero_sprite.add(hero)

while running:
    if doodle.NEXT:
        for j in doodle.all_sprites:
            j.kill()
        doodle.create_level()
        doodle.NEXT = False

    if doodle.STOP:
        pause_sprite.draw(screen)
        pygame.display.update()
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_f):
            running = False
            exit()

        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE):
            doodle.STOP = False

    if not doodle.STOP and not doodle.END:
        timedelta = clock.tick(60) / 15

        for m in doodle.all_sprites:
            m.update(timedelta)

        hero.update(timedelta)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_f):
                running = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE):
                doodle.STOP = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    hero.rect.x -= 20
                    hero.image = doodle.BOI_LEFT

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    hero.rect.x += 20
                    hero.image = doodle.BOI_RIGHT

        screen.fill((255, 255, 255))
        doodle.all_sprites.draw(screen)
        hero_sprite.draw(screen)
        pygame.display.flip()
