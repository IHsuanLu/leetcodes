# divide the quesiton in to the sub question
# [1, 5, 11 ,5], target = 11
#   -> [X, 5, 11 ,5], i = 1, target = 10 # choose 1
#   -> [X, 5, 11 ,5], i = 1, target = 11 # not choose 1

# time complexity -> O(2^N) -> O(n * sum(nums))
# memory complexity -> O(sum(nums))

# for t in subarray:
#  if t == target:
#      return True
#  if t + 1 == target:
#      return True

# store the possible sum in a set, iterating in the reverse order, add the next number to every element in the set, creating new elements
# set = {0, 5, 11, 16, 10, 21, 1, 6, 12, 17, 22}
# return True if the set contains target
from ast import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total / 2
        memo = set([0])

        while nums:
            nxt = nums.pop(0)
            curr = memo.copy()
            for n in curr:
                memo.add((nxt + n))

        return target in memo