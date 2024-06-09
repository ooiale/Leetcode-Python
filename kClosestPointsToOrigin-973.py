'''
  the first approach that comes to mind is to compute the distance
  of all points and then sort the array and grab the first k points.
  this solution would be O(n logn) but we can instead create a 
  min heap instead of sorting the array. this operation is O(n)
  and for each value we pop from the heap its a O(logn) time
  so after grabbing the first k values from the heap the time
  complexity would be O(n) + O(k logn) which is faster for small values
  of k.
'''

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #K closest points to (0, 0)
        #create a min heap => insertion is logn
        heap = []
        for point in points: #O(n)
            heap.append((self.dist(point), [point[0], point[1]]))
        heapq.heapify(heap) #O(n)
        output = []
        for _ in range(k): #O(k)
            vals = heapq.heappop(heap) #O(logn)
            output.append(vals[1])
        return output
    def dist(self, point):
        return (point[0] ** 2 + point[1]** 2)