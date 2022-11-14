from ast import List
import heapq

# O(n + klogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reverse_nums = [-n for n in nums]
        heapq.heapify(reverse_nums)
        
        res = 0
        for _ in range(k):
            res = - heapq.heappop(reverse_nums)
        
        return res