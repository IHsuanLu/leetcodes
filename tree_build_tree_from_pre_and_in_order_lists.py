from ast import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# build tree -> find root
# the first element from preorder list will be the next root
# inorder[:idx]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        idx = inorder.index(preorder.pop(0)) 
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[0:idx]) # left
        root.right = self.buildTree(preorder, inorder[idx+1:]) # right
        return root