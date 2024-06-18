'''
  people ahead buys k tickets
  people behind buys k - 1 tickets.
  time is O(n)
'''

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        #people ahead buy k tickets
        #people behind buy k - 1 tickets
        numberOfTickets = tickets[k]
        i = 0
        res = 0
        while i < len(tickets):
            if i <= k:
                res += min(tickets[i], numberOfTickets)
            else:
                res += min(tickets[i], numberOfTickets - 1)
            i += 1
        return res