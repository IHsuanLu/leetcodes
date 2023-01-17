from ast import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hmap = {}
        for t in tasks:
            hmap[t] = hmap.get(t, 0) + 1

        res = 0
        for k, v in hmap.items():
            if v == 1:
                return -1
            
            res += math.ceil(v/3)
            
        return res