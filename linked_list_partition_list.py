from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        
        first, second = ListNode(), ListNode()
        first_curr = first
        second_curr = second
        
        while curr:
            if curr.val < x:
                first_curr.next = curr
                first_curr = first_curr.next
            else:
                second_curr.next = curr
                second_curr = second_curr.next
            
            curr = curr.next

        # Last node of "after" list would also be ending node of the reformed list 
        second_curr.next = None
        
        first_curr.next = second.next
                
        return first.next