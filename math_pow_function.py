class Solution:
    def myPow(self, x: float, n: int) -> float:
        def traverse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            # O(logn), 2^10 = 2^5 * 2^5
            res = traverse(x, n // 2)
            res = res * res
            
            return res if n % 2 == 0 else x * res # 2^5 = 2*2^2*2^2
        
        res = traverse(x, abs(n))
        return res if n >= 0 else 1 / res