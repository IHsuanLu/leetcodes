from ast import List
import collections


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        we can remove any connections that is a part of cycle
            -> apply tarjan's algorithm (for finding SCC) to find circles
        """
        adjacents = collections.defaultdict(list)
        for u, v in connections:
            adjacents[u].append(v)
            adjacents[v].append(u)

        visited = set()
        low_link_values = [float('inf')] * n # store the low-link values for node

        """
        node: current node to do dfs
        idx: tarjan ID
        parent: parent of the current node
            -> to avoid repeating search
            -> to we need that for append result in the callback of the dfs
        """
        def dfs(node, idx, parent=None):
            # for undirected graph to avoid repeating search
            if node in visited:
                return
            visited.add(node)

            # assign low link value as the node's ID at first
            low_link_values[node] = idx

            for neighbor in adjacents[node]:
                """
                we cannot use `if neighbor in visited` here
                otherwise, we won't be able to traverse back to parent
                0 -> 1; 1 -> 2; 2 -> 0 (2 -> 0 won't be processed)
                """
                if neighbor == parent:
                    continue
                
                # perform dfs for the neighbor nodes
                dfs(neighbor, idx + 1, node)

                # in the callback, we assign the low link value of the current node with 
                # the minimum value between the low link value of current node and neighbors
                low_link_values[node] = min(low_link_values[node], low_link_values[neighbor])

            # if the low link value didn't get updated, meaning no loop have been founded
            if low_link_values[node] == idx and parent is not None:
                res.append([parent, node])
        
        res = []
        # since all the nodes are connected, we just need to start at any point
        dfs(0, 0)
        return res


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        cons = collections.defaultdict(set)
        for a, b in connections:
            cons[a].add(b)
            cons[b].add(a)

        low = {}
        results = []
        def visit(node, from_node=None):
            if node in low: return low[node]
            cur_id = low[node] = len(low)
            
            for neigh in cons[node]:
                if neigh == from_node: continue
                low[node] = min(low[node], visit(neigh, node))
            
            if cur_id == low[node] and from_node is not None:
                results.append([from_node, node])
            
            print(low)
            return low[node]

        visit(0)
        return results