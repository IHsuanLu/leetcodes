from ast import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_ptr = max(weights)
        max_ptr = sum(weights)
        boundary_index = max_ptr
        while min_ptr <= max_ptr:
            midpoint = (min_ptr + max_ptr) // 2
            if self.feasible(weights, midpoint, days):
                boundary_index = midpoint
                max_ptr = midpoint - 1
            else:
                min_ptr = midpoint + 1
        return boundary_index
        
    
    def feasible(self, weights: List[int], max_weight: int, days: int) -> bool:
        req_days = 1
        capacity = max_weight
        i = 0
        n = len(weights)
        while i < n:
            if weights[i] <= capacity:
                capacity -= weights[i]
                i += 1
            else:
                req_days += 1
                capacity = max_weight
        return req_days <= days