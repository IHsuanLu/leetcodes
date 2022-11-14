# take n and % 2 to check the last bit is 0 or 1
# bit shift to the right by one position (natively support by programming language)

# Neet code solution
class Solution:
    def hammingWeight(self, n: int) -> int:        
        res = 0
        
        while n:
            res += n % 2 # add one if 1 else continue
            n = n >> 1 # bit shift
        
        return res

# format and count
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = "{0:b}".format(n)
        
        res = 0
        for c in s:
            if c == '1':
                res += 1
        
        return res