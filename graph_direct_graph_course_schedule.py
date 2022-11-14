# equivalent to checking if there are outward edges for nodes
# solve it with DFS, firstly we can visualize the given example

# [[0,1], [0,2], [1,3], [1,4], [3,4]]
# instead of graph, we can use adjacency list 
# 
# course, prereq
# 0       [1,2]
# 1       [3]
# 2       []
# 3       [4]
# 4       []
# 
# run DFS from 0 to n-1
from ast import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create the adjacency list
        # [[0,1], [0,2], [1,3], [1,4], [3,4]]
        
        pre_map = { i:[] for i in range(numCourses) }
        for c, p in prerequisites:
            pre_map[c].append(p)
        
        visited = set()
        def dfs(curr):
            if len(pre_map[curr]) == 0:
                return True
            
            if curr in visited:
                return False
            visited.add(curr)
            
            for p in pre_map[curr]:
                if not dfs(p):
                    return False

            pre_map[curr] = [] # so that next time we check on the curr course, it will return at line 29, another way of memoize the result
            return True
        
        # reason of looping every one is the graph might not be all connected
        # 1 -> 2; 3 -> 4
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


# use two sets
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create the adjacency list
        # [[0,1], [0,2], [1,3], [1,4], [3,4]]
        
        pre_map = { i:[] for i in range(numCourses) }
        for c, p in prerequisites:
            pre_map[c].append(p)
        
        visited = set()
        cycle = set()
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visited:
                return True

            cycle.add(curr)            
            for p in pre_map[curr]:
                if not dfs(p):
                    return False
            cycle.remove(curr)
            visited.add(curr)

            return True
        
        # reason of looping every one is the graph might not be all connected
        # 1 -> 2; 3 -> 4
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
