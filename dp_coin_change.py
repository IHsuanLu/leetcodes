from ast import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(coins, amount, memo):
            if amount in memo:
                return memo[amount]
            
            minCoins = float('inf')
            for c in coins:
                if amount - c >= 0:
                    numOfCoins = dfs(coins, amount - c, memo) + 1
                    minCoins = min(numOfCoins, minCoins)
            
            memo[amount] = minCoins
            return minCoins
        
        rlt = dfs(coins, amount, {0:0})
        return rlt if rlt != float('inf') else -1
        
# DP Solution
# dp array stores number of coins required for summing to particular amount

# [1,3,4,5], target = 7
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2 (1 + dp[1])
# dp[3] = 1
# dp[4] = 1
# dp[5] = 1
# dp[6] = 2
# dp[7] = 2

# check every number in the list, and see if we select one of them, what will be remaining.
# further, based on the previous result, we can easily get the minimum

# choose 1
# dp[7] = 1 + dp[6] = 3

# choose 3
# dp[7] = 1 + dp[4] = 2

# choose 4
# dp[7] = 1 + dp[3] = 2

# choose 5
# dp[7] = 1 + dp[2] = 2




class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1