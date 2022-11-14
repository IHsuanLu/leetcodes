from ast import List

# l runs after r is fine some times

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmap = {}
        for c in p:
            hmap[c] = hmap.get(c, 0) + 1
        
        res = []
        l = 0        
        for i, c in enumerate(s):
            if c in hmap:
                hmap[c] -= 1
            else:
                hmap[c] = -1
                
            while hmap[c] < 0:
                hmap[s[l]] += 1
                l += 1
            
            if i - l + 1 == len(p):
                res.append(l)
                
        return res