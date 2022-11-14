from ast import List
from collections import Counter


class Solution:
    def findAnagrams(self, p: str, q: str) -> List[int]:
        res = []
        qCounter = Counter(q)
        pCounter = Counter(p[:len(q)-1])
        
        for i in range(len(q) - 1 ,len(p)):
            pCounter[p[i]] += 1   # include a new char in the window
            j = i - len(q) + 1 # adjusted indice based on i and len(q), which then starts from 0
            
            if pCounter == qCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(j)   # append the starting index
            
            pCounter[p[j]] -= 1   # decrease the count of oldest char in the window
            
            if pCounter[p[j]] == 0:
                del pCounter[p[j]]   # remove the count if it is 0 (so that the set equility may pass)

        return res