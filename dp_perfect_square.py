# nearly identical to coin change problem
# time complexity O(n * sqrt(n))

# draw the decision tree, divide the question into sub-problems
# n = 12
#    -> 12 - 1^2 -> n(11)
#    -> 12 - 2^2 -> n(8)
#    -> 12 - 3^2 -> n(3)

# either top-down, dfs + memoization (refer to coin change)
# or bottom-up, dp
from cmath import sqrt

# bottom-up solutions
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        # number of times required for summing to particular amount with perfect square number
        dp[0] = 0
        
        for target in range(1, n + 1):
            for val in range(1, target + 1):
                square = val * val
                if target - square < 0:
                    break
                
                dp[target] = min(dp[target], 1 + dp[target - square])
                
        return dp[n]


# top-down solutions
class Solution:
    def numSquares(self, n: int) -> int:
        def dfs(remaining, memo):
            if remaining == 0:
                return 0
            
            if remaining in memo:   
                return memo[remaining]
            
            min_total = float('inf')
            for num in range(int(sqrt(n)), 0, -1):
                pn = num ** 2
                if remaining - pn >= 0:
                    total = dfs(remaining - pn, memo) + 1
                    min_total = min(min_total, total)
            
            
            memo[remaining] = min_total
            return min_total
        
        res = dfs(n, {})
        return res if res != float('inf') else -1

# bfs, but use set to eliminate duplicate
#   -> directly return if match found, since it'll always be the minimum