from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def _connect(curr, child_head, child_tail):
            nxt = curr.next
            curr.next = child_head
            child_head.prev = curr
            
            if nxt:
                child_tail.next = nxt
                nxt.prev = child_tail
            
            curr.child = None

        def _flatten(node):
            _head = _tail = _curr = node
            while _curr:
                if _curr.child is not None:
                    child_head, child_tail = _flatten(_curr.child)
                    _connect(_curr, child_head, child_tail)
        
                _tail = _curr
                _curr = _curr.next
    
            return _head, _tail

        return _flatten(head)[0]


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def _connect(curr, child_head, child_tail):
            nxt = curr.next
            curr.next = child_head
            child_head.prev = curr
            
            if nxt:
                child_tail.next = nxt
                nxt.prev = child_tail
            
            curr.child = None

        def _flatten(node):
            _head = _tail = _curr = node
            while _curr:
                if _curr.child is not None:
                    child_head, child_tail = _flatten(_curr.child)
                    _connect(_curr, child_head, child_tail)
        
                _tail = _curr
                _curr = _curr.next
    
            return _head, _tail

        curr = head
        while curr:
            if curr.child is not None:
                child_head, child_tail = _flatten(curr.child)
                _connect(curr, child_head, child_tail)

            curr = curr.next

        return head


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def _flatten(node):
            _head = _tail = _curr = node
            while _curr:
                if _curr.child is not None:
                    nxt = _curr.next
                    child_head, child_tail = _flatten(_curr.child)
                    
                    _curr.next = child_head
                    child_head.prev = _curr
                    
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail
                    
                    _curr.child = None

                _tail = _curr
                _curr = _curr.next
    
            return _head, _tail

        curr = head
        while curr:
            if curr.child is not None:
                nxt = curr.next
                child_head, child_tail = _flatten(curr.child)

                curr.next = child_head
                child_head.prev = curr

                if nxt:
                    child_tail.next = nxt
                    nxt.prev = child_tail

                curr.child = None

            curr = curr.next

        return head