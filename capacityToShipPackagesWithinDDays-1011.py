'''
  the min number of capacity is max(weights) resulting in, worst case scenario len(weights) days to ship (1 package at a time) and the max number of capacity is the sum(weights) resulting in 1 day for shipping.
  Since our capacity is bounded we can apply binary search on it to find the minimal solution. The reason this works is: if we can not ship within D days with cap = cap, it means that any amount less than cap also cannot fullfil our requirements so we move left pointer to m + 1. 
  If its possible to ship, we will store this value of m and try to ship with less capacity making r = m - 1.
  let r = sum(weights) and l = max(weights)
  time is n log(r-l) where n is the length of weights.
  log(r-l) comes from binary search, n comes from the helper function.
'''

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #do a binary search between max(weights), sum(weights) because
        #this way we ensure being possible to deliver from len(weights) days
        #to in 1 day
        def possible(cap):
            curSum = 0
            minDays = 0
            for w in weights:
                if curSum + w > cap:
                    minDays += 1
                    curSum = 0
                curSum += w
            return minDays + 1 <= days
        
        l = max(weights) 
        r = sum(weights) 
        output = r
        while l <= r:
            m = (l+r)//2
            if possible(m):
                output = m
                r = m - 1
            else:
                l = m + 1
        return output
        