from ast import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        
        for i, o in enumerate(order):
            hmap[o] = i
        
        for i in range(len(words)):
            if i + 1 < len(words):
                
                for j in range(len(words[i])):
                    # (apple, app)
                    if j >= len(words[i + 1]): 
                        return False
                
                    if words[i][j] != words[i + 1][j]:
                        if hmap[words[i][j]] > hmap[words[i+1][j]]:
                            return False
                        # if we find the first different character and they are sorted,
                        # then there's no need to check remaining letters
                        break
                
        return True