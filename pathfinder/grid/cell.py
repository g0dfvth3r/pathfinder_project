for enum import Enum

class CellState(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3
    PATH = 4

class Cell:

    def __init__(self, row, col, state=CellState.EMPTY):
        self.position = (row, col)
        self.state = state
