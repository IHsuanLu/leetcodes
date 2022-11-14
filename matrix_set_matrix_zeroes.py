# 1. O(m * n) space -> keep a copy of the matrix and mark zeroes while iterating
# 2. O(m + n) space -> keep two arrays indicating which rows, cols should be mark as zeroes at the very end
# 3. O(1) space -> use the fisrt row and col as the arrays mentioned in (2.). since we are iterating from top-left corner, it won't affect the result
from ast import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows, num_cols = len(matrix), len(matrix[0])
        row_zero = False # if the first row should be zero
        
        # determine which rows, cols should be zero
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True
        
        # note that we should start from the second row and col
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                
        
        if matrix[0][0] == 0:
            for row in range(num_rows):
                matrix[row][0] = 0
        
        if row_zero:
            for col in range(num_cols):
                matrix[0][col] = 0
                    