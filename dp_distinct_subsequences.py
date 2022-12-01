# time complexity: O(m * n)
# space complexity: O(m * n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        memo = {}
        def dfs(s_idx, t_idx):
            if t_idx == len(t):
                return 1
            if s_idx >= len(s):
                return 0
            
            if (s_idx, t_idx) in memo:
                return memo[(s_idx, t_idx)]
            
            # Always make this recursive call
            # cause even in the match case, s[s_idx] == t[t_idx],
            # we can still skip the character and see if there are matches further on
            matches = dfs(s_idx + 1, t_idx)

            if s_idx < len(s) and t_idx < len(t) and s[s_idx] == t[t_idx]:
                matches += dfs(s_idx + 1, t_idx + 1)
            
            memo[(s_idx, t_idx)] = matches
            return matches
        
        res = dfs(0, 0)
        return res