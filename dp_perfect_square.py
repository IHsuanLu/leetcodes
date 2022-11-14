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
        def dfs(amount, memo):
            if amount in memo:
                return memo[amount]
            
            minCoins = float('inf')
            x = int(sqrt(n))
            for i in range(1, x + 1):
                square = i * i
                if amount - square >= 0:
                    numOfCoins = dfs(amount - square, memo) + 1
                    minCoins = min(numOfCoins, minCoins)
            
            memo[amount] = minCoins
            return minCoins
        
        rlt = dfs(n, {0:0})
        return rlt if rlt != float('inf') else -1