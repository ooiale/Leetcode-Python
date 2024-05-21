'''
  for every cell in the array, check if its possible to insert a flower.
  if it is, insert the flower. To see if the element is plantable,
  check if previous spot is free and next spot is also free.
  time is O(n)
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0
            


