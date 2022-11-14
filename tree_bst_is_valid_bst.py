from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(head, current_max, current_min):
            if head is None:
                return True
            
            if head.val >= current_max or head.val <= current_min:
                return False
            
            is_left_valid = dfs(head.left, head.val, current_min)
            is_right_valid = dfs(head.right, current_max, head.val)
            
            return is_left_valid and is_right_valid
        
        return dfs(root, float('inf'), float('-inf'))