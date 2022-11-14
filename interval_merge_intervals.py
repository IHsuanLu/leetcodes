from ast import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        
        res = []
        target = intervals[0]
        for i in range(1, len(intervals)):
            # check if overlap
            if target[1] < intervals[i][0]:
                res.append(target)
                target = intervals[i]
            else:
                # overlap
                target = [min(target[0], intervals[i][0]), max(target[1], intervals[i][1])]
        
        res.append(target)
        return res