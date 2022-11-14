# think how much water could we trap in every index
#   -> min(min(L, R) - h[i], 0); L = max height on the left; R = max height on the right

# space O(n)
# input                    => [0,1,0,2,1,0,1,3,2,1,2,1]
# max_left                 => [0,0,1,1,2,2,2,2,3,3,3,3]
# max_right                => [3,3,3,3,3,3,3,2,2,2,1,0]
# min(L,R)                 => [0,0,1,1,2,2,2,2,2,2,1,0]
# max(min(L, R) - h[i], 0) => [0,0,1,0,1,2,1,0,0,1,0,0] => output = 6 

# space O(1), two pointers
#           0 0 1 0 1 2 1 0 0 1 0 0 => output = 6 
#           L L L L L L L L R R R R
#           L                     R
# input => [0,1,0,2,1,0,1,3,2,1,2,1]
# max_left = 0
# max_right = 1

# when and which to shift?
#   -> shift the one with the smaller maximum value
#   -> according to above, we want to know min(L, R)
#       -> if we shift smaller maximum value (e.g. shift L due to L < R), then min(L, R) should be L directly 
#       -> if two maximum values are equal, then we shift either one cause no difference 

from ast import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += max(left_max - height[l], 0)
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += max(right_max - height[r], 0)

        return res