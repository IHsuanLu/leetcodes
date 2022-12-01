from ast import List

# The intuition:
#    When the unmatch occurs, nums[i] > nums[i + 1], there are two ways to consider
#        1. modify nums[i]
#        2. modify nums[i + 1]

# To fix it correctly, we need to check nums[i - 1]
#   If you observe 20 30 10, we will find there is an inversion at 30 / 10. Because a[i-1] > a[i+1], we change a[i+1] to a[i]
#       -> 不得以要改成 >= nums[i]的才能符合 non-decreasing
#   If you observe 20 30 25, we will find there is an inversion at 30 / 25. Because a[i-1] < a[i+1], we change a[i] to a[i+1]
#       -> fix within the three values; a[i] 改成 a[i - 1] or a[i + 1] 皆可 -> 不影響除了這三個數字之外的element
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        unmatched_detected = False
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]: # 15, 30, 20
                    nums[i] = nums[i + 1]
                elif nums[i - 1] > nums[i + 1]: # 25, 30, 20
                    nums[i + 1] = nums[i]
                
                if unmatched_detected:
                    return False
                unmatched_detected = True

        return True


# This is not going to work
#   -> Case like `[3,4,2,3]` has only one unmatch, where nums[i] < nums[i - 1], 
#      yet it's still impossible to be non-decreaing array with only one replacement 
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        unmatched_detected = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if unmatched_detected:
                    return False
                unmatched_detected = True
                
        return True