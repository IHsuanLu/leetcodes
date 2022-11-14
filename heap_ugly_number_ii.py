import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, 1)
        
        ugly = set([1])
        curr = 1
        while n > 0:
            curr = heapq.heappop(min_heap)
            n -= 1
            for prime in [2,3,5]:
                new_ugly_num = prime * curr
                if new_ugly_num not in ugly:
                    ugly.add(new_ugly_num)
                    heapq.heappush(min_heap, new_ugly_num)
        
        return curr