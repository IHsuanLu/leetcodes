from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node):
            if not node or not node.next:
                return node
            
            first_node = node
            second_node = node.next
            
            last_head = dfs(second_node.next)
            
            first_node.next = last_head
            second_node.next = first_node
            
            return second_node
            
            
        return dfs(head)