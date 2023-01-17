from ast import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        - we need to try every possibility to know the minimum path
            - do it recursively
        
        2 -> 3 -> **5**
        2 -> 4 -> **5** (repeated work spotted)
        """
        row_count = len(triangle)
        memo = {}
        def dfs(idx, curr_row):
            if curr_row == row_count - 1: # dig to the deepest level
                return triangle[curr_row][idx]
            if (idx, curr_row) in memo:
                return memo[(idx, curr_row)]
            
            min_val = min(dfs(idx, curr_row + 1), dfs(idx + 1, curr_row + 1))

            memo[(idx, curr_row)] = min_val + triangle[curr_row][idx]
            return memo[(idx, curr_row)]

        return dfs(0, 0)
