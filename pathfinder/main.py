from grid.grid import Grid
from grid.cell import CellState
from ui.draw import draw_grid
from algorithms.bfs import bfs
from algorithms.path_utils import reconstruct_path
import pygame
import config

STEP_DELAY = 1000  # ms between BFS steps — tune to taste

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    grid = Grid(config.ROWS, config.COLS)
    running = True
    start = None
    end = None

    bfs_gen = None
    last_step_time = 0
    last_current = None  # tracks the most recent cell BFS visited

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
                    bfs_gen = bfs(grid, start, end)  # create generator, don't run it yet

        if bfs_gen is not None:
            now = pygame.time.get_ticks()
            if now - last_step_time >= STEP_DELAY:
                try:
                    current, visited, came_from = next(bfs_gen)
                    last_current = current
                    last_step_time = now

                    if current != start and current != end:
                        current.state = CellState.VISITED

                except StopIteration:
                    bfs_gen = None  # search is done, one way or another
                    if last_current == end:
                        path = reconstruct_path(came_from, start, end)
                        for c in path:
                            if c != start and c != end:
                                c.state = CellState.PATH
                    # else: queue exhausted, no path found — nothing to do, grid already shows VISITED cells

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()