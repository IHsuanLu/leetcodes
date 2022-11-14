from ast import List

# horizontal scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            while prefix != strs[i][:len(prefix)]:
                prefix = prefix[:len(prefix) - 1]
                
                if not prefix:
                    return ""
                
        return prefix


# vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
        
        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        
        return shortest
                    