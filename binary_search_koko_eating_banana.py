from ast import List
import math

# brute force
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            res = 0
            for p in piles:
                res += math.ceil(p / speed)
            
            if res > h:
                speed += 1
            else:
                return speed



# binary search

# works
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min, max speed
        
        while l < r:
            hours = 0
            mid = (l + r) // 2 # speed
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                r = mid
            else:
                l = mid + 1
        
        return r


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min, max speed
        res = r

        while l <= r:
            hours = 0
            mid = (l + r) // 2 # speed
            for p in piles:
                hours += math.ceil(p / mid)
            
            # res = h doesn't mean we find the answer, we need to keep finding til the two pointers meet
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # pointers for the min, max eating speed
        res = r
        while l < r:
            mid = (l + r) // 2 # if the eating speed
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            
            if hours > h: # eat too slow
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid
        
        return res




# ----------------- doesn't work on the last test case -----------------

# [1,1,1,999999999]
# 10
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min, max speed
        
        while l < r:
            hours = 0
            mid = (l + r) // 2 # speed
            for p in piles:
                hours += math.ceil(p / mid)
            
            # res = h doesn't mean we find the answer, we need to keep finding til the two pointers meet
            if hours <= h:
                r = mid # so we don't want to exclude the mid from our answer candidates
            else:
                l = mid + 1
        
        return r