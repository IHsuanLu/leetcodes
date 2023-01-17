# FAV

from ast import List
from functools import lru_cache


# backtracking, -> brute force
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        we are gonna use backtracking to enumerate every possbility, since we don't know which bracket to use or not
            -> so for every bracket, we can either include it into our solutions or not
        """
        min_invalid_count = [len(s)]
        self.res = set()
        
        @lru_cache(maxsize=None)
        def dfs(idx, left_count, invalid_count, path):
            if idx == len(s) or left_count < 0:
                if left_count == 0: # valid case
                    if min_invalid_count[0] > invalid_count:
                        min_invalid_count[0] = invalid_count
                        self.res = set({ path[:] })
                    elif min_invalid_count[0] == invalid_count:
                        self.res.add(path[:])
                return

            if s[idx] == '(':
                dfs(idx + 1, left_count + 1, invalid_count, path + "(") # include
                dfs(idx + 1, left_count, invalid_count + 1, path) # don't include
            elif s[idx] == ")":
                dfs(idx + 1, left_count - 1, invalid_count, path + ")") # include
                dfs(idx + 1, left_count, invalid_count + 1, path) # don't include
            else:
                dfs(idx + 1, left_count, invalid_count, path + s[idx]) # include and skip

        dfs(0, 0, 0, "")
        return self.res