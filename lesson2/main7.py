import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    running = True
    screen2 = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                screen2.blit(screen, (0, 0))
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            screen.fill(pygame.Color('black'))
            screen.blit(screen2, (0, 0))
            if drawing:
                if w > 0 and h > 0:
                    pygame.draw.rect(screen, (0, 204, 204), ((x1, y1), (w, h)), 5)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
