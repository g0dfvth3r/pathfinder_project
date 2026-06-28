import pygame
import config

def draw_grid(screen):
    for row in range(config.ROWS + 1):
        pygame.draw.line(screen, (200, 200, 200), (0, row * config.CELL_SIZE), (config.WIDTH, row * config.CELL_SIZE))
    for col in range(config.COLS + 1):
        pygame.draw.line(screen, (200, 200, 200), (col * config.CELL_SIZE, 0), (col * config.CELL_SIZE, config.HEIGHT))