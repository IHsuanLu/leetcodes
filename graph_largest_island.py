from ast import List
import collections


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row_nums, col_nums = len(grid), len(grid[0])
        nextColor = 2
        componentCounts = collections.defaultdict(int)
        
        def paint(row, col, color):
            if row < 0 or col < 0 or row >= row_nums or col >= col_nums:
                return
            if grid[row][col] != 1:
                return
            
            grid[row][col] = color
            componentCounts[color] += 1
            
            paint(row + 1, col, color)
            paint(row - 1, col, color)
            paint(row, col + 1, color)
            paint(row, col - 1, color)
        
        for r in range(row_nums):
            for c in range(col_nums):
                if grid[r][c] != 1:
                    continue
                paint(r, c, nextColor)
                nextColor += 1
        
        def get_neighbors(r, c):
            neighbors = []
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            for i in range(4):
                new_row = r + delta_rows[i]
                new_col = c + delta_cols[i]
                if new_row < 0 or new_row >= row_nums or new_col < 0 or new_col >= col_nums:
                    continue
                neighbors.append((new_row, new_col))
            return neighbors
        
        res = max(componentCounts.values() or [0])
        
        # iterate again thru the grid, try turning every "0" into "1"
        # and getting the maximum value
        for r in range(row_nums):
            for c in range(col_nums):
                if grid[r][c] == 0:
                    total = 1 # including grid[r][c] itself
                    neighborSet = set() # for not re-calculating the same-color neighbors
                    for nr, nc in get_neighbors(r, c):
                        n_color = grid[nr][nc]
                        if n_color not in neighborSet:
                            total += componentCounts[n_color]
                            neighborSet.add(n_color)
                            
                    res = max(res, total)

        return res