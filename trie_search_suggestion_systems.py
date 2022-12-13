from ast import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr.words.append(word)
            curr = curr.children[char]

        # append the word to the last node
        curr.words.append(word)

    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        
        return curr.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        res = []
        for i in range(len(searchWord)):
            search_rlt = trie.search(searchWord[:i+1])
            search_rlt.sort()
            
            res.append(search_rlt[:3])

        return res