from ast import List

class Solution:
    def rob(self, nums: List[int]) -> int:    
        return max(self.helpers(nums[1:]), self.helpers(nums[:-1])) if len(nums) != 1 else nums[0]

    def helpers(nums):
        robPrev, robNext = 0, 0
        for n in nums:
            curr = max(robPrev + n, robNext)
            robPrev = robNext
            robNext = curr
        
        return robNext

# top-down
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(idx, max_length, memo):
            if idx in memo:
                return memo[idx]

            if idx >= max_length:
                return 0

            sum1 = nums[idx] + dfs(idx + 2, max_length, memo)
            sum2 = dfs(idx + 1, max_length, memo)
            memo[idx] = max(sum1, sum2)
            return memo[idx]

        return max(dfs(0, len(nums) - 1, {}), dfs(1, len(nums), {}))