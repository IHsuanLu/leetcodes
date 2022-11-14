# We need to sort the given array (nlogn)
# Skip the number we decide not to include based on the decision tree (shift the pointer)

from ast import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        subset = []
        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # All subsets that include nums[i]
            subset.append(nums[idx])
            dfs(idx + 1)
                    
            # All subsets that do not include nums[i]
            subset.pop()
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]: # skip the duplicate number
                idx += 1
            dfs(idx + 1)
        
        dfs(0)
        return res