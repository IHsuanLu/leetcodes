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