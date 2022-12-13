from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leave_seq = []
        def dfs(node):
            if not node:
                return None
            
            left_node = dfs(node.left)
            right_node = dfs(node.right)

            if not left_node and not right_node:
                leave_seq.append(node.val)

            return node
        
        dfs(root1)
        dfs(root2)

        l, r = 0, len(leave_seq) // 2
        while r < len(leave_seq):
            if leave_seq[l] != leave_seq[r]:
                return False
            
            l += 1
            r += 1

        return True


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leave_seq = []
        def dfs(node, in_creation):
            if not node:
                return None, True
            
            left_node, is_left_valid = dfs(node.left, in_creation)
            right_node, is_right_valid = dfs(node.right, in_creation)

            if not left_node and not right_node:
                if in_creation:
                    leave_seq.append(node.val)
                else:
                    if not leave_seq or (leave_seq and leave_seq.pop(0) != node.val):
                        return node, False

            return node, is_left_valid and is_right_valid
        
        dfs(root1, True)
        _, is_valid = dfs(root2, False)

        return is_valid and not leave_seq