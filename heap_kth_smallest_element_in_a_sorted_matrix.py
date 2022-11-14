# takeaways: store the number of the next col back to the heap
# time complexity => N+Klog(N)

from ast import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) 
        
        minHeap = []
        for r in range(n):
             minHeap.append((matrix[r][0], r, 0))
                
        heapq.heapify(minHeap)
        
        num = -1
        while k:
            num, r, c = heapq.heappop(minHeap)
            
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
                
            k -=1
            
        return num
