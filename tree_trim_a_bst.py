# If the val of current node is smaller than L, abandon the left sub-tree and trim its right sub-tree
# If the val of current node is greater than R, abandon the right sub-tree and trim its left sub-tree
# Else, recursively trim its left and right sub-tree and return the root

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(node): 
            if node is None:
                return None
            
            if node.val > high:
                return dfs(node.left)
            
            if node.val < low:
                return dfs(node.right)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            return node
        
        return dfs(root)