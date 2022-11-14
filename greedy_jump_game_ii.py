# think of it as BFS, but implement it as sliding windows
# l, r indicate the selections of current jump

# how to determine the next boundary?
#  -> look at who can jump the farthest; left = right + 1, right = farthest point possible

# takeaways: BFS on an array can be done with two pointers
from ast import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0 # indicate the selection of current jump
        
        while r < len(nums) - 1:
            farthest_idx = 0
            for i in range(l, r + 1):
                farthest_idx = max(farthest_idx, i + nums[i])
            
            l = r + 1
            r = farthest_idx
            res += 1
        
        return res
