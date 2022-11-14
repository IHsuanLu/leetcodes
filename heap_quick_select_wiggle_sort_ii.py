from ast import List
import heapq
import random

# time: O(n), space: O(1)
# concept: we find median value, put numbers bigger than median into odd index, smaller than median into even index.


# Naive solution:

# 1. Sort the array to find median in O(nlgn) time + O(1) space
# 2. Move odd and even index numbers into temp array and move them back to the original array with new index. Taking O(n) time + O(n) space.
# Total: O(nlgn) time + O(n) space


# In order to achieve O(n) time + O(1) space, we need to answer two questions:

# 1. How to find median in O(n)+O(1)
# 2. How to re-order the odd-even indexes "in-place" using O(1) memory.


# key thought:
# 1. Quick select to find median in O(n) time on average, O(n^2) in worst case. Taking O(1) memory.
# 2. "Median of medians" alogrithm to improve quick select, making the time complexity "deterministic O(n)" rather than "average O(n)".
# 3. `Virtual indexing` achieve in-place wiggle sort based on median value found above.

# Virtual indexing:
# This is actually a "Three color Sort" problem. Imagine scanning the nums this way: "1,3,5,7,9, ... 0,2,4,6,8,10...". During the scan, when you see a big number, put it to "left", a small number, put it to "right", in the end, you will see all big numbers on left, all small numbers on right, and all median numbers in the middle.
# But wait, here "left" and "right" are actually the left and right of "1,3,5,7...0,2,4,6,8,..." indexes, not the left and right of "0,1,2,3,4,5...", because you are scanning in "1,3,5,7...0,2,4,6,8,..." order. So what you actually see is all big numbers on odd index, all small numbers on even index, all median numbers distributed on the left and right side of the array. And this kind of distribution is guaranteed to be wiggled sorted.


class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        def quick_select_n_smallest(n):
            start, end = 0, len(nums) - 1
            while True:
                pivot = nums[random.randint(start, end)]
                l, r = start, end
                p = start
                while p <= r:
                    if nums[p] > pivot: # swap to the back
                        nums[p], nums[r] = nums[r], nums[p]
                        r -= 1
                    elif nums[p] < pivot:
                        nums[p], nums[l] = nums[l], nums[p]
                        l += 1
                        p += 1
                    else:
                        p += 1
                
                n_idx = n - 1
                if l <= n_idx <= r:
                    return pivot
                elif n_idx < l:
                    end = r - 1
                else:
                    start = l + 1
        
        quick_select_n_smallest(len(nums) // 2)
    
        half = (len(nums)+1) // 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


# time: O(nlogn), space: O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_heap = [n * -1 for n in nums]
        heapq.heapify(max_heap)
        
        for i in range(1, len(nums), 2):
            nums[i] = heapq.heappop(max_heap) * -1
        
        for i in range(0, len(nums), 2):
            nums[i] = heapq.heappop(max_heap) * -1