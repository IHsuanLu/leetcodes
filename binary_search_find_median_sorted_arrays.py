from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 #A
            j = half - i - 2 #B, subtract 2 for converting into index
            
            a_left = A[i] if i >= 0 else float('-inf')
            a_right = A[i + 1] if i+1 < len(A) else float('inf')
            b_left = B[j] if j >= 0 else float('-inf')
            b_right = B[j + 1] if j+1 < len(B) else float('inf')
            
            # correct partitioning
            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                
                return min(a_right, b_right)

            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1