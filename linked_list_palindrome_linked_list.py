from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        
        if not fast:
            return True
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        sn = slow.next
        slow.next = None
        
        # reverse sn
        prev, curr = None, sn
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        while head and prev:
            if head.val != prev.val:
                return False
            
            head = head.next
            prev = prev.next
                    
        
        return True
        