from enum import Enum

class CellState(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3
    PATH = 4
    VISITED = 5

class Cell:

    def __init__(self, row, col, state=CellState.EMPTY):
        self.row = row
        self.col = col
        self.state = state

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"
