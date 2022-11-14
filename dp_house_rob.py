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