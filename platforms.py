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


class Platform(pygame.sprite.Sprite):  # Platform(x, y)
    image = load_image('platform.png')
    image = pygame.transform.scale(image, (102, 27))

    def __init__(self, x, y):
        super().__init__(all_sprites)

        self.image = Platform.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


class MovingPlatform(pygame.sprite.Sprite):
    image = load_image('blueplatform.png')

    def __init__(self, x, y, velocity):
        super().__init__(all_sprites)

        self.image = MovingPlatform.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

        self.velocity = velocity
        self.is_right = True

    def update(self, timedelta):
        change = timedelta * 0.15 * self.velocity

        if self.rect.x + change >= 500 - 102 and self.is_right:
            self.rect.x = 500 - 102
            self.is_right = False

            return

        if self.rect.x - change <= 0 and not self.is_right:
            self.rect.x = 0
            self.is_right = True

        self.rect.x = self.rect.x + change if self.is_right else self.rect.x - change

        for i in all_sprites:
            if i.__class__.__name__ == 'Platform' and pygame.sprite.collide_mask(self, i):
                self.is_right = not self.is_right

all_sprites = pygame.sprite.Group()