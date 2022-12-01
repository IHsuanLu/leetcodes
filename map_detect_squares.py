from ast import List


class DetectSquares:

    def __init__(self):
        self.hmap = {}

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.hmap[key] = self.hmap.get(key, 0) + 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        
        # find the diagonal point first
        # (x1, y3) and (x3, y1) should be p2 and p4
        for (x3, y3), count in self.hmap.items():
            if abs(x1 - x3) != 0 and abs(x1 - x3) == abs(y1 - y3):
                p2, p4 = (x1, y3), (x3, y1)
                res += count * self.hmap.get(p2, 0) * self.hmap.get(p4, 0)
                
        return res
        