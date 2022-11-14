from ast import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(idx, curr, total):
            if total == target:
                res.append(curr.copy()) 
                return
            
            if total > target or idx >= len(candidates):
                return
            
            # All subsets that include nums[i]
            curr.append(candidates[idx])
            dfs(idx + 1, curr, total + candidates[idx])
            
            # All subsets that do not include nums[i]
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            
            dfs(idx + 1, curr, total)
        
        dfs(0, [], 0)
        return res