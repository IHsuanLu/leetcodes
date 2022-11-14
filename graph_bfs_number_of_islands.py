from ast import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        def get_neighbors(coord):
            res = []
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    res.append((r, c))
            return res

        def bfs(idx):
            queue = deque([idx])
            r, c = idx
            grid[r][c] = '0'
            while len(queue) > 0:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in get_neighbors(node):
                        r, c = neighbor
                        if grid[r][c] == '0':
                            continue
                        queue.append(neighbor)
                        grid[r][c] = '0'

        count = 0
        # bfs starting from each unvisited land cell
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '0':
                    continue
                bfs((r, c))
                count += 1 # bfs would find 1 connected island, increment count

        return count