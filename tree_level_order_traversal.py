from ast import List
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        rlt = []
        
        while len(queue) > 0:
            new_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)

            if len(new_level) > 0:
                rlt.append(new_level)
            
        return rlt