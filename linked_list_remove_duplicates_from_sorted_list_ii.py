from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        # set prev to dummy
        prev, curr = dummy, head
        while curr:            
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                
            if prev.next != curr:
                prev.next = curr.next
            else:
                # only move prev if curr is not shifted
                prev = curr
                
            curr = curr.next
        
        return dummy.next