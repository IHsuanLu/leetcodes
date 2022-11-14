# Definition for a binary tree node.
from ast import List
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        map = {}
        res = []

        if not root:
            return res
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                node, group = queue.popleft()
                
                if group in map:
                    map[group].append(node.val)
                else:
                    map[group] = [node.val]
                    
                if node.left is not None:
                    queue.append((node.left, group - 1))
                    
                if node.right is not None:
                    queue.append((node.right, group + 1))
        
        while map:
            min_key = min(map.keys())
            res.append(map[min_key])
            del map[min_key]
                
        return res