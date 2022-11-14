from ast import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # maintain a hash map to store <sum % k, index>
        prefix_sum_map = {}

        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            key = curr_sum % k
            
            if key == 0 and i > 0:
                return True
            
            if key in prefix_sum_map and i - prefix_sum_map[key] > 1:
                return True
            
            #  If say we have two occurrences of a particular sum, then we need the one is farther away from the next occurrence to ensure that we get a subarray of atleast 2 elements, that is why when we're getting the occurrence again we aren't adding the new index where we see that so we can get a larger subarray as required in the question.
            if key not in prefix_sum_map:
                prefix_sum_map[key] = i
            
        return False
            