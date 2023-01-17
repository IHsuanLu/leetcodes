from ast import List
import collections


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacents = collections.defaultdict(list)
        for u, v in edges:
            adjacents[u].append(v)
            adjacents[v].append(u)

        res = [0] * n
        visited = set()
        def dfs(node):
            # create a counter for every traversal
            # accumulate the result and pass the counter back to parents
            memo = {}

            # undirected graph -> ensure we only visit every node once
            if node in visited:
                return memo
            visited.add(node)

            for child in adjacents[node]:
                child_memo = dfs(child)
                
                # merge the child's counter with the parent's counter
                for k, v in child_memo.items():
                    if k in memo:
                        memo[k] += v
                    else:
                        memo[k] = v

            # update counter
            memo[labels[node]] = memo.get(labels[node], 0) + 1

            # update result
            res[node] = memo[labels[node]]
            return memo

        dfs(0)
        return res