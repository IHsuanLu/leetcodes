from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num, col_num = len(matrix), len(matrix[0])
        
        for row in range(row_num):
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                l, r = 0, col_num
                while l < r:
                    mid = (l + r) // 2
                    if matrix[row][mid] < target:
                        l = mid + 1
                    elif matrix[row][mid] > target:
                        r = mid 
                    else:
                        return True
        
        return False
        