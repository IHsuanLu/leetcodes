from ast import List

# missing 
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # define a function counting the missing number until x
        # use binary search to check on candidates
        def missing_counts(idx):
            return nums[idx] - nums[0] - idx
        
        if missing_counts(len(nums) - 1) < k:
            count = missing_counts(len(nums) - 1)
            return nums[-1] + (k - count)
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            count = missing_counts(mid)
            if count < k:
                l = mid + 1
            else:
                r = mid
        
        return nums[l - 1] + (k - missing_counts(l - 1))


# time limited exceeded
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # define a function counting the missing number until x
        # use binary search to check on candidates
        def missing_counts(n):
            start, end = nums[0], nums[-1]
            
            count = 0
            for num in range(start + 1, n + 1):
                if num not in nums:
                    count += 1
            
            return count

        if missing_counts(nums[-1]) < k:
            count = missing_counts(nums[-1])
            return nums[-1] + (k - count)
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            count = missing_counts(nums[mid])
            if count < k:
                l = mid + 1
            else:
                r = mid
        
        return nums[l - 1] + (k - missing_counts(nums[l - 1]))
