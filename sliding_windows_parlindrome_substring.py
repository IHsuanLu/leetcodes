class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # odd length
            r = l = i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                # valid parlindrome
                res += 1
                r += 1
                l -= 1
            
            # even length
            l, r = i, i + 1            
            while r < len(s) and l >= 0 and s[r] == s[l]:
                # valid parlindrome
                res += 1
                r += 1
                l -= 1
                
        return res