# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, acc):
            if not node:
                return False
            
            acc += node.val

            if acc == targetSum and not node.left and not node.right:
                return True
            
            left_result = dfs(node.left, acc)
            right_result = dfs(node.right, acc)
            
            return left_result or right_result
                
        
        return dfs(root, 0)
                