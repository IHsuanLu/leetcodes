# monotonic decreasing stack
# and keep track of the min value came before (i value)
# the top of the stack should be j value
# and we are looking for k value while loopong thru


# monotonic increasing stack is not gonna work
# the following will fail the test case like [3,5,0,3,4]
from ast import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minimum = nums[0]
        
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            
            if stack and n > stack[-1][1]:
                return True
            
            stack.append((n, minimum))
            minimum = min(minimum, n)
        
        return False



class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        
        poped = False
        while nums:
            nxt = nums.pop(0)
            while stack and nxt < stack[-1]:
                stack.pop()
                poped = True
            
            stack.append(nxt)
            
            if poped and len(stack) >= 2:
                return True
            
            poped = False
        
        return False
