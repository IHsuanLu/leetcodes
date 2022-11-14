import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        heapq.heapify(max_heap)
        if a != 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        res = []
        
        while max_heap:
            first_count, first_char = heapq.heappop(max_heap)
            if len(res) >= 2 and res[-2] == res[-1] == first_char:
                if len(max_heap) == 0:
                    return "".join(res)
                
                second_count, second_char = heapq.heappop(max_heap)
                res.append(second_char)
                second_count += 1
                
                if second_count != 0:
                    heapq.heappush(max_heap, (second_count, second_char))

                heapq.heappush(max_heap, (first_count, first_char))
                continue
            
            res.append(first_char)
            first_count += 1
            
            if first_count != 0:
                heapq.heappush(max_heap, (first_count, first_char))
        
        return "".join(res)
            