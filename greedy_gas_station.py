# gas  [ 1, 2, 3, 4, 5]
# cost [ 3, 4, 5, 1, 2]
# diff [-2,-2,-2, 3, 3]
# we know that sum(gas) >= sum(cost)

# [7, 1, 0, 11, 4] 
# [5, 9, 1, 2, 5]
# [2,-8,-1,9,-1]

# GREEDY ALDORITHM => assume it's gonna work and see if it does

# why the problem is greedy?
# we need to keep track of total
#   -> if the total ever become 0, the starting index is not gonna work, so we reset total and try the next one
from ast import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        # guarantee the solution exists
        
        total = 0
        start = 0        
        # we assume the first non-negative should be the solution cause there should be the one and the only one solution
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0: # if the total ever fails, it means the starting point is incorrect since it does not accumulate enough gas.
                # reset total and try next one
                total = 0
                start = i + 1
                
        return start
        