from ast import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # enough length to check to equalivent
                if i <= len(s) - len(w):
                    if s[i: i + len(w)] == w:
                        dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break

        return dp[0]
