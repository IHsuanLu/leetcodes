from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # cut the linked list into half
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None
        
        # reverse second half
        prev, curr = None, second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second_head = prev
        max_sum = float('-inf')
        while head and second_head:
            max_sum = max(max_sum, head.val + second_head.val)
            head = head.next
            second_head = second_head.next
            
        return max_sum