from ast import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            if len(path) >= len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                
                backtrack(path, used)
                
                path.pop()
                used[i] = False
            
        
        backtrack([], [False] * len(nums))
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, memo):
            if len(path) >= len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in memo:
                    continue
                
                path.append(nums[i])
                memo.add(nums[i])
                
                backtrack(path, memo)
                
                path.pop()
                memo.remove(nums[i])
            
        memo = set()
        backtrack([], memo)
        return res


# Neet code version -> no need extra space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums) # [[3,2], [2,3]]
            for perm in perms:
                perm.append(n) # [[3,2,1], [2,3,1]]
            
            res.extend(perms) # append multiple elements to an array
            nums.append(n) # [2,3,1], so next time pop(0) will get "2"
        
        return res