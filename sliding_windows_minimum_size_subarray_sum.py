from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        conduct a sliding windows algorithm
            -> if the sum of the elements in the winodow >= target
                -> we expand the window
            -> otherwise, decrease the window
            -> record thee length of the window once we get to the solution
        """

        min_val = float('inf')
        curr_sum = 0
        j = 0
        # expand the window
        for i in range(len(nums)):
            curr_sum += nums[i]

            # shrink the window
            while curr_sum > target:
                min_val = min(min_val, i - j + 1)
                curr_sum -= nums[j]
                j += 1

            if curr_sum == target:
                min_val = min(min_val, i - j + 1)

        return min_val if min_val != float('inf') else 0