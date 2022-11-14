class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = x < 0
        x = abs(x)
        while x:
            remainder = x % 10
            x = x // 10
            res = res * 10 + remainder
        
        if neg:
            res *= -1
            
        if res > 2**31 or res < -2**31:
            return 0
                 
        return res 