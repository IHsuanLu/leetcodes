from ast import List

# use the memo as a global variable to reduce time consumption

"""
Usually, in DFS or BFS, we can employ a set visited to prevent the cells from duplicate visits. 
We will introduce a better algorithm based on this in the next section.

Yet, note that we don't need a set in the question to prevent visiting traversed nodes because the path is increasing, and we will never visit a node with a smaller value.
"""

# Time complexity : O(mn)
# Space complexity : O(mn)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_num, col_num = len(matrix), len(matrix[0])
        memo = {}
        def dfs(row, col, pre_val):
            # out of bound
            if row < 0 or row >= row_num or col < 0 or col >= col_num:
                return 0
            
            if matrix[row][col] <= pre_val:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            curr = matrix[row][col]
            top_count = dfs(row - 1, col, curr)
            right_count = dfs(row, col + 1, curr)
            bottom_count = dfs(row + 1, col, curr)
            left_count = dfs(row, col - 1, curr)
            
            res = 1 + max(top_count, right_count, bottom_count, left_count)
            
            memo[(row, col)] = res
            return memo[(row, col)]
        
        max_val = float('-inf')
        for row in range(row_num):
            for col in range(col_num):
                res = dfs(row, col, -1)
                max_val = max(max_val, res)
                
        return max_val