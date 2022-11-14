# key of writing dfs
#   -> write the base case
#   -> write the recursive case and assume it's gonna work
#   -> get the return value if any
#   -> do the further things with the returned value 

# process the left subtree and stick it in the right subtree recursively
#  -> re-assign the right pointer to actually pointing to the start of the left subtree
#  -> update the left pointer to pointing to None  
#  -> the end of the left subtree should be pointing to the right child of the root node
#       -> after flattening, we should return the tail

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # flatten the tree and return the list tail
        def dfs(node):
            if node is None:
                return None

            left_tail = dfs(node.left)

            if left_tail is not None:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            right_tail = dfs(node.right)
                
            # if right_tail is None, we should return node;            
            return right_tail or node
        
        dfs(root)        