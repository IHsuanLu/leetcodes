from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.target = None
        self.successor = None
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            
            if self.target and not self.successor:
                self.successor = node
            if node.val == p.val:
                self.target = node
                
            dfs(node.right)
            
        dfs(root)
        return self.successor