class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}

        while True:
            if n in memo:
                break

            numbers = [int(a) for a in str(n)]
            res = 0
            for num in numbers:
                res += num * num
            
            memo[n] = res
            n = res
        
        return n == 1