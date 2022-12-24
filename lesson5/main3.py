import random

import os
import sys

import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('..\data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()

bi = load_image('bomb.png')
for i in range(50):
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = bi
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = random.randrange(width)
    sprite.rect.y = random.randrange(height)

if __name__ == '__main__':
    pygame.display.set_caption('Бомбы не шевелятся')
    fps = 50
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()