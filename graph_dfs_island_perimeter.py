from ast import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_num, col_num = len(grid), len(grid[0])
        
        def dfs(row, col, visited):
            if row < 0 or col < 0 or row >= row_num or col >= col_num:
                return 1
            
            if grid[row][col] == 0:
                return 1
            
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            perimeter = 0
            perimeter += dfs(row - 1, col, visited)
            perimeter += dfs(row, col + 1, visited)  
            perimeter += dfs(row + 1, col, visited)
            perimeter += dfs(row, col - 1, visited)
            
            return perimeter
        
        visited = set()
        res = 0
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c]:
                    res += dfs(r, c, visited)
                    
        return res
                    
