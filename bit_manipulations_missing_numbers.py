from ast import List

# [xor](exclusive or, '^') -> 2 ^ 3 -> 10 ^ 11 -> 01 (different gets 1; same gets 0)
# why "xor" helpful in the case?
#   5 ^ 3 ^ 5 == 5 ^ 5 ^ 3 == 3 (order does not matter)
#   [0, 1, 2, 3] ^ [0, 1, 3] => get 2

# bit manipulations
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res


# Math solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total = 0
        for n in nums:
            total += n
        
        return int((length * (length + 1)) / 2) - total 