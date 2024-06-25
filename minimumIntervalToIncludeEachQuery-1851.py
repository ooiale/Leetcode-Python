'''
  by sorting both interval and query arrays, we can solve this problem in one pass
  through each array.
  by sorting both, we can always check all available intervals for each query, and in order to retrieve the smallest interval, we can create a minHeap which will store the values(interval length, end of interval). whenever our query value is below the end of interval, the value popped from the minHeap is the minimum one, because at each iteration we append to the minHeap all possible intervals.
  since we sorted the queries, we need to keep track of the original array, so this is why we used a hashMap to map query => interval length.
  time is O(n logn + q logq), for both sorts. note that the loop part runs through queries and intervals just once to the loop is O(n + q) 
'''

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        res = {} # maps query => size
        minHeap = [] #(interval length, end of interval)
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]) ) 
                #add intervals that start before(or =) the query
                #later remove the interval that ends before the query
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1
        
        for i in range(len(queries)):
            queries[i] = res[queries[i]]
        return queries