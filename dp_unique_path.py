# Bottom up DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]

# Top down DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_num, col_num = m, n
        memo = {}
        def dfs(row, col):
            if row == row_num - 1 or col == col_num - 1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[(row, col)]
        
        return dfs(0, 0)
