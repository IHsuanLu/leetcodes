# FAV
from ast import List
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# record leaves in each level
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = collections.defaultdict(list)
        def dfs(node):
            if not node:
                return 0
            
            level = max(dfs(node.left), dfs(node.right)) + 1
            memo[level].append(node.val)

            return level
            
        dfs(root)
        return memo.values()


# naive DFS (delete simulation)
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node):
            if not node:
                return [], False

            leaves = []
            found = False
            if not node.left and not node.right:
                leaves.append(node.val)
                found = True

            left_leaves, left_found = dfs(node.left)
            leaves.extend(left_leaves)
            if left_found:
                node.left = None
            
            right_leaves, right_found = dfs(node.right)
            leaves.extend(right_leaves)
            if right_found:
                node.right = None
            
            return leaves, found

        if not root:
            return []

        res = []
        while root.left or root.right:
            leaves, _ = dfs(root)
            res.append(leaves)

        res.append([root.val])
        return res
            

# Topological Sort
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Get the degree of each node.
        degrees = {}
        parents = {}
        self.get_degrees_and_parents(root, degrees, parents)
        # Initialize the queue with the leaves (nodes with degree == 0)
        queue = collections.deque()
        for node, degree in degrees.items():
            if degree == 0:
                queue.append(node)
        # Iterate over all nodes as their degree becomes 0.
        result = []
        while len(queue) > 0:
            leaves = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node != root:
                    parent = parents[node]
                    degrees[parent] -= 1
                    if degrees[parent] == 0:
                        queue.append(parent)
                leaves.append(node.val)
            result.append(leaves)
        return result

    def get_degrees_and_parents(self, root, degrees, parents):
        if not root:
            return
        degrees[root] = 0
        if root.left:
            parents[root.left] = root
            degrees[root] += 1
            self.get_degrees_and_parents(root.left, degrees, parents)
        if root.right:
            parents[root.right] = root
            degrees[root] += 1
            self.get_degrees_and_parents(root.right, degrees, parents)