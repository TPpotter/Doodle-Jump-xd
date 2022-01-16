import os
import random

import pygame
import sys

from platforms import all_sprites, create_level


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8 = '', '', '', '', '', '', '', ''
STOP, NEXT = False, True
BOI_LEFT = load_image('blue_doodle_left.png')
BOI_RIGHT = load_image('blue_doodle_right.png')
BOI_UP = load_image('blue_doodle_up.png')
END = False

class Doodle(pygame.sprite.Sprite):
    image = BOI_LEFT

    def __init__(self, *group):
        super().__init__(*group)

        self.image = Doodle.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 810
        # self.mask = pygame.mask.from_surface(self.image)

        self.velocity = 1
        self.distance = 100
        self.is_up = True

    def update(self, timedelta):
        change = timedelta * self.velocity

        if not self.is_up or not self.distance:
            self.rect = self.rect.move(0, change)

        if self.distance and self.distance - change > 0:
            self.rect = self.rect.move(0, -change)
            self.distance -= change

        elif self.distance and self.distance - change < 0:
            self.rect = self.rect.move(0, -self.distance)
            self.distance = 0
            self.is_up = False

        if self.rect.y >= 830:
            global END
            END = True

        if self.rect.y <= 0:
            global NEXT
            NEXT = True
            self.rect.y = 810

        for i in all_sprites:
            if self.rect.y + 50 == i.rect.y and \
                    (i.__class__.__name__ == 'Platform' or i.__class__.__name__ == 'MovingPlatform') \
                    and pygame.sprite.collide_mask(self, i):
                self.is_up = True
                self.distance = 175
                return


# size = width, height = 500, 900
# screen = pygame.display.set_mode(size)
# running = True
# pygame.display.set_caption('Doodle Test')
# clock = pygame.time.Clock()
#
# hero = Doodle()
# hero_sprite = pygame.sprite.Group()
# hero_sprite.add(hero)
#
# while running:
#     if NEXT:
#         for j in all_sprites:
#             j.kill()
#         create_level()
#         NEXT = False
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     if not STOP:
#         timedelta = clock.tick(60) / 15
#
#         for m in all_sprites:
#
#             m.update(timedelta)
#
#         hero.update(timedelta)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_a:
#                     hero.rect.x -= 20
#                     hero.image = BOI_LEFT
#
#                 if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                     hero.rect.x += 20
#                     hero.image = BOI_RIGHT
#
#         screen.fill((255, 255, 255))
#         all_sprites.draw(screen)
#         hero_sprite.draw(screen)
#         pygame.display.flip()
