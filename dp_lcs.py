from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if both match, find the diagonal cell and add 1
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # find the larger value from either right or bottom
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]


# Recursive, memoize the duplicated result
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(idx1, idx2, memo):
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if text1[idx1] == text2[idx2]:
                return dfs(idx1 + 1, idx2 + 1, memo) + 1
            
            # shift text1 and text2 to another index
            res_case_1 = dfs(idx1 + 1, idx2, memo)
            res_case_2 = dfs(idx1, idx2 + 1, memo)
            
            memo[(idx1, idx2)] = max(res_case_1, res_case_2)
            return max(res_case_1, res_case_2)
        
        return dfs(0,0, {})


# Recursive, memoize the duplicated function calls
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @lru_cache(maxsize=None) is the built-in function of python to memoize the funtion
        @lru_cache(maxsize=None)
        def dfs(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            if text1[idx1] == text2[idx2]:
                return dfs(idx1 + 1, idx2 + 1) + 1
            
            res_case_1 = dfs(idx1 + 1, idx2)
            res_case_2 = dfs(idx1, idx2 + 1)
            
            return max(res_case_1, res_case_2)
        
        return dfs(0,0, {})