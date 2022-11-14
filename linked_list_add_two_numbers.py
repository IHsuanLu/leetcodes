from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            # shift pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()
        
        add_one = False
        while l1 and l2:
            new_node = ListNode()
            
            sum_val = l1.val + l2.val + (1 if add_one else 0)
            if sum_val > 9:
                new_node.val = sum_val % 10
                add_one = True
            else: 
                new_node.val = sum_val
                add_one = False

            curr.next = new_node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        remained = l1 or l2
        while remained:
            new_node = ListNode()
            sum_val = remained.val + (1 if add_one else 0)
            if sum_val > 9:
                new_node.val = sum_val % 10
                add_one = True
            else: 
                new_node.val = sum_val
                add_one = False

            curr.next = new_node
            curr = curr.next
            
            remained = remained.next
        
        if add_one:
            curr.next = ListNode(1)
            curr = curr.next
        
        return head.next