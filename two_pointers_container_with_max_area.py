from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        current_max = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            current_max = max(current_max, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return current_max