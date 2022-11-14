from ast import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        def backtrack(path, memo):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in memo:
                if memo[n] > 0:
                    path.append(n)
                    memo[n] -= 1

                    backtrack(path, memo)

                    path.pop()
                    memo[n] += 1
                
        backtrack([], counter)
        return res