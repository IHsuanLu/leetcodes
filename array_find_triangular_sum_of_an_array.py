from ast import List

# O(n^2), O(1)
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums), 0, -1):
            for j in range(1, i):
                nums[j - 1] += nums[j]
                if nums[j - 1] >= 10:
                    nums[j - 1] %= 10
            
        return nums[0]


# O(n^2), O(n)
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_arr = [-1] * (len(nums) - 1)
            for i in range(1, len(nums)):
                sum_val = nums[i - 1] + nums[i]
                if sum_val >= 10:
                    new_arr[i - 1] = sum_val % 10
                else:
                    new_arr[i - 1] = sum_val
            
            nums = new_arr

        return nums[0]