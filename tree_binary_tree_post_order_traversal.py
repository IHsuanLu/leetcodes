# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        def dfs(node, memo):
            if not node:
                return None
            
            dfs(node.left, memo)
            dfs(node.right, memo)
            
            memo.append(node.val)
            
        memo = []
        dfs(root, memo)
        
        return memo


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  
        res, stack = [], []
        
        prev, curr = None, root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # avoid pop directly in post order cases
            top = stack[-1]
            if top.right and top.right != prev:
                curr = top.right
            else:
                res.append(top.val)
                prev = top
                stack.pop()

        return res