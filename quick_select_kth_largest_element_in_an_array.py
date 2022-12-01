# pretty much the same as quick sort, set pivot and compare, swap with other elements in the array
# average O(n) [n + n/2 + n/4 ... = 2n]; worse case O(n^2) [every time the pivot we select is the largest -> we only eliminate one element per recursion ]
# quick sort is O(nlogn), and quick select is O(n) -> in quick select we only need to deal with the side we are interested in (the solution potentially lies in recursively)
from ast import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find the kth largest element at the index `len(nums) - k` after going thru quick select   
        k = len(nums) - k
        
        # left, right keep track of which portion of array we're running quick select on
        def quick_select(l, r):
            pivot, p = nums[r], l
            
            # iterate thru the entire array except for the last element
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p] # swap pivot with the p

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]
        
        return quick_select(0, len(nums) - 1)