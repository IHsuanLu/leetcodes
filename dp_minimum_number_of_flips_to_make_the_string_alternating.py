"""
intuition ->

given 111000
there are only two possibility of alternating string, 101010 and 010101

check the number of differences between 111000 and both 101010 and 010101
"""

# O(n^2) -> TLE
class Solution:
    def minFlips(self, s: str) -> int:
        targets = ["0", "1"]
        targets[0] += "1" if targets[0][-1] == "0" else "0"
        targets[1] += "0" if targets[1][-1] == "1" else "1"

        def check_diff(m, t):
            res = 0
            for i in range(len(m)):
                if m[i] != t[i]:
                    res += 1
            return res
        
        min_diff = [len(s)]
        def dfs(idx):
            if idx == len(s):
                return
            
            for t in targets:
                min_diff[0] = min(min_diff[0], check_diff(s[idx:] + s[:idx], t))
            
            dfs(idx + 1)

        dfs(0)
        return min_diff[0]