class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        
        for i in range(hlen - nlen + 1):
            if haystack[i:i+nlen] == needle:
                return i
        
        return -1