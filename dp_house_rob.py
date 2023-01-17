from ast import List

# [1, 2, 3, 1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        robPrev, robNext = 0, 0

        for n in nums:
            curr = max(robPrev + n, robNext)
            robPrev = robNext
            robNext = curr
        
        return robNext


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dfs + memoization
        """
        memo = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]

            sum1 = nums[idx] + dfs(idx + 2)
            sum2 = dfs(idx + 1)
            memo[idx] = max(sum1, sum2)
            return memo[idx]

        return dfs(0)