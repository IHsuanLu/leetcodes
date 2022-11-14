from ast import List

"""
[1, 2, 3, 4]
[1, 2, 3]
[1, 2, 4]
[1, 2]
[1, 3, 4]
[1, 3]
[1, 4]
[1]
[2, 3, 4]
[2, 3]
[2, 4]
[2]
[3, 4]
[3]
[4]
[]
[1]
[]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(curr, path):
            if curr > n:
                if len(path) == k:
                    res.append(path[:])
                return
            
            path.append(curr)
            
            backtrack(curr + 1, path)
            path.pop()
            backtrack(curr + 1, path)
            
        backtrack(1, [])        
        return res


"""
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 4]
[1, 3]
[1, 3, 4]
[1, 4]
[2]
[2, 3]
[2, 3, 4]
[2, 4]
[3]
[3, 4]
[4]
[]
[1]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, path):
            if len(path) == k:  
                res.append(path[:])

            for i in range(curr, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        
        res = []
        backtrack(1, [])
        return res