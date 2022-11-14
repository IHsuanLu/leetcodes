class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        # maximum digits possible
        res = [0] * (len(num1) + len(num2))
        
        # 乘法從least significant開始，reverse
        num1 = num1[::-1]
        num2 = num2[::-1]
                
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                temp = int(n1) * int(n2)
                res[i + j] += temp # 先加再取remainder和carry，carry溢出位交給下一輪
                
                remainder = res[i + j] % 10
                carry = res[i + j] // 10
                res[i + j + 1] += carry
                res[i + j] = remainder
        
        # remove unused "0" digits
        last_idx = len(res) - 1
        while last_idx > 0 and res[last_idx] == 0:
            last_idx -= 1
            
        res = res[:last_idx + 1][::-1]
        return "".join([str(n) for n in res])