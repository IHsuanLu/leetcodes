# FAV

from ast import List
import collections
import heapq

"""
- instead of making the iteration go on by adding `curr_time` by 1 in each round,
we can run the loop on the basis of the existing keys of the sorted `hmap` and handle the `cpu_idle` time gracefully
using `max(et, last_cpu_idle_time) + pt`

- make sure to clean up the heap since we stop the loop after enqueueing every tasks, which means
there might be tasks that are not processed yet.
"""

# Pass (heap + sorted array)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks): #(et, pt, idx)
            task.append(i)

        tasks.sort(key=lambda it: it[0])
        
        idx, curr_time = 0, tasks[0][0]
        available_tasks, res = [], []
        heapq.heapify(available_tasks)

        while available_tasks or idx < len(tasks):
            # enqueue
            while idx < len(tasks) and tasks[idx][0] <= curr_time:
                heapq.heappush(available_tasks, [tasks[idx][1], tasks[idx][2]])
                idx += 1

            # process
            if available_tasks:
                pt, _idx = heapq.heappop(available_tasks)
                curr_time += pt
                res.append(_idx)
            else:
                # forward the time to the startiing point of the next task
                curr_time = tasks[idx][0]

        return res


# Pass (heap + sorted hash map)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        hmap = collections.defaultdict(list)
        for i, (enqueue, process) in enumerate(tasks):
            hmap[enqueue].append((process, i, enqueue))

        last_cpu_idle_time = 0
        available_tasks, res = [], []
        heapq.heapify(available_tasks) # min_heap (processing_time, idx, enqueue_time)

        for i in sorted(hmap):
            while available_tasks and last_cpu_idle_time < i:
                pt, idx, et = heapq.heappop(available_tasks)
                # get a larger value between `et` and `last_cpu_idle_time` to handle the mis-alignment
                last_cpu_idle_time = max(et, last_cpu_idle_time) + pt
                res.append(idx)
            for pt, idx, et in hmap[i]:
                heapq.heappush(available_tasks, (pt, idx, et)) 
        
        # clean up the rest pending tasks
        while available_tasks:
            res.append(heapq.heappop(available_tasks)[1])

        return res

# TLE
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        hmap = collections.defaultdict(list)
        for i, (enqueue, processing) in enumerate(tasks):
            hmap[enqueue].append((processing, i))

        curr_time = 0
        next_avail_time = 0
        
        available_tasks = []
        heapq.heapify(available_tasks) # min_heap (processing_time, idx)
        res = []
        while len(res) != len(tasks):
            # enqueue
            if curr_time in hmap:
                for i in range(len(hmap[curr_time])):
                    heapq.heappush(available_tasks, hmap[curr_time][i])            

            # process
            if curr_time >= next_avail_time and available_tasks:
                processing_time, idx = heapq.heappop(available_tasks)
                next_avail_time = curr_time + processing_time
                res.append(idx)

            curr_time += 1

        return res