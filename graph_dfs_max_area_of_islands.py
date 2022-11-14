from ast import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col):
            # out of bound
            if row < 0 or col < 0 or row >= num_row or col >= num_col:
                return 0
            
            # water
            if grid[row][col] == 0:
                return 0
            
            # visited
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            return (1 + dfs(row + 1, col)
                      + dfs(row - 1, col)
                      + dfs(row, col + 1)
                      + dfs(row, col - 1))
        
        max_area = 0
        for r in range(num_row):
            for c in range(num_col):
                max_area = max(max_area, dfs(r, c))
        
        return max_area
                