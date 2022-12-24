import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    x_pos = 0
    running = True
    v = 40
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos) % 800, 200), 20)
        x_pos += v * clock.tick() / 1000
        pygame.display.flip()
    pygame.quit()
