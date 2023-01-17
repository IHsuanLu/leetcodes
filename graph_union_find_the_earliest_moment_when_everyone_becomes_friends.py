# FAV
from ast import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        symmetric -> undirected graph
        acquainted -> if nodes are connected as a small group
        
        conduct union find
        ,
        """
        logs.sort(key= lambda it: it[0])

        parents = [i for i in range(n)]
        ranks = [0] * n

        """
        [0,0,1,2,4]
        think of `node == 3`
        """
        def find(node):
            parent = parents[node]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]

            return parent

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2: # already in the same set
                return False

            rank1, rank2 = ranks[root1], ranks[root2]
            if rank1 >= rank2:
                # merge small set to large set
                parents[root2] = root1
                ranks[root1] += 1
            else:
                parents[root1] = root2
                ranks[root2] += 1

            return True

        for timestamp, x, y in logs:
            union(x, y)
            if len(set([find(i) for i in parents])) == 1:
                return timestamp

        return -1