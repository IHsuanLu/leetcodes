from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = [0,0], [len(matrix) - 1, len(matrix[0]) - 1]
        
        mid_row = 0
        while left[0] <= right[0]:
            mid_row = (left[0] + right[0]) // 2
            if matrix[mid_row][0] == target:
                return True
            elif target > matrix[mid_row][0]:
                if target <= matrix[mid_row][len(matrix[0]) - 1]:
                    break
                left[0] = mid_row + 1
            elif target < matrix[mid_row][0]:
                right[0] = mid_row - 1
        
        col_left, col_right = 0, len(matrix[0]) - 1
        while col_left <= col_right:
            mid = (col_left + col_right) // 2
            if matrix[mid_row][mid] == target:
                return True
            if matrix[mid_row][mid] < target:
                col_left = mid + 1
            else:
                col_right = mid - 1
        
        return False
