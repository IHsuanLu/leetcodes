# right cursor can keep going; we can use while loop for the left cursor to follow up

from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        minVal = float('inf')
        curr = 0
        while r < len(nums):
            curr += nums[r]
            while curr >= target:
                minVal = min(minVal, r - l + 1)
                curr -= nums[l]
                l += 1
            
            r += 1
        
        return minVal if minVal != float('inf') else 0



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        minVal = float('inf')
        curr = 0
        while r < len(nums):
            if curr < target:
                curr += nums[r]
            else:
                minVal = min(minVal, r - l + 1)
                curr -= nums[l]
                l += 1
                
            if curr < target:
                r += 1                
            
        
        return minVal if minVal != float('inf') else 0