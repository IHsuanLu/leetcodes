from ast import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        total = 0
        for char in tokens:
            if char.isnumeric() or char.strip('-').isnumeric():
                stack.append(int(char))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                res = 0
                
                if char == "+":
                    res = operand_1 + operand_2
                elif char == "-":
                    res = operand_1 - operand_2
                elif char == "*":
                    res = operand_1 * operand_2
                elif char == "/":
                    res = int(operand_1 / operand_2)

                stack.append(res)
                
        return stack[0]
       