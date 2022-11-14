from ast import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        
        for s in strings:
            if len(s) == 1:
                hmap[(0)].append(s)
                continue

            key = []
            for i in range(1, len(s)):
                key.append((ord(s[i]) - ord(s[i - 1]))%26) # %26 for handling the circular cases
            
            hmap[tuple(key)].append(s)
                
        return hmap.values()