from ast import List
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = collections.defaultdict(list)
        # { 0: [], 1: [ # list of roots of the FBTs ], 2: ... }
        memo[0] = []
        memo[1] = [TreeNode(0)] # base case
        
        def dfs(remaining_count):
            if remaining_count % 2 == 0:
                return []
            if remaining_count in memo:
                return memo[remaining_count]
            
            # a list to store different BST with N Nodes
            all_trees = []

            for left_subtree_nodes in range(1, remaining_count, 2):
                left_subtrees = dfs(left_subtree_nodes)
                right_subtrees = dfs(remaining_count - 1 - left_subtree_nodes)
                
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode()
                        root.left = l
                        root.right = r
                        
                        all_trees.append(root)
                        
            memo[remaining_count] = all_trees
            return all_trees
        
        return dfs(n)