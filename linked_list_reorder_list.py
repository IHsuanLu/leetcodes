from typing import Optional


# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves

def _splitList(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):
    tail = head = a

    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a
            
    return head


class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)



# Neet Code solution


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # spliting the list in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # spliting
        
        # reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next # keep the reference
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
