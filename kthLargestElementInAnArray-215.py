'''
  natural approach would be to just sort the array and solve it in O(n logn)
  since we just want the kth largest element, we can instead use a max heap
  and then pop from the heap k times and thats our result.
  time is O(n) + O(k logn) which is faster than the sorting method for small k's (note that k here technically is n - k so for big k's)
'''

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap) #O(n)
        for _ in range(k): #O(k)
            val = heapq.heappop(heap) #O(logn)
        return -val #overall = O(k logn) + O(n)