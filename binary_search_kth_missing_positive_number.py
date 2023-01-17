# FAV

from ast import List


class Solution:
   def findKthPositive(self, arr: List[int], k: int) -> int:
        # conduct a binary search
        """
        tear the problem down into small pieces
        - how do we know the number of missing positive integer at certain index?
            - missing_count = arr[i] - i - 1
        
        - sorted array -> binary search
            - if missing_count >= k, move right pointer
            - else move left pointer

        - what if the element does not present in the array?
            - 

        [2,3,4,7,11]; k = 5
                  r
                  l
        """
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            missing_count = arr[mid] - mid - 1
            if missing_count >= k:
                r = mid - 1
            else:
                l = mid + 1

        return l + k
