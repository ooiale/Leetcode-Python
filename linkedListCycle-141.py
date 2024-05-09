'''
  idea: create a dummy node pointing to the head and invert the linked list.
  if there was a cycle, the cur node will reach None by reaching the dummy node so we check if the prev is the dummy.
  in case cur reaches null but dummy is never reached, there were no loops
  Time is O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        dummy = ListNode()
        prev = dummy
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if prev == dummy:
            return True
        return False