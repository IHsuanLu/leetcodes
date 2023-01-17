# FAV
from ast import List
import collections

# DFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(manager)):
            adjacents[manager[i]].append(i)

        def dfs(node, acc):
            if not adjacents[node]:
                return acc
            
            max_val = 0
            for subordinate in adjacents[node]:
                max_val = max(max_val, dfs(subordinate, acc + informTime[subordinate]))
            
            return max_val
        
        return dfs(headID, informTime[headID])


# DFS. accumulate result from the bottom
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(manager)):
            adjacents[manager[i]].append(i)

        def dfs(node):
            if not adjacents[node]:
                return 0
            
            max_val = 0
            for subordinate in adjacents[node]:
                max_val = max(max_val, dfs(subordinate) + informTime[subordinate])
            
            return max_val
        
        return dfs(headID) + informTime[headID]


# BFS. Accumulate the time consumed along the way from parent to childrens
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                adjacents[manager[i]].append(i)

        res = 0
        queue = collections.deque([(headID, informTime[headID])])
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt, nxt_time = queue.popleft()
                res = max(res, nxt_time)
                for subordinate in adjacents[nxt]:
                    queue.append((subordinate, nxt_time + informTime[subordinate]))
    
        return res


# Not working -> find the max value of the level does not necessarily get us to the solution
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                adjacents[manager[i]].append(i)

        res = 0
        queue = collections.deque([headID])
        while len(queue) > 0:
            max_val = 0
            for _ in range(len(queue)):
                nxt = queue.popleft()
                max_val = max(max_val, informTime[nxt])
                for subordinate in adjacents[nxt]:
                    queue.append(subordinate)
            
            res += max_val
            
        return res
