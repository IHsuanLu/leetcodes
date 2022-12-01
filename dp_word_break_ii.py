from ast import List

# Top-down -> DFS + Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(idx, path, memo):
            if idx == len(s):
                res.append(" ".join(path[:]))
                return
            
            if idx in memo:
                return memo[idx]
            
            for word in wordDict:
                word_length = len(word)
                if idx + word_length <= len(s) and s[idx: idx + word_length] == word:
                    path.append(word)
                    memo[idx] = path
                    
                    dfs(idx + word_length, path, memo)
                    path.pop()
                    del memo[idx]
        
        dfs(0, [], {})
        return res