from ast import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        
        def dfs(target, count):
            # set the condition `count >= 1`, since we are checking the suffix directly in the base case
            if target in words and count >= 1: 
                return True
            
            # instead of searching the word in the words list
            # for word in words:
            #     word_length = len(word)
            #     if idx + word_length <= len(target) and target[idx: idx + word_length] == word:
            #         dfs(idx + word_length, target, count + 1)
                    
            # we can check if any target's partition lies in the words `set`
            for i in range(len(target)):
                prefix = target[:i]
                if prefix in words:
                    if dfs(target[i:], count + 1):
                        return True
                    
            return False

        for word in words:
            if dfs(word, 0):
                res.append(word)
            
        return res


# TLE (not accepted)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        
        def dfs(idx, target, count):
            if idx == len(target) and count > 1:
                if target not in res:
                    res.append(target)
                return
            
            for word in words:
                word_length = len(word)
                if idx + word_length <= len(target) and target[idx: idx + word_length] == word:
                    dfs(idx + word_length, target, count + 1)

        for word in words:
            dfs(0, word, 0)
            
        return res