from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            total = 0
            if node.val >= low and node.val <= high:
                total += node.val

            total += dfs(node.left)
            total += dfs(node.right)

            return total

        return dfs(root)