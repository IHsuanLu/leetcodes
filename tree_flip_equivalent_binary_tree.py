# we realize we solve the problem from the sub problems first, meaning that it is a recursive definition
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            non_flipped_left = dfs(node1.left, node2.left)
            non_flipped_right = dfs(node1.right, node2.right)
            
            flipped_left = dfs(node1.left, node2.right)
            flipped_right = dfs(node1.right, node2.left)
            
            return (non_flipped_left and non_flipped_right) or (flipped_left and flipped_right)
        
        return dfs(root1, root2)