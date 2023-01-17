"""
Time Complexity: O(nlogn)

Suppose our linked list consists of N elements. 
For every list we pass to our recursive function, we have to calculate the middle element for that list. 
For a list of size N, it takes N/2 steps to find the middle element.

N/2 + 2 * (N/4) + 4 * (N/8) .... => (n*logn)

Space Complexity: O(logn) -> the recursion stack
"""

# FAV
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        divide the linked list into smaller portions
            -> find the root of the trees, return to the parent
        """

        def find_mid(node):
            fast = slow = node
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            
            # cut the connection between two sub lists
            if prev and prev.next:
                prev.next = None
            else:
                # if `slow` pointer is still pointing to the `node`
                node = None
            
            # slow is the root of the second tree
            return node, slow
        
        def divide_and_conquer(node):
            if not node:
                return
            
            start, mid = find_mid(node)

            # mid should be the root
            root = TreeNode(mid.val)
            root.left = divide_and_conquer(start)
            root.right = divide_and_conquer(mid.next)

            return root

        return divide_and_conquer(head)