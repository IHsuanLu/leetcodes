from ast import List
from collections import deque
from string import ascii_lowercase

# make enhancement to the efficiency of getting neighbors

# time limited excceeded, passes 34/50
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def get_diff(w1, w2) -> int:
            diffCount = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diffCount += 1
            return diffCount
    
        def get_neighbors(curr_word):
            neighbors = []
            for word in wordList:
                if get_diff(curr_word, word) == 1:
                    neighbors.append(word)
                    
            return neighbors
        
        res = 0
        visited = set()
        queue = deque([beginWord])
        while len(queue) > 0:
            res += 1
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                visited.add(nxt)
                
                if nxt == endWord:
                    return res
                
                neighbors = get_neighbors(nxt)
                for child in neighbors:
                    queue.append(child)
        
        return 0



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        def get_neighbors(curr_word):
            for i in range(len(curr_word)):
                for c in ascii_lowercase:
                    # generate every possible combination via iterating thru ascii_lowercase and create according new string
                    newStr = curr_word[:i] + c + curr_word[i+1:]
                    if newStr in wordSet:
                        yield newStr
        
        res = 0
        visited = set()
        queue = deque([beginWord])
        while len(queue) > 0:
            res += 1
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                visited.add(nxt)
                
                if nxt == endWord:
                    return res
                
                neighbors = get_neighbors(nxt)
                for child in neighbors:
                    queue.append(child)
        
        return 0
                    