# Two Pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        sp = tp = 0
        while tp < len(t) and sp < len(s):
            if  s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)

# Recursion
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        def dfs(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            if s[i] == t[j]:
                if dfs(i + 1, j + 1):
                    return True
            else:
                if dfs(i, j + 1):
                    return True
            
            return False

        return dfs(0, 0)