'''
  so the minimum number of bananas koko can eat an hour is 1, and the maximum
  is max(piles). To find the minimum and feasible solution to this probably we will do a binary search on the range [1, max(piles)]. the reason we can do this is that if koko can not eat the bananas in time while eating M bananas/h then if koko eats m < M bananas then it will also not be a feasible solution. and if koko CAN eat the bananas in time while eating m bananas/h then since we want the minimum, we know the minimum is either m or k < m bananas/h so the search continues.
  time is O(log(max(piles))n) with n being the length of piles.
'''

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #number max of bananas is max(piles)
        #number min of bananas is 1
        #binary search to find the optimal amount of bananas between [1, max(piles)]

        def canEat(amount):
            t = 0
            for pile in piles:
                if pile % amount == 0:
                    t += pile//amount
                else:
                    t += (pile // amount) + 1
            return t <= h

        l = 1
        r = max(piles)
        output = r
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if canEat(m):
                output = m
                r = m - 1
            else:
                l = m + 1
        return output

