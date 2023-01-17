from ast import List
import collections



# DFS
"""
For every pair of emails in the same account, draw an edge between those emails. 
The problem is about enumerating the connected components of this graph.
"""

"""
For every pair of emails in the same account, draw an edge between those emails. 
The problem is about enumerating the connected components of this graph.
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        it's a graph problem 
            -> connect all the accounts
            -> create an ajacency list 
            ```
            {
                "johnsmith@mail.com": [""john_newyork@mail.com"", "john00@mail.com"],
            }
            ```
        use dfs to enumerate the components
        """
        ajacents = collections.defaultdict(list)
        nodes = set()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if j + 1 < len(accounts[i]):
                    ajacents[accounts[i][j]].append(accounts[i][j + 1])
                    ajacents[accounts[i][j + 1]].append(accounts[i][j])
                
                nodes.add((accounts[i][0], accounts[i][j]))

        """
        iterate through nodes and run dfs for every single node
        provide a hash set `visited` to avoid visiting a same node twice

        return a enumerate component list of adjacent nodes
        """
        def dfs(node, visited):
            # no further adjacent node
            if not ajacents[node]:
                return [node]
            # do not record the node if it has been visited
            if node in visited:
                return []
            visited.add(node)

            enum = []
            for neighbor in ajacents[node]:
                enum.extend(dfs(neighbor, visited))
            
            # append the node itself
            enum.append(node)

            return enum

        res = []
        visited = set()
        for name, node in nodes:
            components = dfs(node, visited)
            if components:
                components.sort()
                res.append([name, *components])
        
        return res

