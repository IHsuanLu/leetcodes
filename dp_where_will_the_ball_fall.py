# FAV
from ast import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        use dfs to simulate the ball drops
            -> for every element in the first row, we run a dfs to see if it reaches the end (last row)
                -> if we see the combination of `-1, 1`
                    -> return False directly
                -> if the ball reaches the last row
                    -> return True
        """
        row_num, col_num = len(grid), len(grid[0])
        res = [-1] * col_num

        def dfs(row, col):
            if col < 0 or col >= col_num:
                return -1
            if row >= row_num:
                return col

            if grid[row][col] == -1:
                if col == 0 or (col - 1 > 0 and grid[row][col - 1] == 1):
                    return -1
                return dfs(row + 1, col - 1)
            else:
                if col == col_num - 1 or (col + 1 > 0 and grid[row][col + 1] == -1):
                    return -1
                return dfs(row + 1, col + 1)

        for col in range(col_num):
            res[col] = dfs(0, col)
        
        return res



