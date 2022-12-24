import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[False] * height for _ in range(width)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        left = self.left
        top = self.top
        for i in range(self.height):
            for j in range(self.width):
                if not self.board[j][i]:
                    pygame.draw.rect(screen, (255, 255, 255), ((left, top), (self.cell_size, self.cell_size)), 1)
                elif self.board[j][i]:
                    pygame.draw.rect(screen, (255, 255, 255), ((left, top), (self.cell_size, self.cell_size)), 0)
                left += self.cell_size
            top += self.cell_size
            left = self.left

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def on_click(self, cell_coords):
        if cell_coords is not None:
            for i in range(self.height):
                self.board[cell_coords[0]][i] = not self.board[cell_coords[0]][i]
            for i in range(self.width):
                self.board[i][cell_coords[1]] = not self.board[i][cell_coords[1]]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Клетчатое поле')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    fps = 50
    clock = pygame.time.Clock()
    board = Board(15, 15)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
