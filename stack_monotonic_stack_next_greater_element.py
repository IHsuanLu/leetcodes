from ast import List

# O(n^2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        nums_idx_map = { n: i for i, n in enumerate(nums1) }
        for i, n2 in enumerate(nums2):
            if n2 not in nums1:
                continue
            
            for j in range(i, len(nums2)):
                if nums2[j] > n2:
                    num1_idx = nums_idx_map[n2]
                    res[num1_idx] = nums2[j]
                    break
        
        return res

# O(m+n), monotonic stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}
        for n2 in nums2:
            while stack and stack[-1] < n2:
                last_ele = stack.pop()
                hmap[last_ele] = n2
    
            stack.append(n2)

        res = [-1] * len(nums1)
        for i, n1 in enumerate(nums1):
            if n1 in hmap:
                res[i] = hmap[n1]

        return res