class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
    
        hmap = {} # key: char, num: count
        max_val = 0
        l = 0
        for r, c in enumerate(s):
            hmap[c] = hmap.get(c, 0) + 1
            
            while len(hmap) > k:
                hmap[s[l]] -= 1
                
                if hmap[s[l]] == 0:
                    del hmap[s[l]]

                l += 1
                    
            max_val = max(r - l + 1, max_val)
            
        return max_val