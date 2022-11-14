class Solution:
    def canJump(self, nums):
        if len(nums)<2:
            return True
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1]<i:
                return False
            dp[i] = max(dp[i-1], i + nums[i])
        return dp[-1] >= len(nums)-1

# Greedy
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return True if goal == 0 else False