'''
  explaining this is too confusing so I'll just show a simple example.
  take this linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6.
  the first iteration will turn this list into
  3 -> 2 -> 1 -> 4 -> 5 -> 6
  we have the get_kth aux function to get the last node of the group of k nodes. groupPrev will point at the element right before the first node of the group. group next is a pointer at the first node of the next group.
  time is O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy #node before the start of the current group

        while True:
            kth = self.getKth(groupPrev, k) #last node of current group
            if not kth:
                 break
            
            groupNext = kth.next #start of next group

            #reverse the group
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                aux = cur.next
                cur.next = prev
                prev = cur
                cur = aux
            
            aux = groupPrev.next
            groupPrev.next = kth
            groupPrev = aux
        return dummy.next


    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
