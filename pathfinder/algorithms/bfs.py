from collections import deque

def bfs(grid, start, end):

    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == end:
            return True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            new_row = current.row + dr
            new_col = current.col + dc
            if 0 <= new_row < grid.rows and 0 <= new_col < grid.cols:
                neighbor = grid.cells[new_row][new_col]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    return False
    