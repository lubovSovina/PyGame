import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Green square')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    running = True
    image = pygame.Surface([100, 100])
    image.fill(pygame.Color('green'))
    screen.blit(image, (10, 10))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
