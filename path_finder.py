import numpy as np
from collections import deque

class PathFinder3D:
    def __init__(self):
        self.directions = [
            (-1, 0, 0),  # move up
            (1, 0, 0),   # move down
            (0, -1, 0),  # move left
            (0, 1, 0),   # move right
            (0, 0, -1),  # move back
            (0, 0, 1),   # move forward
        ]
    def is_valid_cell(self, grid, pos, n, m, k):
        x, y, z = pos
        return 0 <= x < n and 0 <= y < m and 0 <= z < k and grid[x, y, z] == 0
    def find_path(self, grid, start, stop):
        # Dimensions of the grid
        n, m, k = grid.shape
        # start and stop positions validation
        if not self.is_valid_cell(grid, start, n, m, k) or not self.is_valid_cell(grid, stop, n, m, k):
            return []  # Invalid start or stop position
        # Queue for BFS, initialized with the start position and path
        queue = deque([(start, [start])])
        # Tracking visited cells
        visited = set([tuple(start)])

        while len(queue) != 0:
            current, path = queue.popleft()

            if tuple(current) == tuple(stop):
                return path
            # Do all the possible moves
            for dx, dy, dz in self.directions:
                x, y, z = current[0] + dx, current[1] + dy, current[2] + dz
                if self.is_valid_cell(grid,(x,y,z),n,m,k) and (x, y, z) not in visited:
                   visited.add((x, y, z))
                   queue.append(([x, y, z], path + [[x, y, z]]))
        return [] # No path found