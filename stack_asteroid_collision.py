from ast import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            if aster > 0:
                stack.append(aster)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(aster):
                    stack.pop()
                       
                if not stack or stack[-1] < 0 and aster < 0:
                    stack.append(aster)
                    continue
                    
                if stack[-1] == -aster:
                    stack.pop()
            
        return stack