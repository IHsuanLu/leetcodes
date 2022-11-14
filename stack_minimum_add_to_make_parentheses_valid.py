class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                
                if not stack or stack[-1] == ")":
                    stack.append(c)
        
        return len(stack)


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(": 
                stack.append(c)
            else:
                if len(stack) and stack[-1] == '(': 
                    stack.pop()
                else: 
                    stack.append(c)

        return len(stack)


# w/o stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = count = 0
        
        for c in s:
            if c == "(":
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    count += 1
        
        return opening + count