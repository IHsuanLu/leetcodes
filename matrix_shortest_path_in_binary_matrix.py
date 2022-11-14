from ast import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_num = col_num = len(grid)
        
        if grid[0][0] == 1:
            return -1

        # use bfs to calculate the shortest path 
        queue = deque([(0, 0)])
        count = 0
        visited = set()
        while len(queue) > 0:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) in visited: 
                    continue
                visited.add((r, c))

                if (r,c) == (row_num - 1, col_num - 1):
                    return count
                
                children = []
                if r + 1 < row_num and grid[r+1][c] == 0:
                    children.append((r+1, c))
                if c + 1 < col_num and grid[r][c+1] == 0:
                    children.append((r, c+1))
                if r + 1 < row_num and c + 1 < col_num and grid[r+1][c+1] == 0:
                    children.append((r+1, c+1))
                
                if r - 1 >= 0 and grid[r-1][c] == 0:
                    children.append((r-1, c))
                if c - 1 >= 0 and grid[r][c-1] == 0:
                    children.append((r, c-1))
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == 0:
                    children.append((r-1, c-1))
                
                
                if r - 1 >= 0 and c + 1 < col_num and grid[r-1][c+1] == 0:
                    children.append((r-1, c+1))
                if r + 1 < row_num and c - 1 >= 0 and grid[r+1][c-1] == 0:
                    children.append((r+1, c-1))
                
                for child in children:
                    queue.append(child)
                
        return -1