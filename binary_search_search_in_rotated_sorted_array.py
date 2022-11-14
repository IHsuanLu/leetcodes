from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
       
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                if nums[start] <= target and nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid]>target:
                if target <= nums[end] and nums[end] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
       
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1 
