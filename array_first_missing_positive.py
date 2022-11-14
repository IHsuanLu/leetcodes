from ast import List

# time complexity: O(n)
# space complexity: O(n), using hashset
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        memo = set(nums)
        
        for m in range(1, len(nums) + 1):
            if m in memo:
                continue
            return m
        
        return len(nums) + 1


# time complexity: O(3n)
# space complexity: O(1) -> use the input array as the extra memory

# replace every existing negative value to zero, O(n)
# see "3" in the array -> modify the nums[2] to negative as the mark that "3" existed in the array, O(n)
#   -> due to changing the value to negative as the mark, we need to use abs(nums[i]) to do the indexing
# iterate through 1...len(nums), O(n)
#   -> check if nums[(i - 1)] is negative, if yes, then the number i exists
#   -> return first non-negative number's position + 1
# if the value happen to be "0" then we update it to -(len(nums) + 1) to no affect the result 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # use the input array to mark which value has existed in the nums
        for i in range(len(nums)):
            val = abs(nums[i]) 
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
                    
        for i in range(1, len(nums) + 1):
            if nums[i - 1] < 0:
                continue
            return i
        
        return len(nums) + 1