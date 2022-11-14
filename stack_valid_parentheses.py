class Solution:
    def isValid(self, s: str) -> bool:
        memo = {']':'[', '}':'{', ')':'('}
        stack = []
        for i in range(len(s)):
            if s[i] in memo.values():
                stack.append(s[i])
            elif s[i] in memo:
                if len(stack) == 0:
                    return False
                if stack.pop() != memo[s[i]]:
                    return False
                
        return len(stack) == 0