from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_sum = max(max_sum, current_max)

        return max_sum