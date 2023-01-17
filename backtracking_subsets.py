# FAV

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


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(idx):
            res.append(subset.copy())
            
            for i in range(idx + 1, len(nums)):
                subset.append(nums[i])
                dfs(i)
                subset.pop()

        dfs(-1)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(idx):
            res.append(subset.copy())
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return res