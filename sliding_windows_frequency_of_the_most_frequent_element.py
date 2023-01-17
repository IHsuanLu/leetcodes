#FAV
from ast import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_freq = 0
        curr_total = 0
        l = 0

        # expanding the window
        for r in range(len(nums)):
            curr_total += nums[r]

            # shrinking the window
            # nums[r] is the number we seek to align the numbers in the window with
            while nums[r] * (r - l + 1) > curr_total + k:
                curr_total -= nums[l]
                l += 1
            
            # valid solution
            max_freq = max(max_freq, (r - l + 1))
        
        return max_freq