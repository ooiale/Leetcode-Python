'''
  the most obvious solution would be to always be sorting the array so that finding the median is O(1). However, this way, adding and removing elements would be O(n)
  and we can instead use max/min heaps which can insert and remove elements in O(logn).
  the trick will be to divide our array into 2 equal sized heaps. the first half
  will contain the half lowest numbers and will be a max heap so that we can access 
  its maximum in O(1) and the second half will contain the half biggest numbers in
  a min heap so we can access its min in O(1)
  this way, computing the median is basically taking the half of max + min
  or if one of the arrays has 1 element more than the other we will take the
  min/max of that heap.
  in order to secure these heap properties, every time we add a new number,
  we will first put it in the small heap. then we check if its biggest value
  is still lower than the other heap's min. if so we transfer that value to the other
  heap.
  and secondly we check if their lengths differ by at most 1. otherwise, we transfer
  the appropriate value to the other heap.
  this way we ensure time O(logn) for adding and O(1) for computing median
'''

import heapq

class MedianFinder:

    def __init__(self):
        #small is a max heap 
        #large is a min heap
        #we will use import heapq
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        #check if small <= large
        if (self.small and self.large) and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #check if lens are offset by max 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
        