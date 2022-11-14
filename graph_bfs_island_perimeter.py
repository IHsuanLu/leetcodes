from ast import List
from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_num, col_num = len(grid), len(grid[0])
        queue = deque([])
        
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == 1:
                    queue.append((r, c))
    

        def get_neighbors(coord):
            r, c = coord
            res = []
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                new_row = r + delta_row[i]
                new_col = c + delta_col[i]
                res.append((new_row, new_col))
                
            return res
        
        
        perimeter = 0
        visited = set()
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                visited.add(nxt)
                neighbors = get_neighbors(nxt)
                for children in neighbors:
                    r, c = children
                    if r < 0 or c < 0 or r >= row_num or c >= col_num:
                        perimeter += 1
                    else:
                        if grid[r][c] == 0:
                            perimeter += 1
                        if grid[r][c] == 1:
                            queue.append(children)  


        return perimeter
