from ast import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        curr = root
        
        while True:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left

            if not stack:
                break
            
            curr = stack.pop()
            curr = curr.right

        return res


# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res