# non-sorted array, O(n) to retrieve
# sorted array, O(logn) to retrieve but O(n) to insert
# heap, O(logn) to insert and retrieve
# use "min heap of size k" cause we are never gonna remove element, use while loop to do so
#   -> kth largest => smallest
from ast import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        
        heapq.heapify(self.min_heap) # O(n)
        
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        # add and pop, the heap will handle the kth for us
        heapq.heappush(self.min_heap, val) 
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)