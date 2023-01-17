# FAV

from ast import List

# Binary Search
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sums = [] # (sum, index)
        for i, c in enumerate(s):
            if c == "|":
                if prefix_sums:
                    prefix_sums.append((prefix_sums[-1][0] + 1, i))
                else:
                    prefix_sums.append((1, i))

        def binary_search(target):
            l, r = 0, len(prefix_sums) - 1
            while l < r:
                mid = (l + r) // 2
                if prefix_sums[mid][1] < target:
                    l = mid + 1
                elif prefix_sums[mid][1] > target:
                    r = mid
                else:
                    return mid
            
            return r

        if not prefix_sums:
            return [0]

        res = []
        for x, y in queries:
            l = binary_search(x)
            r = binary_search(y)
            if r > 0 and y < prefix_sums[r][1]:
                r -= 1
    
            if l > r:
                res.append(0)
                continue
            
            res.append(prefix_sums[r][1] - prefix_sums[l][1] - (prefix_sums[r][0] - prefix_sums[l][0]))

        return res

# TLE
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        brute force:
            -> acutally create substring and find out the number of plates between candles
                -> sliding windows

        -> a lot of repetitive works
        
        -> prefix sum solution
            -> keep track on the accumulated count of the plates and candles
        """
        prefix_sums = [] # (sum, index)
        for i, c in enumerate(s):
            if c == "|":
                if prefix_sums:
                    prefix_sums.append((prefix_sums[-1][0] + 1, i))
                else:
                    prefix_sums.append((1, i))
            
        res = []
        for x, y in queries:
            l, r = 0, len(prefix_sums) - 1
            while l < len(prefix_sums) and prefix_sums[l][1] < x:
                l += 1
            
            while r > 0 and prefix_sums[r][1] > y:
                r -= 1
            
            if l > r:
                res.append(0)
                continue
            
            res.append(prefix_sums[r][1] - prefix_sums[l][1] - (prefix_sums[r][0] - prefix_sums[l][0]))

        return res

# TLE
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        brute force:
            -> acutally create substring and find out the number of plates between candles
                -> sliding windows

        -> a lot of repetitive works
        
        -> prefix sum solution
            -> keep track on the accumulated count of the plates and candles
        """
        prefix_sums = [[0, 0] for _ in range(len(s))] # [plate_count, candle_count]
        for i, c in enumerate(s):
            plate_count = 1 if c == "*" else 0
            candle_count = 1 if c == "|" else 0
            if i > 0:
                plate_count += prefix_sums[i - 1][0]
                candle_count += prefix_sums[i - 1][1]
            prefix_sums[i] = [plate_count, candle_count]
        
        res = []
        for x, y in queries:
            l, r = x, y
            if s[l] == "*":
                while l < len(s) and prefix_sums[l][1] == prefix_sums[x][1]:
                    l += 1
            if s[r] == "*":
                while r > 0 and prefix_sums[r][1] == prefix_sums[y][1]:
                    r -= 1

            if l > r:
                res.append(0)
                continue
            
            res.append(prefix_sums[r][0] - prefix_sums[l][0])

        return res