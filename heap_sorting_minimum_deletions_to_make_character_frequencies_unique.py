# hmap + hset + sorting
import heapq


class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        
        counts = sorted(hmap.values())     
        res = 0
        hasNext = True
        while hasNext:
            hset = set(counts)
            hasNext = False
            for i in range(1, len(counts)):
                if counts[i] != 0 and counts[i] == counts[i - 1]:
                    counts[i - 1] -= 1
                    if counts[i - 1] in hset:
                        hasNext = True
                    hset.add(counts[i - 1])
                    res += 1

        return res


# priority queue
class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        
        max_heap = [val * -1 for val in hmap.values()]
        heapq.heapify(max_heap)
        
        res = 0
        while max_heap:
            next_ele = heapq.heappop(max_heap)
            
            if max_heap and max_heap[0] == next_ele:
                next_ele += 1
                if next_ele != 0:
                    heapq.heappush(max_heap, next_ele)
                
                res += 1
        
        return res
