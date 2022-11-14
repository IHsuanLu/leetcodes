class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        found_misalignment = False
        l = r = 0
        
        while l < len(s) and r < len(t):
            if s[l] != t[r]:
                if found_misalignment:
                    return False
                found_misalignment = True
                
                if len(s) < len(t):
                    l -= 1
                elif len(s) > len(t):
                    r -= 1
            l += 1
            r += 1
        
        return True

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        # same length
        if len(s) == len(t):
            replaced = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    replaced += 1
            return replaced == 1
        # different length
        else:
            long_str = s if len(s) > len(t) else t
            short_str = s if len(s) < len(t) else t
            
            found_misalignment = False
            i = j = 0
            while i < len(long_str) and j < len(short_str):
                if long_str[i] != short_str[j]:
                    if found_misalignment:
                        return False
                    found_misalignment = True
                    j -= 1
    
                i += 1
                j += 1
            
            return True
