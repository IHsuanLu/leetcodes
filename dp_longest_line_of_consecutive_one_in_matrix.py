from ast import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        row_num, col_num = len(mat), len(mat[0])

        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row < 0 or col < 0 or row >= row_num or col >= col_num:
                return (0,0,0,0)
            if mat[row][col] == 0:
                return (0,0,0,0)

            (horizontal_count, _, _, _) = dfs(row, col + 1)
            (_, vertical_count, _, _) =  dfs(row + 1, col)
            (_, _, diagonal_count, _) = dfs(row + 1, col + 1)
            (_, _, _, a_diagonal_count) = dfs(row + 1, col - 1)
    
            memo[(row, col)] = (horizontal_count + 1, vertical_count + 1, diagonal_count + 1, a_diagonal_count + 1)
            return memo[(row, col)]
    
        max_val = 0
        for r in range(row_num):
            for c in range(col_num):
                if mat[r][c] == 1:
                    max_val = max(max_val, max(dfs(r, c)))
        
        return max_val