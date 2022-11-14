from ast import List


class Solution:
    def createSubarray(self, nums: List[int]) -> int:
        res = []
        
        def dfs(start, end):
            if end == len(nums):
                return
            
            if start > end:
                dfs(0, end + 1)
            else:
                subarr = nums[start:end+1]
                res.append(subarr)
                dfs(start + 1, end)
        
        dfs(0, 0)
    
        return res