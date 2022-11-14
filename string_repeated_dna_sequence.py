from ast import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hset = set()
        
        res = []
        for i in range(len(s) - 10 + 1):
            target = s[i:i+10]
            if target in hset and target not in res:
                res.append(target)
            
            hset.add(target)

        return res