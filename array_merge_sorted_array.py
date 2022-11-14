from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = m - 1, len(nums2) - 1
        tail = len(nums1) - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] >= nums2[l2]:
                nums1[tail] = nums1[l1]
                l1 -= 1
            else:
                nums1[tail] = nums2[l2]
                l2 -= 1
            
            tail -= 1
            
        while l1 >= 0:
            nums1[tail] = nums1[l1]
            l1 -= 1
            tail -= 1
        
        while l2 >= 0:
            nums1[tail] = nums2[l2]
            l2 -= 1
            tail -= 1 
        