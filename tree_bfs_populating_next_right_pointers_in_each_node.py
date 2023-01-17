from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        intuition:
            -> use BFS to traverse the nodes 
            -> connect the next pointer correspondingly
                -> connect to the node on top of the queue, except for those right most node on the level
        """
        queue = deque([root])
        while queue:
            leftmost = queue[-1]
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if not nxt:
                    continue

                if nxt == leftmost:
                    nxt.next = None
                else:
                    nxt.next = queue[0]

                for child in [nxt.left, nxt.right]:
                    if child:
                        queue.append(child)
                
        return root