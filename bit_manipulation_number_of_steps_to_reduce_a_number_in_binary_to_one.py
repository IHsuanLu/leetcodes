class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        s = list(s)
        while s != ["1"]:
            if s[-1] == "0":
                # even
                s = s[:-1]
            elif s[-1] == "1":
                # odd
                carry = 0
                for i in range(len(s) - 1, -1, -1):
                    num = int(s[i])
                    if i == len(s) - 1:
                        num += 1

                    num += carry
                    carry = num // 2
                    s[i] = "0" if num % 2 == 0 else "1"
                
                if carry and len(s) != 1:
                    s = ["1"] + s
            
            res += 1
            
        return res


class Solution:
    def numSteps(self, s: str) -> int:
        s = [int(digit) for digit in s]
        res = 0
        carry = 0
        
        while len(s) > 1:
            if (s[-1]+carry)%2:
                res += 2
                carry = 1
            elif s[-1]+carry == 2:
                res += 1
            else:
                carry = 0
                res += 1

            s.pop()
            
        if s[-1] + carry == 2:
            res += 1

        return res