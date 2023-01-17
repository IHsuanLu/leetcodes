# FAV, sometimes we don't want naively put everything into queue

from ast import List
from collections import deque

# BFS (enhanced)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        use bfs to traverse the grid, storing (r, c, remaining_k, steps)
        """
        row_num, col_num = len(grid), len(grid[0])

        # (ENHANCEMENT) directly return if k is enough to remove evey obstacle
        if k > (row_num - 1) + (col_num - 1):
            return (row_num - 1) + (col_num - 1)

        def get_neighbors(row, col):
            neighbors = []
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            for i in range(4):
                n_row = row + delta_rows[i]
                n_col = col + delta_cols[i]
                if n_row < 0 or n_row >= row_num or n_col < 0 or n_col >= col_num:
                    continue
                neighbors.append((n_row, n_col))
            return neighbors

        visited = set()
        queue = deque([(0, 0, k, 0)])
        while queue:
            for _ in range(len(queue)):
                n_row, n_col, remaining_k, steps = queue.popleft()

                if (n_row, n_col) == (row_num - 1, col_num - 1):
                    return steps
                
                for neighbor in get_neighbors(n_row, n_col):
                    r, c = neighbor
                    # (ENHANCEMENT) instead of naively put (r, c) into queue, we should only add if (r, c, remaining_k - 1) has not occured before
                    if grid[r][c] == 1 and remaining_k > 0 and (r, c, remaining_k - 1) not in visited: 
                        queue.append((r, c, remaining_k - 1, steps + 1))
                        visited.add((r, c, remaining_k - 1))
                    
                    # (ENHANCEMENT) the above logic applies as well
                    if grid[r][c] == 0 and (r, c, remaining_k) not in visited:
                        queue.append((r, c, remaining_k, steps + 1))
                        visited.add((r, c, remaining_k))

        return -1


# BFS -> TLE pass 22 / 43
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        use bfs to traverse the grid, storing (r, c, remaining_k, steps)
        """
        row_num, col_num = len(grid), len(grid[0])

        def get_neighbors(row, col):
            neighbors = []
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            for i in range(4):
                n_row = row + delta_rows[i]
                n_col = col + delta_cols[i]
                if n_row < 0 or n_row >= row_num or n_col < 0 or n_col >= col_num:
                    continue
                neighbors.append((n_row, n_col))
            return neighbors

        visited = set()
        queue = deque([(0, 0, k, 0)])

        while queue:
            for _ in range(len(queue)):
                n_row, n_col, remaining_k, steps = queue.popleft()
                if (n_row, n_col) in visited:
                    continue

                if (n_row, n_col) == (row_num - 1, col_num - 1):
                    return steps

                if grid[n_row][n_col] == 1:
                    remaining_k -= 1
                if remaining_k < 0:
                    continue
                
                for neighbor in get_neighbors(n_row, n_col):
                    r, c = neighbor
                    queue.append((r, c, remaining_k, steps + 1))

        return -1
                


