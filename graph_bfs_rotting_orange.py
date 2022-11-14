# Note that DFS in this case is not gonna work cause the rotten oranges are infecting adjacent simultaneously
# to simulate the simultaneous rotting, we should run BFS simutaneously on multiple sources
# by putting sources in the queue at the very begining
from ast import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
            
        def get_neighbors(r, c):
            res = []
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            
            for i in range(len(delta_row)):
                next_r = r + delta_row[i]
                next_c = c + delta_col[i]
                if next_r >= 0 and next_r < num_row and next_c >= 0 and next_c < num_col:
                    res.append((next_r, next_c))
            
            return res
        
        rotten_spots = []
        fresh_count = 0
        for r in range(num_row):
            for c in range(num_col):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    rotten_spots.append((r,c))
                    
        visited = set()
        queue = deque(rotten_spots)
        res = 0
        
        while len(queue) > 0 and fresh_count > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                r, c = nxt
                visited.add((r, c))
                for neighbor in get_neighbors(r, c):
                    r, c = neighbor
                    if grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh_count -= 1
            res += 1
        
        return res if fresh_count == 0 else -1