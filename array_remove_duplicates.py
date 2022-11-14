# instead of removing duplicates, we can think of it as finding unique numbers and replace it to the front index
from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[valid_idx] = nums[i]
                valid_idx += 1
        
        return valid_idx