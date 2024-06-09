'''
  step 1: sort the timetable O(n logn)
  now lets run a dfs on the sorted arr making two decisions:
    1- don't select the current job and move to the next job
    2- select the current job and move to the next available job
    which we may or may not choose
  during this dfs we will compute the maximum profit choosing to take
  any possible combination of jobs. Use a cache for optimization. 
  another optimization is to use a binary search to look for the next
  available job in case you choose to take the current visited job.
  Sorting - O(n logn)
  n * Binary - O(n logn)
  overall - O(n logn)
  Memory - O(n) + O(n) = O(n) from cache and recursion
'''

from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = sorted(zip(startTime, endTime, profit))
        cache = {} #idx of the times => max profit so far
        def dfs(idx):
            if idx == len(times):
                return 0
            if idx in cache:
                return cache[idx]
            
            #not choose current job
            res = dfs(idx + 1)

            #choose current job and select the next available one (which we may or may not choose)
            j = self.binarySearch(times, idx)
            res = max(res, times[idx][2] + dfs(j)) #max of skipping the current job or choosing it
            cache[idx] = res #cache the max profit computed so far for this idx.
            return res
        return dfs(0)
    
    def binarySearch(self, times, start):
        if start >= len(times):
            return start
        startTime = times[start] #(start time, end time, profit)
        left = start + 1
        right = len(times) - 1
        idxToReturn = len(times)
        while start <= right:
            middle = (start + right)//2
            if times[middle][0] >= startTime[1]: #start time must be >= end time of startTime
                idxToReturn = middle
                right = middle - 1
            else:
                start = middle + 1
        return idxToReturn
