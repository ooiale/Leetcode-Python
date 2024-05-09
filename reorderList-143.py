'''
  idea: divide the list in two halves and invert the second half. then its just merging.
  to find the middle, use the slow and fast algorithm, where slow walks one node at a time and fast walks 2 at a time. once fast is null, slow is at the middle.
  remember to cut the link between the two halves by setting slow.next = None.
  Now, invert the second half that starts at the former slow.next.
  then merge them.
  time is O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        r = s.next
        s.next = None
        prev = None
        while r:
            next = r.next
            r.next = prev
            prev = r
            r = next
            
        r = prev

        l = head
        while l and r:
            nl = l.next
            nr = r.next
            l.next = r
            r.next= nl
            l = nl
            r = nr

        