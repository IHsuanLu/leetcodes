# loop through the given intervals and find the insertion point
# overlap -> neither goes before nor after -> need to merge, min(starting_points), max(ending_points) => check if overlap the next one before adding to the soultion list
from ast import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # check if overlap
            if newInterval[1] < intervals[i][0]:
                # new interval goes before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # new interval goes after
                res.append(intervals[i])
            else:
                # overlapping case
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
        return res
                