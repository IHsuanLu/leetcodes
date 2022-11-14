from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        def dfs(head):
            if head is None:
                return -1
            
            left_depth = dfs(head.left)
            right_depth =  dfs(head.right)
            self.counter = max(self.counter, 2 + left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return self.counter