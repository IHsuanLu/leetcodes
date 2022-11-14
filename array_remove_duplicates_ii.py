from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, insert_idx = -1, 0
        for r in range(len(nums)):
            if r + 1 < len(nums) and nums[r] != nums[r+1] or r == len(nums) - 1:
                length = min(r - l, 2) 
                nums[insert_idx:insert_idx + length] = [nums[r]] * length
                insert_idx += length
                l = r
    
        return insert_idx