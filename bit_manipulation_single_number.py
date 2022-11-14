# utilize xor to find the single value in the list
# 1 xor 1 = 0
# 1 xor 0 = 1
# 0 xor 0 = 0
#
# 4 -> 1 0 0
# 1 -> 0 0 1
# 2 -> 0 1 0
# 1 -> 0 0 1
# 2 -> 0 1 0
from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n, it's ideal to set default as 0
        
        for n in nums:
            res = res ^ n
        
        return res
        