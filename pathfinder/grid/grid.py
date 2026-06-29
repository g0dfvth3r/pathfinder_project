from grid.cell import Cell

class Grid:
    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]