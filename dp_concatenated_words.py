from ast import List

# passing substring
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

# passing index + target
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        
        res = []
        def dfs(idx, target, count):
            if target[idx:] in words and count >= 1:
                return True
            
            for i in range(idx, len(target)):
                prefix = target[idx:i+1]
                if prefix in words:
                    if dfs(i + 1, target, count + 1):
                        return True
            
            return False
        
        for word in words:
            if dfs(0, word, 0):
                res.append(word)
        
        return res


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            
        curr.end_of_word = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # prepare trie        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(idx, target, root, count):    
            if idx == len(target):
                return count > 1
            if idx > len(target):
                return False
            
            curr = root
            for i in range(idx, len(target)):
                if target[i] not in curr.children:
                    return False

                curr = curr.children[target[i]]

                # found the element in the array that is substring of the target
                if curr.end_of_word:
                    # keep going
                    if dfs(i + 1, target, root, count + 1):
                        return True

            return False
        
        res = []
        for word in words:
            if dfs(0, word, trie.root, 0):
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