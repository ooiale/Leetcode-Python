'''
  we will run through the array once computing the max, min values up to that point. the reason we store the minimum is to deal with negative values since
  a very negative number becomes a big positive number once multiplied by -1.
  once we find a 0, what the algorithm should do is reset its values since we already know the maximum value until that 0. The reason this algorithm already passes this edge case is because once we find a 0, curMin and curMax = 0
  and then these values will update themselves with the following numbers.
  the trick is to compare max with the number itself as well which also solves the issue with eg: [-1, 2]. maximum product should be the 2 by itself.
  time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = -float("inf")
        curMin, curMax = 1, 1

        for n in nums:
            aux = min(n * curMin, n * curMax, n) #curMin
            curMax = max(n * curMin, n * curMax, n)
            curMin = aux
            output = max(output, curMax)
        return output

            