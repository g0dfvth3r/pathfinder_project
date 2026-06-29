from grid.grid import Grid
from grid.cell import CellState
from ui.draw import draw_grid
import pygame
import config
from algorithms.bfs import bfs

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    grid = Grid(config.ROWS, config.COLS)
    running = True

    start = None
    end = None
    path = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // config.CELL_SIZE
                col = x // config.CELL_SIZE
                cell = grid.cells[row][col]

                if start is None:
                    start = cell
                    start.state = CellState.START
                elif end is None:
                    end = cell
                    end.state = CellState.END
                    path = bfs(grid, start, end)  # Call BFS to find the path
                    for c in path:
                        if c != start and c != end:
                            c.state = CellState.PATH  # Mark the path cells

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()




 