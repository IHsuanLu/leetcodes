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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        queue = deque([root])
        rlt = []
        
        while len(queue) > 0:
            rlt.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        
        return rlt