'''
  to get the nth node from the end, start a left pointer at the start and a right pointer offset from the left by n. once right reaches null, left is at the node we want to remove. since we want the node prior to this one, start left at a dummy node instead.
  once r reaches null, just remove the node after previous.
  time is O(n)
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        for _ in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next