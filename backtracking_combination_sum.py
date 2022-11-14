from ast import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        def dfs(idx, cur_arr, total):
            if total == target:
                # we're reusing the same arr in very recursive call, and 
                # we don't wanna modify it
                rlt.append(cur_arr.copy())
                return
            if total > target or idx >= len(candidates):
                return
            
            # include the certain candidate with index equals to idx
            cur_arr.append(candidates[idx])
            dfs(idx, cur_arr, total + candidates[idx]) # use the same index cause duplication is allowed
            
            # pop the arbitrary one and move on to the next index
            cur_arr.pop()
            dfs(idx + 1, cur_arr, total)
        
        dfs(0, [], 0)
        return rlt