class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {}
        
        for c in text:
            hmap[c] = hmap.get(c, 0) + 1
        
        res = 0
        while True:
            for tc in "balloon":
                if tc in hmap and hmap[tc] > 0:
                    hmap[tc] -= 1
                else:
                    return res
            res += 1        