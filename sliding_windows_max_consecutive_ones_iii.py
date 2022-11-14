from ast import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        memo = []
        longest = l = 0
    
        for r in range(len(nums)):
            if nums[r] == 0:
                memo.append(r)
            
            if len(memo) > k: 
                l = memo.pop(0) + 1
                
            longest = max(longest, r - l + 1)

        return longest
