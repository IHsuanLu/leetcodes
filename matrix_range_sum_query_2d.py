"""
# given_mat
3, 0, 1
5, 6, 3

# prefix_mat
3,  3,  4
8, 14, 18

# intuition
18 - (14 + 4 - 3) = 3
18 - (8 + 4 - 3) = 9    
"""
from ast import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_mat = matrix
        
        row_num, col_num = len(self.prefix_mat), len(self.prefix_mat[0])
        for row in range(1, row_num):
            self.prefix_mat[row][0] += self.prefix_mat[row - 1][0]
        
        for col in range(1, col_num):
            self.prefix_mat[0][col] += self.prefix_mat[0][col - 1]
        
        for r in range(1, row_num):
            for c in range(1, col_num):
                prev_col_val = self.prefix_mat[r][c - 1] if c - 1 >= 0 else 0
                prev_row_val = self.prefix_mat[r - 1][c] if r - 1 >= 0 else 0
                self.prefix_mat[r][c] += prev_col_val + prev_row_val - self.prefix_mat[r - 1][c - 1]
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix_sum = self.prefix_mat[row2][col2]
        
        prev_col_val = self.prefix_mat[row2][col1 - 1] if col1 - 1 >= 0 else 0
        prev_row_val = self.prefix_mat[row1 - 1][col2] if row1 - 1 >= 0 else 0
        dup = self.prefix_mat[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        
        return prefix_sum - prev_col_val - prev_row_val + dup
