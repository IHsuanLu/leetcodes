# times (-1) for every element to simulate the max heap 

from ast import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversed_stones = [-s for s in stones]
        heapq.heapify(reversed_stones)
        
        while len(reversed_stones) > 1:
            first = heapq.heappop(reversed_stones)
            second = heapq.heappop(reversed_stones)
            
            if second > first:
                heapq.heappush(reversed_stones, first - second)
        
         # handle no stone left cases; if there is a stone left, it will still in the first priority to pop
        heapq.heappush(reversed_stones, 0)
        return abs(heapq.heappop(reversed_stones))