# FAV

# O(n), O(n)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                groups[-1] += 1
            else:
                groups.append(1)

        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])

        return res

# O(n^2), O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            if s[i] + s[i - 1] in ["01", "10"]:
                res += 1
                l, r = i - 1, i
                while l - 1 >= 0 and s[l] == s[l - 1] and r + 1 < len(s) and s[r] == s[r + 1]:
                    l, r = l - 1, r + 1
                    res += 1

        return res