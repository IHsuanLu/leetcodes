from ast import List

# 1　　2　　7　　4　　3　　1   find 2 -> first element which is smaller that next element 
# 1　　2　　7　　4　　3　　1   find 3 -> smallest emlement which is larget that 2
# 1　　3　　7　　4　　2　　1   swap 2 and 3
# 1　　3　　[1　　2　　4　　7]   sort nums after 3

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # send the i pointer to the position where descending order starts
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # nums are entirely in a descending order
        if i == 0:
            nums.reverse()
            return 
        
        # find the last "ascending" position
        k = i - 1    
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  

        # reverse the k+1 to the end
        l, r = k + 1, len(nums) - 1  
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1
