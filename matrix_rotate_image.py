# set boundary pointers (top, right, bottom, left)
# rotate from outer to inner, one by one, starting from (0,0), (0,1) ...
#   (0,0) -> (0,2) -> (2,2) -> (2,0)
#   (0,1) -> (1,2) -> (2,1) -> (1,0)
# update boundary pointers for inner
# stop when the left and right boundary pointers intercepted
# use "i" correctly to move to the next round
from ast import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix[0]) - 1
        
        while left < right:
            # iterate through every element except for the last one
            for i in range(0, right - left):
                top, bottom = left, right # n*n
                
                # save top-left element
                top_left = matrix[top][left + i]
                
                # move bottom-left to top-left
                matrix[top][left + i] = matrix[bottom - i][left]
        
                # move bottom-right to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # move top-right to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # assign saved top-left to top-right
                matrix[top + i][right] = top_left
            
            left += 1
            right -= 1
                
                