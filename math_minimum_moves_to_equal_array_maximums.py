from ast import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ele = max(nums)
        min_ele = min(nums)
        
        checked_max = False
        res = max_ele - min_ele
        for num in nums:
            if num == min_ele:
                continue
    
            if num == max_ele and not checked_max:
                checked_max = True
                continue
                
            res += num - min_ele
        
        return res


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ele = min(nums)
        res = 0
        
        for n in nums:
            res += n - min_ele
    
        return res