from ast import List

# enhancement on the way of finding predecessor -> using hash set
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        first, we need to know if a word is a predecessor of another
        and then we do top-down dp for getting the maximum length of the word chain
        """
        wordSet = set(words)

        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            
            max_val = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:] # skip a character
                if predecessor in wordSet:
                    max_val = max(max_val, dfs(predecessor) + 1)

            memo[word] = max_val
            return max_val

        res = 1
        for word in words:
            res = max(res, dfs(word))
    
        return res


# LIS style DP
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        first, we need to know if a word is a predecessor of another
        and then we do top-down dp for getting the maximum length of the word chain
        """
        words.sort(key=len)

        def is_predecessor(prev, curr):
            M, N = len(prev), len(curr)
            if N - M != 1:
                return False

            i = j = 0
            mismatched_found = False
            while i < M:
                if prev[i] == curr[j]:
                    j += 1
                    i += 1
                else:
                    if mismatched_found:
                        return False
                    mismatched_found = True
                    j += 1

            return True
        
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            if idx == len(words):
                return 1
            
            max_val = 1
            for i in range(idx, len(words)):
                if i + 1 < len(words) and is_predecessor(words[idx], words[i + 1]):
                    max_val = max(max_val, dfs(i + 1) + 1)
            
            memo[idx] = max_val
            return max_val

        res = 1
        for i in range(len(words)):
            res = max(res, dfs(i))
    
        return res
