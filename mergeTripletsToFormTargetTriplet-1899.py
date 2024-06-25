'''
  any triplet with a value (at same index) higher than the target value
  is an invalid triplet.
  so once we have filtered the valid triplets, we just need to see if there
  is at least one triplet with the target value at the right index. if there 
  are we can merge these together
  time is O(n)
'''

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        c1, c2, c3 = False, False, False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                c1 = True
            if b == target[1]:
                c2 = True
            if c == target[2]:
                c3 = True
        
    
        return c1 and c2 and c3