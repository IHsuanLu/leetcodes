from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(head):
            if head is None:
                return None
            
            head.left, head.right = head.right, head.left
            
            dfs(head.left)
            dfs(head.right)
            
            return head
        
        return dfs(root)