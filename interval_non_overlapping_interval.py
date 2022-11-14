# sort the intervals list
# check if overlap
# keep the one end first if overlapping occur   
from ast import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        
        target = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= target[1]:
                # not overlapped
                target = intervals[i]
            else:
                # overlapped
                res += 1
                target = [target[0], min(target[1], intervals[i][1])]
        
        return res
