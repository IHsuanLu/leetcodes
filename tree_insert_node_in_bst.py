# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursively search for the correct spot (first None position)
        def dfs(node):
            if not node:
                return None
            
            if node.val < val:
                if dfs(node.right) is None:
                    node.right = TreeNode(val)
            elif node.val > val:
                if dfs(node.left) is None:
                    node.left = TreeNode(val)
            else:
                node.val = val
            
            return node
        
        if not root:
            return TreeNode(val)
    
        return dfs(root)


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursively search for the correct spot (first None position)
        def dfs(node):
            if not node:
                return TreeNode(val)
            
            if node.val < val:
                node.right = dfs(node.right)
            elif node.val > val:
                node.left = dfs(node.left)
            else:
                node.val = val
            
            return node
    
        return dfs(root)