# use [&](logic and) to figure out which bit is it
# 0 & 1 = 0
# 1 & 1 = 1

# use [|](logic or) to fill in the result
# 0 | 1 = 1
# 0 | 0 = 0

## << shift to the left, 01 << 10
## >> shift to the right, 10 >> 01


# bit manipulations
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1 # get the ith bit    
            res = res | (bit << (31 - i)) # put the bit into the (31 - i)th spot of the res 
        return res


# reverse string
class Solution:
    def reverseBits(self, n: int) -> int:
        s = "{0:b}".format(n)
        while len(s) < 32:
            s = '0' + s

        s = s[::-1]
        return int(s, 2)
