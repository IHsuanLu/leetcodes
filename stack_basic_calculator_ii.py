class Solution:
    def calculate(self, s):
        res = 0
        stack = []
        sign = "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
                
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(res)
                elif sign == "-":
                    stack.append(-res)
                elif sign == "*":
                    stack.append(stack.pop()*res)
                else:
                    stack.append(int(stack.pop()/res))
                res = 0
                sign = s[i]

        return sum(stack)