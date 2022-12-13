from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 把 subproblems 解決之後把結果 append 到 main problem
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end):
             # this case happens when we curRootValue = start so we call helper(start, start-1). Or when curRootValue = end and we call helper(end+1, end). In both cases, within helper(), start is greater than end which will cause the for loop to not run.
            if start > end:
                
                # if we changed the based case return value to be [None]. then if left sub tree is None, it's perfectly safe to set curRoot.left = None and we avoid the problem of skipping the loop entirely.
                return [None]
            
            allTrees = []
            for curRootVal in range(start, end + 1):
                # We really want each child to not just be a single node, but rather be the root of a whole subtree.

                # should the recursive function return a single subtree? Take a look at the trees for roots 1 and 3 above, they have multiple possible subtrees! Thus, we should return all possible left and right subtrees. That is, the recursive function returns a list! I'll call this list `all_trees`.
                leftSubtrees = dfs(start, curRootVal - 1)
                rightSubtrees = dfs(curRootVal + 1, end)
                
                # every l and r is a valid tree's node
                # and we append all the combinations to the new TreeNode (no deep copy is needed) with the `selected root value` and 
                # append the root to the result, and the previous round's leftSubtrees or rightSubtrees

                for l in leftSubtrees: # get each possible left subtree
                    for r in rightSubtrees: # get each possible right subtree
                        # create root node with each combination of left and right subtrees
                        curr_node = TreeNode(curRootVal)
                        curr_node.left = l
                        curr_node.right = r
                        
                        allTrees.append(curr_node)
            
            return allTrees
        
        return dfs(1, n)