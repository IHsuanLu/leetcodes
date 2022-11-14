# keep the state of are we buying or selling next, using boolean
# draw the decision tree, https://youtu.be/I7j0F7AHpb8?t=435

# O(2^N) -> O(2N) with caching
# (idx, bool for buy, sell); idx -> the index we are at in the pricing array; 
from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying or selling ?
        # if buy -> i + 1
        # if sell -> i + 2 (for mandatory cooldown)
        
        dp = {} # key = (idx, buying); val = max_profit
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy_profit = dfs(i + 1, not buying) - prices[i]
                cool_down_profit = dfs(i + 1, buying) # do nothing
                dp[(i, buying)] = max(buy_profit, cool_down_profit)
            else:
                # selling                
                sell_profit = dfs(i + 2, not buying) + prices[i] # directly move the pointer to i + 2 so that we don't have to maintain the third state
                cool_down_profit = dfs(i + 1, buying)  # do nothing
                dp[(i, buying)] = max(sell_profit, cool_down_profit)

            return dp[(i, buying)]
        
        dfs(0, True)
        return dp[(0, True)]
        