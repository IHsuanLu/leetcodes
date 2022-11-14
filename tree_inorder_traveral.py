from ast import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(head, curr):
            if head is None:
                return
            
            dfs(head.left, curr)
            curr.append(head.val)
            dfs(head.right, curr)
            
        res = []
        dfs(root, res)
        
        return res

# iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
                return res
            
            nxt = stack.pop()
            res.append(nxt.val)
            root = nxt.right