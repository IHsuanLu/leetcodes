from ast import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
    
        def dfs(idx, curr):
            if idx >= len(s):
                res.append(curr.copy())
                return
            
            for i in range(idx, len(s)): # get every possible substring
                word = s[idx: i + 1]
                if word == word[::-1]: # only proceed if we get parlindrome
                    curr.append(word)
                    dfs(i + 1, curr) # start from the next index
                    curr.pop() # clear the array
        
        dfs(0, [])
        return res