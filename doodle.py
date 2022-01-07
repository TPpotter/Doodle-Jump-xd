import os
import pygame
import sys

from platforms import Platform, all_sprites


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


BOI_LEFT = load_image('blue_doodle_left.png')
BOI_RIGHT = load_image('blue_doodle_right.png')
BOI_UP = load_image('blue_doodle_up.png')


class Doodle(pygame.sprite.Sprite):
    image = BOI_LEFT

    def __init__(self, *group):
        super().__init__(*group)

        self.image = Doodle.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 640
        # self.mask = pygame.mask.from_surface(self.image)

        self.velocity = 1
        self.distance = 50
        self.is_up = True

    def update(self, timedelta):
        change = round(timedelta * self.velocity)

        if not self.is_up:
            self.rect = self.rect.move(0, change)

        if self.distance and self.distance - change > 0:
            self.rect = self.rect.move(0, -change)
            self.distance -= change
            return

        if self.distance and self.distance - change < 0:
            self.rect = self.rect.move(0, -self.distance)
            self.distance = 0
            self.is_up = False
            return


size = width, height = 500, 900
screen = pygame.display.set_mode(size)
running = True
pygame.display.set_caption('Doodle Test')
clock = pygame.time.Clock()

hero = Doodle()
pl = Platform(10, 350)
hero_sprite = pygame.sprite.Group()
hero_sprite.add(hero)

while running:
    clock.tick(60)
    timedelta = 10
    hero.update(timedelta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                hero.rect.x -= 10
                hero.image = BOI_LEFT

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                hero.rect.x += 10
                hero.image = BOI_RIGHT

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    hero_sprite.draw(screen)
    pygame.display.flip()
