from ast import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, memo):
            if node is None:
                return
            
            memo[node.val] = memo.get(node.val, 0) + 1
            
            dfs(node.left, memo)
            dfs(node.right, memo)
            
        memo = {}
        dfs(root, memo)
        
        max_val = max(memo.values())
        res = []
        for k, v in memo.items():
            if v == max_val:
                res.append(k)
        
        return res