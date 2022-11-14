# 0 -> 0 0 0 0 -> 0
# 1 -> 0 0 0 1 -> 1 + dp[n - 1]
# 2 -> 0 0 1 0 -> 1 + dp[n - 2]
# 3 -> 0 0 1 1 -> 1 + dp[n - 2]
# 4 -> 0 1 0 0 -> 1 + dp[n - 4]
# 5 -> 0 1 0 1 -> 1 + dp[n - 4]
# 6 -> 0 1 1 0 -> 1 + dp[n - 4]
# 7 -> 0 1 1 1 -> 1 + dp[n - 4]
# 8 -> 1 0 0 0 -> 1 + dp[n - 8]

from ast import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        offset = 1 # next bit significant number; 1, 2, 4, 8, 16....
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
            
        return dp
        