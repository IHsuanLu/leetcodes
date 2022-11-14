from ast import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        min_diff = float('inf')
        
        l = 0
        for r in range(k - 1, len(nums)):
            min_diff = min(min_diff, nums[r] - nums[l])
            l += 1
        
        return min_diff