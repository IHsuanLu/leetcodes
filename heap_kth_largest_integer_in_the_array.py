from ast import List
import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = []
        heapq.heapify(max_heap)
        
        for n in nums:
            heapq.heappush(max_heap, int(n) * -1)
                
        for i in range(k - 1):
            heapq.heappop(max_heap)
        
        return str(int(max_heap[0]) * -1)