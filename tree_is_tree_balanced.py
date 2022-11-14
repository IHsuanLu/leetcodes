from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(head):
            if head is None:
                return 0
            
            left_height = dfs(head.left)
            right_height = dfs(head.right)
            
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return dfs(root) != -1
        