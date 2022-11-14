
# recursive + memoization; 
# time: O(M^N) , M = number of coins we have; N is the amount (height of the tree)
# space: O(M^N) 

# first thing is how do we avoid getting duplicate?
#   -> in the decision tree, we exclude the selected number on the first layer previously
#   -> to do that, **we are gonna maintain a pointer, and we don't use the number prior the pointer**
from ast import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(i, sub_amount):
            if sub_amount == amount:
                return 1
            if sub_amount > amount:
                return 0
            if i >= len(coins): #index out of bound
                return 0
            if ((i, sub_amount) in memo):
                return memo[(i, sub_amount)]
            
            # dfs(i, sub_amount + coin[i]), if we are choosing the coin at index i
            # dfs(i + 1, sub_amount), if we skip the coin at index i
            res = dfs(i, sub_amount + coins[i]) + dfs(i + 1, sub_amount)
            
            memo[(i, sub_amount)] = res
            return res

        return dfs(0, 0)

# dp; O(M^N)
# time: O(M^N) , M = number of coins we have; N is the amount (height of the tree)
# space: O(M^N)

#         coins
#           1, 2, 5
# amounts [
#       0  [1, 1, 1, 1], 
#       1  [0, 0, 0, 0], 
#       2  [0, 0, 0, 0], 
#       3  [0, 0, 0, 0], 
#       4  [0, 0, 0, 0], 
#       5  [0, 0, 0, 0]
#         ]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                
                # skipping the coin at index i
                # analogous to dfs(i + 1, sub_amount)
                dp[a][i] = dp[a][i+1] 
                
                # the case we do use the coin
                if a - coins[i] >= 0: # if the amount leftover is greater than 0
                    # analogous to dfs(i, sub_amount + coins[i])
                    dp[a][i] += dp[a - coins[i]][i]
        
        return dp[amount][0]