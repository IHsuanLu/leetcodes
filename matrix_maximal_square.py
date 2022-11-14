from ast import List

'''
[
 ["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]
]


3 4
3 3
3 2
3 1
3 0
2 4
2 3
2 2
2 1
2 0
1 4
1 3
1 2
1 1
1 0
0 4
0 3
0 2
0 1
0 0
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_num, col_num = len(matrix), len(matrix[0])
        
        memo = {}
        def dfs(row, col, memo):
            if row >= row_num or col >= col_num:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            if matrix[row][col] == "0":
                memo[(row, col)] = 0
            
            down = dfs(row + 1, col, memo)
            right = dfs(row, col + 1, memo)
            diag = dfs(row + 1, col + 1, memo)
                        
            if matrix[row][col] == "1":
                memo[(row, col)] = 1 + min(down, right, diag)
            
            return memo[(row, col)]
        
        dfs(0, 0, memo)
        maxVal = max(memo.values())
        
        # since we don't return if meeting 0 nor 1, after one dfs, position will be covered; that's why we don't need to call dfs for every cell
        
        # maxVal = 0
        # for row in range(row_num):
        #     for col in range(col_num):
        #         res = dfs(row, col, memo)
        #         maxVal = max(maxVal, res)
        
        return maxVal * maxVal
            


# not that efficient but still works
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_num, col_num = len(matrix), len(matrix[0])
        
        memo = {}
        def dfs(row, col, memo):
            if row >= row_num or col >= col_num:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            if matrix[row][col] == "0":
                return 0
            
            down = dfs(row + 1, col, memo)
            right = dfs(row, col + 1, memo)
            diag = dfs(row + 1, col + 1, memo)
                        
            if matrix[row][col] == "1":
                memo[(row, col)] = 1 + min(down, right, diag)
            
            return memo[(row, col)]
        
        
        maxVal = 0
        for row in range(row_num):
            for col in range(col_num):
                res = dfs(row, col, memo)
                maxVal = max(maxVal, res)
        
        return maxVal * maxVal
            
                    