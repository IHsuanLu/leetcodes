from ast import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix_sum = [0] * len(nums)
        right_prefix_sum = [0] * len(nums)      
        
        left_prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            left_prefix_sum[i] = left_prefix_sum[i-1] + nums[i]
        
        right_prefix_sum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_prefix_sum[i] = right_prefix_sum[i+1] + nums[i]
        
        for i in range(len(right_prefix_sum)):
            if right_prefix_sum[i] == left_prefix_sum[i]:
                return i
            
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            if left_sum == (total - left_sum - n):
                return i
            left_sum += n
        return -1