from ast import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair (value, idx)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx) 
            
            stack.append((temperatures[i], i))
        
        return res
