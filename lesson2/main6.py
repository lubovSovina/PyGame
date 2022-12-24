import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Синий круг')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 204, 204), event.pos, 20)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
