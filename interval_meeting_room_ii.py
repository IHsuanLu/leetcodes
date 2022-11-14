from ast import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        end_times = []
        heapq.heapify(end_times)

        min_count = 0
        for i in range(len(intervals)):
            heapq.heappush(end_times, intervals[i][1])
            
            min_count = max(min_count, len(end_times))

            while i + 1 < len(intervals) and end_times and intervals[i+1][0] >= end_times[0]:
                heapq.heappop(end_times)
                    
        return min_count
