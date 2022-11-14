# the question teaches us topological sort (the result order by traversing the adjaceny list)
# running dfs on every node

# same as course schedule -> create adjacency list at the very beginning
# iterate through every node
# record from the furthest to the nearest

# O(number_of_prereq + number_of_courses), O(number_of_edges, + number_of_vertices)
from ast import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # equivalent to check if there are outgoing edges for nodes
        pre_map = { c: [] for c in range(numCourses) }
        for c, pre in prerequisites:
            pre_map[c].append(pre)
        """
        {
            0: [],
            1: [0], 
            2: [0], 
            3: [1, 2]
        }
        """
        
        res = []
        visited = set() # the node we've done dfs
        cycle = set() # for detecting cycle in each dfs round
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)

            for prereq in pre_map[node]:
                # run dfs for every prereqs
                if not dfs(prereq):
                    return False
            
            cycle.remove(node) # release the node from the current dfs round

            visited.add(node)
            res.append(node)
            return True
            
        
        for i in range(numCourses):
            # run dfs for every node
            if not dfs(i):
                return []
        
        return res