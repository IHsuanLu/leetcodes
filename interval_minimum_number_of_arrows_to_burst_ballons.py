# FAV
from ast import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda it: it[1])
        res = 1
        max_end = points[0][1]
        for i in range(1, len(points)):
            t_s, t_e = points[i]
            if t_s > max_end:
                max_end = t_e
                res += 1

        return res

# Not Working 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        compare init node's end with the following intervals start.
            -> if the followings' start <= init node's end 
                -> we can pop them together
        """
        points.sort()
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 1 if points[1][0] <= points[0][1] else 2

        min_arrow_count = 0
        max_end = points[0][1]
        i = 1
        N = len(points)
        while i < N:                
            while i + 1 < N and points[i + 1][0] <= max_end:
                max_end = min(max_end, points[i + 1][1])
                i += 1
            min_arrow_count += 1
            i += 1
            if i < N:
                if i == len(points) - 1 and points[i][0] > points[i - 1][1]:
                    min_arrow_count += 1
                max_end = points[i][1]

        return min_arrow_count


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        compare init node's end with the following intervals start.
            -> if the followings' start <= init node's end 
                -> we can pop them together
        """
        points.sort()

        min_arrow_count = 0
        i = 0
        N = len(points)
        while i < N:
            t_start, t_end = points[i]
            while i + 1 < N and points[i + 1][0] <= t_end:
                i += 1
            min_arrow_count += 1
            i += 1

        return min_arrow_count