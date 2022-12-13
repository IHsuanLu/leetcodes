from ast import List
import collections


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        pid = [1,3,10,5], ppid = [3,0,5,3]
        
        {
            0: [3]
            3: [1, 5]
            5: [10]
        }
        """
        adjacents = collections.defaultdict(list)
        n = len(pid)
        for i in range(n):
            adjacents[ppid[i]].append(pid[i])

        res = []
        def dfs(node):
            res.append(node)
            for child in adjacents[node]:
                dfs(child)
        
        dfs(kill)
        return res