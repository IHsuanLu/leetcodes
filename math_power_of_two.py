class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        k = 0
        res = 1
        while res < n:
            res = 1 << (1 + k)
            k += 1
            if n == res:
                return True

        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (1 << 31) % n == 0