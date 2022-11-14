# Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase
# Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.
# Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]


from ast import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost + [0] # minimum cost to climb to the top starting from the ith staircase
        
        for i in range(len(cost) - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
                        
        return min(dp[0], dp[1])