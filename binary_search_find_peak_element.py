from ast import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < len(nums):
                if nums[mid] > nums[mid + 1]:
                    boundary_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid

        return boundary_index