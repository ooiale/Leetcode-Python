'''
  if we are always looking for the kth largest element, we can create
  a min heap with at most k numbers. this way, the kth largest element
  will always be the smallest element in the heap.
  to initialize the heap the complexity is O(n logn) because insertion in a heap
  is logn and we will insert all values from nums.
  now, when we want to insert a number, we insert it in the heap, if the heap exceeds
  k elements we pop from the heap.
  then return the smallest element from the heap.
  time for adding is O(logn)
'''

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
