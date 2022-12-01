from ast import List

# O(n) -> hash map
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = {}
        
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        
        max_val = 0
        for key in hmap:
            if (key + 1) in hmap:
                max_val = max(max_val, hmap[key] + hmap[key + 1])
            
            if (key - 1) in hmap:
                max_val = max(max_val, hmap[key] + hmap[key - 1])
            
        return max_val



# O(nlogn) -> sorting + sliding windows
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        max_val = 0
        curr_max = 0
        l = r = 0
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff == 0:
                r += 1
            elif diff == 1:
                curr_max = r - l + 1
                r += 1
            elif diff > 1:
                curr_max = 0
                l += 1
            
            max_val = max(max_val, curr_max)
            
        return max_val