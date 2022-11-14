from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        pivot = val
        l, r = 0, len(nums) - 1
        
        while l < r:
            while l < len(nums) and nums[l] != pivot:
                l += 1
            while r > 0 and nums[r] == pivot:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        k = 0
        while k < len(nums) and nums[k] != pivot:
            k += 1
        
        return k


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
                
        return count