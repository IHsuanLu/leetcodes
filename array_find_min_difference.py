from ast import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [[int(val) for val in time.split(":")] for time in timePoints]
        timePoints.sort()

        timePoints.append([timePoints[0][0] + 24, timePoints[0][1]])

        min_diff = 1440
        for i in range(1, len(timePoints)):
            hour1, min1 = timePoints[i - 1]
            hour2, min2 = timePoints[i]

            diff = ((hour2 - hour1) * 60) + (min2 - min1)
            min_diff = min(min_diff, diff)
        
        return min_diff