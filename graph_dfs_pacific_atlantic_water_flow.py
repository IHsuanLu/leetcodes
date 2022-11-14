from ast import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row, num_col = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(row, col, visited, prev_height):
            if row < 0 or col < 0 or row >= num_row or col >= num_col:
                return
            if ((row, col) in visited):
                return 
            if heights[row][col] < prev_height:
                return 
            
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            
        
        # run dfs on the cells in the first and last rows
        for c in range(num_col):
            dfs(0, c, pac, heights[0][c]) #row, col, visited, prev_height
            dfs(num_row - 1, c, atl, heights[num_row - 1][c])
            
        # run dfs on the cells in the first and last cols
        for r in range(num_row):
            dfs(r, 0, pac, heights[r][0]) #row, col, visited, prev_height
            dfs(r, num_col - 1, atl, heights[r][num_col - 1])
    
        res = []
        for r in range(num_row):
            for c in range(num_col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        
        return res