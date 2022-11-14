# draw the hierarchy graph for a nicer understanding
from ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            
            # decision to include nums[i]
            subset.append(nums[idx])
            dfs(idx + 1)
        
            # decision NOT to include nums[i]
            subset.pop() # pop the arrar but use the same index
            dfs(idx + 1)
        
        dfs(0)
        return res