# store the number along with the paramtheses into the stack

# 54[ab6[cd]]
# stack: 5,4,[,a,b,6,[,c,d
# meet: ]
# pop until: [
# stack: 5,4,[,a,b,6
# get string "cd"
# keep popping until character is no longer digit
# stack: 5,4,[,a,b
# get digit `6`

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # id
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # pop "["
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * substr)
                
        return "".join(stack)