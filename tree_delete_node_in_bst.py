from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:   
        # recursively search for the node and return the root after deletion
        
        # if node.val < _key 
        #    -> search the left subtree
        # if node.val > _key
        #    -> search the right subtree
        
        # if node.val == _key
        #    -> delete the node and return the root
        
        # cases for deleting the node

        # case 1: if the target node not found
        #   -> return None
        # case 2: if the target node has one child
        #   -> if not left 
        #     -> node = node.right // skip the node as delete
        #   -> if not right
        #     -> node = node.left  // skip the node as delete
        # case 3: if the target node has two children
        #   -> find the successor the `minimum value in the right subtree`
        #     -> update node.val with the successor's value
        #.    -> delete the successor node
        
        def find_successor(node):
            # we can ensure node.right has value cause it's called only in case 4
            node = node.right
            while node.left:
                node = node.left
            return node
        
        def dfs(node, _key):
            # base case: case 1, if the target node not found
            if not node:
                return None
            
            if node.val < _key:
                node.right = dfs(node.right, _key)
            elif node.val > _key:
                node.left = dfs(node.left, _key)
            else:
                # node.val == _key, delete node
                
                # case 2, node is leaf
                if not node.left and not node.right:
                    node = None
                # case 3, node has one child
                elif not node.left:
                    node = node.right
                elif not node.right:
                    node = node.left
                # case 4, node has two children
                else:
                    successor = find_successor(node)
                    node.val = successor.val
                    # delete successor from the right subtree
                    node.right = dfs(node.right, successor.val)

            return node
        
        return dfs(root, key)
