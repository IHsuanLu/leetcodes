# FAV

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        memo = {}
        def dfs(idx, prev):
            if idx == len(s):
                return 0

            if (idx, prev) in memo:
                return memo[(idx, prev)]

            min_val = float('inf')
            if prev == s[idx]:
                min_val = min(min_val, dfs(idx + 1, s[idx]))
            else:
                if prev == '1': # s[idx] == 0 and prev == 1
                    min_val = min(min_val, dfs(idx + 1, '1') + 1)
                else: # s[idx] == 1 and prev == 0
                    min_val = min(dfs(idx + 1, s[idx]), dfs(idx + 1, '0') + 1)

            memo[(idx, prev)] = min_val
            return min_val

        return dfs(0, "0")


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        we should check every possibility and try to get the minimum number of flips
            - do it recursively
        
        (X) ~~brute force O(2^N) -> O(n) check if the string is monotonic~~

        we would want to call the recursion function only if the move we're going to make
        leads to the monotonic string

        if the prev is 0:
            flip, don't flip
        if the prev is 1:
            if curr is 1:
                don't flip
            if curr is 0:
                flip
        """
        memo = {}
        def dfs(idx, prev):
            if idx == len(s):
                return 0

            if (idx, prev) in memo:
                return memo[(idx, prev)]
            
            min_val = float('inf')
            if prev == '0':
                min_val = min(min_val, dfs(idx + 1, '1' if s[idx] == '0' else '0') + 1, dfs(idx + 1, s[idx]))
            else:
                if s[idx] == '1':
                    min_val = min(min_val, dfs(idx + 1, s[idx]))
                else:
                    min_val = min(min_val, dfs(idx + 1, '1' if s[idx] == '0' else '0') + 1)

            memo[(idx, prev)] = min_val
            return min_val

        return dfs(0, "0")