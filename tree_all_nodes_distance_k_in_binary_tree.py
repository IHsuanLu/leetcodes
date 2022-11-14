from ast import List
from collections import deque, defaultdict;


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjacent = defaultdict(list)
        visited = set()
        res = []
        
        def dfs(node):
            if not node:
                return
            
            if node.left:
                adjacent[node].append(node.left)
                adjacent[node.left].append(node)
            
            if node.right:
                adjacent[node].append(node.right)
                adjacent[node.right].append(node)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        queue = deque([target])
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                visited.add(nxt)
                
                if k == 0:
                    res.append(nxt.val)
                    
                for child in adjacent[nxt]:
                    queue.append(child)

            k -= 1

        return res