from ast import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        min_crosses = len(wall)
        hmap = defaultdict(int)
        
        round = 1
        curr_crosses = 0
        length = sum(wall[0]) - 1
        while round <= length:
            for i, row in enumerate(wall):
                curr_cross = row[hmap[i]]
                if curr_cross != round:
                    curr_crosses += 1
                else:
                    hmap[i] += 1

            print(min_crosses)
            round += 1
            min_crosses = min(min_crosses, curr_crosses)
            curr_crosses = 0
        
        return min_crosses