from ast import List


# optimal backtrack
# return the result immediately, 
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = set(nums)
        
        def backtrack(curr, path):
            if curr == len(nums[0]):
                res = "".join(path[:])
                return None if res in strSet else res
            
            res = backtrack(curr + 1, path)
            if res:
                return res

            # update the solution to "1" before backtrack and call the next recursion
            path[curr] = "1"
            
            res = backtrack(curr + 1, path)
            if res:
                return res
            
        
        return backtrack(0, ["0" for _ in nums])


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        
        combinations = []
        counter = {0: length, 1: length}
        def backtrack(path, memo):
            if len(path) == length:
                combinations.append(path)
                return 
            
            for n in memo:
                if memo[n] > 0:
                    path = path + str(n)
                    memo[n] -= 1
                    
                    backtrack(path, memo)
                    
                    path = path[:-1]
                    memo[n] += 1
            
            
        backtrack("", counter)
        
        for c in combinations:
            if c not in nums:
                return c
        
        return ""