'''
  start two pointers, prev at None and cur at Head
  current points to previous, previous goes to current
  and current goes to next. since we lost the pointer to next we store that pointer before these operations.
  do this until cur is None which means prev is the new Head.
  time is O(n)
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev