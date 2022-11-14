from ast import List

"""
Time complexity: O(t⋅n). The memo array of size O(t⋅n) has been filled just once. Here, t refers to the sum of the nums array and nn refers to the length of the nums array.
Space complexity: O(t⋅n). The depth of recursion tree can go up to n. The memo array contains t⋅n elements.

# https://stackoverflow.com/questions/53143539/how-does-complexity-get-reduced-to-on2-from-o2n-in-case-of-memoization
"""

"""
- The core is to find the sub-problem and the base case.
    - The initial problem is: at index 0, for target sum = target, how many possible ways can we find? In the beginning, for an array nums, we can generate 2 cases: either multiply nums[0] by 1 or -1.
    - Then, we come to a sub-problem: at index 1, for target sum = target-nums[0] (if 1 is the multiplier) or target+nums[0] (if -1 is the multiplier), how many possible ways can we find?
    - So, the recursive DFS should return the number of different expressions that can be built at a certain index with a certain target.
- The base case is when the index comes to the end of the array. If the current target is 0, that means we find a valid expression, so count = 1; otherwise, this outcome is not valid, count = 0. Before coming to the base case, the count of valid expressions for the current problem is the sum of the results of its two sub-problems.
- We use a hashmap to store the current answers at each index, whose keys store (index, target) and values store the count of feasible solutions for nums[index+1:] with target sum = target.
- In the dfs function, to avoid duplicates, we take actions only when the current index and target have not been added to our hashmap, otherwise, we simply return hashmap[(index, target)]. If (index, target) is not in the hashmap, we get the value of count and update the hashmap by hashmap[(index, target)] = count.
"""

# Top-down memoization 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(idx, curr_sum, memo):
            if idx >= len(nums):
                return 1 if curr_sum == 0 else 0
            
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]
            
            count = 0
            
            # we don't need for loop, for the following two recursive calls
            # have already covered all the conditions (pos / neg)
            count += dfs(idx + 1, curr_sum + nums[idx], memo)
            count += dfs(idx + 1, curr_sum - nums[idx], memo)
            
            memo[(idx, curr_sum)] = count

            return count
    
        return dfs(0, target, {})