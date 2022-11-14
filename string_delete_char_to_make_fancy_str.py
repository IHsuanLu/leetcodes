class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        count = 1
        
        for i, c in enumerate(s):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                res += c
                
        return res