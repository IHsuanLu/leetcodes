# manage two heaps, one small heap (max heap); one large heap(min heap)
# where every element in the large heap should be greater than those in the small heap
# if not, pop the first value and add to the other, check balance after the modification

# those two should be as balanced as possible (len diff <= 1)
# by default, always add element to small heap and balance if needed
import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        heapq.heapify(self.small)
        
        self.large = []
        heapq.heapify(self.large)
                

    def addNum(self, num: int) -> None:        
        heapq.heappush(self.small, -1 * num)
        
        # make sure every number in small <= every number in large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # check if balanced
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if not self.small and not self.large:
            return -1
        
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.small) < len(self.large):
            return self.large[0]
    
        return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()