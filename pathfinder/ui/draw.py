import pygame
import config
from grid.cell import CellState

def draw_grid(screen, grid):
    for row in grid.cells:
        for cell in row:
            color = (0, 0, 0)  # Default color for empty cells
            if cell.state == CellState.START:
                color = (0, 255, 0)  # Green for start cell
            elif cell.state == CellState.END:
                color = (255, 0, 0)  # Red for end cell
            elif cell.state == CellState.PATH:
                color = (0, 0, 255)  # Blue for path cells
            elif cell.state == CellState.WALL:
                color = (255, 255, 255)  # White for wall cells
            elif cell.state == CellState.VISITED:
                color = (255, 255, 0)  # Yellow for visited cells
            pygame.draw.rect(screen, color, (cell.col * config.CELL_SIZE, cell.row * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))

    for row in range(config.ROWS + 1):
        pygame.draw.line(screen, (200, 200, 200), (0, row * config.CELL_SIZE), (config.WIDTH, row * config.CELL_SIZE))
    for col in range(config.COLS + 1):
        pygame.draw.line(screen, (200, 200, 200), (col * config.CELL_SIZE, 0), (col * config.CELL_SIZE, config.HEIGHT))