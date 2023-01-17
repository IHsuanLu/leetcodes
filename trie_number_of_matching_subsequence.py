# FAV
from ast import List

# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
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
        
        curr.count += 1
        curr.end_of_word = True

        
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def find_idx(child, idx):
            for i in range(idx, len(s)):
                if s[i] == child:
                    return i
            return -1

        res = [0]
        def dfs(node, idx): # (trieNode, index on the string s)
            if node.end_of_word:
                res[0] += node.count
                
            for child in node.children:
                _idx = find_idx(child, idx + 1)
                if _idx != -1:
                    dfs(node.children[child], _idx)

        dfs(trie.root, -1)
        return res[0]


# Recursive
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(w1, w2):
            m, n = len(w1), len(w2)
            if m > n:
                return False

            def dfs(i, j):
                if i == m:
                    return True
                if j == n:
                    return False

                if w1[i] == w2[j]:
                    if dfs(i + 1, j + 1):
                        return True
                else:
                    if dfs(i, j + 1):
                        return True
                
                return False

            return dfs(0, 0)

        hmap = {}
        for w in words:
            hmap[w] = hmap.get(w, 0) + 1

        res = 0
        for k in hmap:
            if is_subsequence(k, s):
                res += hmap[k]
        
        return res


# Trie - not working
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
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
        
        curr.word = word
        curr.end_of_word = True

        
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        hmap = {} # prepare trie for further use
        for word in words:
            trie.insert(word)
            hmap[word] = hmap.get(word, 0) + 1

        res = [0]
        def dfs(node, idx): # (trieNode, index on the string s)
            if node.end_of_word:
                res[0] += hmap[node.word]
            
            """
            if we traverse based on `s` and its index
            - `ja` will be counted twice in `dsahjpjauf`
                - we need to add another hash set to prevent the case be counted twice
                -> TLE
            """
            for i in range(idx, len(s)):
                if s[i] in node.children:
                    dfs(node.children[s[i]], i + 1)

        dfs(trie.root, 0)
        return res[0]
        