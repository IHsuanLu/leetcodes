from ast import List
import collections

# Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # every single node is it's own parent
        parents = [i for i in range(n)]

        # keep track of the rank cause we would always want to merge the small one to the large one
        rank = [1] * (n)
        
        # find the given node's parent
        # if the two nodes happen to have the same result calling `find`, which means they have already been connected
        def find(node):
            parent = parents[node]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False
            
            rank1, rank2 = rank[root1], rank[root2]
            if rank1 >= rank2:
                parents[root2] = root1
                rank[root1] += 1
            else:
                parents[root1] = root2
                rank[root2] += 1
                
            return True
        
        for u,v in edges:
            union(u,v)
        
        return len(set([find(i) for i in parents]))


# DFS O(E + V), go thru every edges(E) to build adjacency list and every node(V) for DFS traversal  
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacents = collections.defaultdict(list)
        for p, c in edges:
            adjacents[p].append(c)
            adjacents[c].append(p)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for child in adjacents[node]:
                dfs(child)
        
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res