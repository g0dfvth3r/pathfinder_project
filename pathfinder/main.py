from grid.grid import Grid
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
    print(path)  # Print the path found by BFS

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_grid(screen)

        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()




 