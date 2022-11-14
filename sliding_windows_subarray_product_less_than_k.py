from ast import List

# sliding windows
# we can only use that if all the Ns are >= 1
# count of subarray => the sum of (r - l + 1) of every iteration

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        res = 0
        l = 0
        for r, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[l]
                l += 1

            res += r - l + 1
        
        return res