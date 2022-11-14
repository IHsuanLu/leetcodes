class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
            
        finalStack = stack[:-k] if k else stack
        while finalStack and finalStack[0] == '0':
            finalStack.pop(0)
        
        return "".join(finalStack) or "0"