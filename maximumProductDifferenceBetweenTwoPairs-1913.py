'''
  we can use a minHeap and maxHeap to retrieve the 2 smallest and biggest numbers
  which would result in time O(n) with memory O(n).
  or we can do one pass to find the 2 biggest and 2 smallest numbers in memory O(1)
  this algorithm works because we know there are at least 4 numbers in the array
  and 4 numbers can always be represented as n1 >= n2 >= n3 >= n4.
'''

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #we want two grab the two biggest values and the two smallest values
        m1, m2 = 0 ,0
        s1, s2 = float('inf'), float('inf')
        for i in range(len(nums)):
            n = nums[i]
            if n > m2:
                if n > m1:
                    m1, m2 = n, m1
                else:
                    m2 = n
            if n < s2:
                if n < s1:
                    s1, s2 = n, s1
                else:
                    s2 = n
        return m1*m2 - s1*s2