'''
  since we always want the biggest values in the array, and we may end up
  inserting values into the array during the code, the best way is to 
  implement a max heap. to initialize it the time complexity is O(n logn)
  searching and inserting in a heap is O(logn) so our entire loop with also have time
  complexity of O(n logn)
'''

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if y < x:
                heapq.heappush(heap, y - x)
        if heap:
            return heap[0] * -1
        return 0