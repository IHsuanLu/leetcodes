from tkinter.tix import ListNoteBook
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(node):
            if node is None:
                return 0
            
            level = dfs(node.next) + 1
            if level == n + 1:
                node.next = node.next.next

            return level

        # If remove head, skip head
        level = dfs(head)
        if level == n:
            head = head.next

        return head

            
                    
        