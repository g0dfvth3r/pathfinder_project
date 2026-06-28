from grid.grid import Grid
from ui.draw import draw_grid
import pygame
import config

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    grid = Grid(config.ROWS, config.COLS)
    running = True

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



 