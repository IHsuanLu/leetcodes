# FAV
from ast import List
import collections


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hmap = collections.defaultdict(list)
        N = len(username)
        for i in range(N):
            hmap[username[i]].append((timestamp[i], website[i]))

        def get_pattern(websites):
            res = []
            def dfs(idx, path):
                if len(path) == 3:
                    res.append(path[:])
                    return

                for i in range(idx + 1, len(websites)):
                    path.append(websites[i][1])
                    dfs(i, path)
                    path.pop()

            dfs(-1, [])
            return res

        pattern_map = {}
        for websites in hmap.values():
            websites.sort()
            memo = set()
            for pattern in get_pattern(websites):
                k = tuple(pattern)
                if k not in memo:
                    pattern_map[k] = pattern_map.get(k, 0) + 1
                    memo.add(k)
        
        return max(sorted(pattern_map), key=pattern_map.get)
        