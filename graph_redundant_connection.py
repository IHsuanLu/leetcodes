from ast import List
import collections
# Union Find
# time: O(N), space: O(N)

# why can we use the union find algorithm?
# disjoiint sets + undirected graphs

# Union Find
# Parents[node] -> look up the array and read the parent of the provided node
#         
# Find(node) -> find the absolute parent of the given node 
#            -> by looking up the array; the array indices stand for the node value; the array value stand for the parent
# 
# Union(node1, node2) -> set the absolute parent from one to another
#                     -> Parent[Find(node1)] = Find(node2)

# If the absolute parent of two nodes are already the same (there are in the same disjoint sets), then
# addiing another connection will be redundant, which creates circle -> return the `edge``

class Solution:
     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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
                return [u, v]


# DFS
# time: O(N^2), space: O(N)

'''
    Tree Properties
    1) Only 1 edge between two vertices
    2) Every child can have only one parent
    3) No cycles
    4) Must have n-1 edges where n is the number of vertices     
    
    In a valid tree, there is a unique path from each node to every other
    node in the tree:
    
         1                  1 -> 2: (1,2)
        / \                 1 -> 3: (1,3)
       2   3                2 -> 3: (2,1,3)
                            3 -> 2: (3,1,2)

    If we add one more edge to this tree, then the tree would be invalid:
    
         1                  1 -> 2: (1,2),   (1,3,2)
        / \                 1 -> 3: (1,3),   (1,2,3)
       2 - 3                2 -> 3: (2,1,3), (2,3)
                            3 -> 2: (3,1,2), (3,2)
    
    To find the redundant connection we can iterate through the list of edges
    and create the graph as we go along the list. For each node u,v in the list
    of edges if both u and v exist as nodes in the graph, then we can try and 
    form a path from u to v. 
    
    If the u -> v path already exists then adding another edge from u to v would 
    make our tree invalid.
'''  

# dfs
class Solution:
     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacents = collections.defaultdict(set)
        
        def dfs(s, t, visited):
            if s in visited:
                return False
            visited.add(s)

            # We have found a path from s to t
            if s == t:
                return True
            
            for child in adjacents[s]:
                if dfs(child, t, visited):
                    return True
            
            # We have found a path from s to t
            return False
        
        for p, c in edges:
            visited = set()
            if p in adjacents and c in adjacents and dfs(p, c, visited):
                return [p, c]
            adjacents[p].add(c)
            adjacents[c].add(p)
