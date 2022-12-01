from ast import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_val = [0]
        def backtrack(idx, path):
            # redundant
            # if idx == len(arr):
            #     if len(set(path)) == len(path):
            #         max_val[0] = max(max_val[0], len(path))
            #     return
            
            if len(set(path)) != len(path):
                return
            
            max_val[0] = max(max_val[0], len(path))
            
            for i in range(idx, len(arr)):
                backtrack(i + 1, path + arr[i])
                
        backtrack(0, "")
        return max_val[0]