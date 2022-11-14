class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {}
        
        res = ""
        for i in range(len(s)):
            map[s[i]] = 1 + map.get(s[i], 0)
            
        for i in range(len(order)):
            if order[i] in map:
                occurance = map[order[i]]
                res += order[i] * occurance
                del map[order[i]]
        
        for key, value in map.items():
            res += key * value
            
        return res