# Can we chopped off some prefixes of the array, such that we can make that sum equals to "k"?
    # we can if we maintain a prefix_map, which stores the count of the particular prefix that has occured

# We need to build up the prefix_map simulataneously while doing iteration, cause we do not want the smalluer subarray subtracting the prefix sum from the larger arrays

# sliding window does not work cause the element in the array might be negative
#   -> adding an element does not guarantee the increase in the sum, and vice versa

# O(n^2) -> O(n), think of the brute force way, and optimize it later on
# using hash map
#   key -> the prefix sum
#   value -> count of the particular prefix has occured

# prefix sum
# nested for loop
# at the certain point, we minus the prefix sum to reduce the repetitive works

# example

# prefix_map {the prefix sum:  count of the particular prefix has occured}
# {
#   0: 2,
#   1: 2,
#   2: 1,
#   3: 1,
#   4: 1
# }


# [1, -1, 1, 1, 1, 1], k = 3
# sum = 1
# res = 


# [1, -1, 1, 1, 1, 1], k = 3
# sum = 1 - 3 = -2 -> do we have "-2" in our prefix_map? No. / we add "1" to the prefix_map
# res = 

# [1, -1, 1, 1, 1, 1], k = 3
# sum = (1 + -1) - 3 = -3 -> do we have "-3" in our prefix_map so that we can subtract the prefix and make the sum equals to k? No. / we increase the value count of "0" in prefix sum
# res = 

# [1, -1, 1, 1, 1, 1], k = 3
# sum = (1 + -1 + 1) - 3 = -2 -> do we have "-2" in our prefix_map so that we can subtract the prefix and make the sum equals to k? No. / we increase the value count of "1" in prefix sum
# res = 

# [1, -1, 1, 1, 1, 1], k = 3
# sum = (1 + -1 + 1 + 1) - 3 = -1 -> do we have "-1" in our prefix_map so that we can subtract the prefix and make the sum equals to k? No. / we add "2" to the prefix_map
# res = 

# [1, -1, 1, 1, 1, 1], k = 3
# sum = (1 + -1 + 1 + 1 + 1) - 3 = 0 -> do we have "0" in our prefix_map so that we can subtract the prefix and make the sum equals to k? Yes. / we see the value of key "0" is 2 -> we have 2 ways to form a subarray with sum of all the elements as "k" -> take the "res" and increment it by 2 /
#                                    -> we add "3" to the prefix_map
# res = 2

# [1, -1, 1, 1, 1, 1], k = 3
# sum = (1 + -1 + 1 + 1 + 1 + 1) - 3 = 1 -> do we have "1" in our prefix_map so that we can subtract the prefix and make the sum equals to k? Yes. / we see the value of key "1" is 2 -> we have 2 ways to form a subarray with sum of all the elements as "k" -> take the "res" and increment it by 2 /
#                                        -> we add "4" to the prefix_map
# res = 2 + 2 = 4
from ast import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_map = {0: 1} # key: prefix_sum of array; val: count of occurence
        
        
        # iterate thru the nums array
        
        curr_sum = 0
        # update the curr_cum so far
        
        # check the diff of the curr_sum and k exists in the prefix_map
        #   if yes, there is subarray that we can dump to get value k
        #       update the res
        #.  update the prefix_map with curr_sum
        
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            
            if diff in prefix_map:
                res += prefix_map[diff]
                
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        
        return res