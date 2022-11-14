from ast import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create adjacent lists
        pre_map = {i: [] for i in set("".join(words))}
        
        for i in range(1, len(words)):
            min_length = min(len(words[i]), len(words[i - 1]))
            for j in range(min_length):
                if words[i][j] != words[i-1][j]:
                    pre_map[words[i][j]].append(words[i-1][j])
                    break
                
                if j == min_length - 1 and len(words[i-1]) > len(words[i]):
                    return ""
        
        res = []
        visited = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            
            for pre in pre_map[node]:
                if not dfs(pre):
                    return False
                
            cycle.remove(node)
            
            visited.add(node)
            res.append(node)
            return True
            
        
        for node in pre_map:
            if not dfs(node):
                return ""
        
        return "".join(res)