from ast import List
import collections

# conclusion
# * 1. Tree has n-1 edges
# * 2. Disjoint Set can detect if there is cycle in graph
# * 3. Graph with less than n-1 edges is definitely not connected
# * 4. Graph with more than n-1 edges definitely has cycle (undirected graph only)

# graph theory
# For the graph to be a valid tree, it must have exactly `n - 1` edges. 
# Any less, and it can't possibly be fully connected.
# Any more, and it has to contain cycles.
# Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!

# Check whether or not there are n - 1 edges. If there's not, then return false.
# Check whether or not the graph is fully connected. Return true if it is, false if otherwise.

# Checking whether or not a graph is fully connected is straightforward — we simply checked if all nodes were reachable from a search starting at a single node.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacent = collections.defaultdict(list)
        for p, c in edges:
            adjacent[p].append(c)
            adjacent[c].append(p)
        
        queue = collections.deque([0])
        visited = set([0])
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                for child in adjacent[nxt]:
                    if child in visited:
                        continue
                    visited.add(child)
                    queue.append(child)
        
        # if the graph is fully connected, then the count of the set visited should align with `n``
        return len(visited) == n

# dfs (recursive)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacent = collections.defaultdict(list)
        for p, c in edges:
            adjacent[p].append(c)
            adjacent[c].append(p)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for child in adjacent[node]:
                dfs(child)
        
        dfs(0)
        return len(visited) == n


# Union Find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        # from 0 to n, though we don't need `0`, we align the value and indice`
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1) # keep height of the tree as low as possible
        
        def find(node):
            parent = parents[node]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]] 
                parent = parents[parent]
            
            return parent
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                # already in the same disjoint set
                return False

            rank1, rank2 = rank[root1], rank[root2]
            
            if rank1 >= rank2:
                # merge root2 to root1
                parents[root2] = root1
                rank[root1] += 1
            else:
                # merge root1 to root2
                parents[root1] = root2
                rank[root2] += 1
            
            return True
        
        for u, v in edges:
            if not union(u,v):
                return False
            
        return True


# wrong answer, mis-consider the two-graph scenarios
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        
        if len(edges) < n - 1:
            return False

        adjacnent = collections.defaultdict(list)
        min_key = float('inf')
        for p, c in edges:
            if p <= c:
                adjacnent[p].append(c)
            else:
                adjacnent[c].append(p)
            min_key = min(min_key, p, c)

        queue = collections.deque([min_key])
        visited = set()
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    return False
                visited.add(nxt)
                
                for child in adjacnent[nxt]:
                    queue.append(child)
                
                del adjacnent[nxt]
        
        return not bool(adjacnent)