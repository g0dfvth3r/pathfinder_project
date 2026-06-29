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

    start = grid.cells[0][0]  # Starting cell
    end = grid.cells[19][19]  # Ending cell
    path = bfs(grid, start, end)  # Run BFS algorithm
    for cell in path:
        cell.state = CellState.PATH  # Mark the path cells

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)

        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()




 