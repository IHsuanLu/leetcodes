from ast import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        cur_min = -float('inf')
        
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == nums[right]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                cur_min = nums[mid]
                right = mid
            else:
                cur_min = nums[right]
                left = mid + 1

        return cur_min