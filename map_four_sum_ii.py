from ast import List

# brute force
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hmap = {}
        n = len(nums1)
        
        for i in range(n):
            for j in range(n):
                two_sum = nums1[i] + nums2[j]
                hmap[two_sum] = hmap.get(two_sum, 0) + 1
        
        count = 0
        for i in range(n):
            for j in range(n):
                key = (nums3[i] + nums4[j]) * -1
                if key in hmap:
                    count += hmap[key]
            
        return count