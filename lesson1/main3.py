import pygame


def draw(screen):
    color = pygame.Color(0, 204, 204)
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


if __name__ == "__main__":
    size = width, height = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.init()
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()
