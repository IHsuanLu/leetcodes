from ast import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        
        for i, (x, y) in enumerate(points):
            pow_distance = pow(x,2) + pow(y,2)
            heapq.heappush(distances, (pow_distance, i))
        
        res = []
        for i in range(k):
            _, idx = heapq.heappop(distances)
            res.append(points[idx])
            
        return res
