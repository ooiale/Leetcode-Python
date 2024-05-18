'''
  the O(n) solution for this problem involves checking if current height
  height(i) is less than the min between the max height on the left and the max height on the right => min(height[l], height[r])
  the trick to improve efficiency involves around the fact we only care about the minimum value between l and r. So, instead of running the algorithm cell by cell, we will run the algorithm to check if we can store water at the index of the lowest between height[l] and height[r]. After that we can try to update the maxHeight of it by moving its index 1 cell inwards.
  time is O(n)
  memory is O(1)
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        output = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft) #if we update here it means water would overflow anyways
                output += maxLeft - height[l] 
                #maxLeft is either a bigger value than height[l] or IS height[l]
                #maxLeft - height[l] can only be > 0 if we didnt update our maxLeft 
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                output += maxRight - height[r]
        return output


'''
  my first idea was to scan layer by layer searching for spots
  where the area could be stored. then removing that layer and 
  repeating it again until height was a null array.
  this lead to a O(m * n) time where m is the length of the array
  and n is the biggest number in the array => slow but I was happy
  I was able to think and code this solution:

  class Solution:
      def trap(self, height: List[int]) -> int:
          # 0 1 0 2 1 0 1 3 2 1 2 1
          #     *     *
          # 0 0 0 1 0 0 0 2 1 0 1 0
          #         * * *     *
          # 0 0 0 0 0 0 0 1 0 0 0 0
          # 0 0 0 0 0 0 0 0 0 0 0 0
          # find wall, count number of zeros until next wall until OoB
          totalZeroCount = 0
          while height != [0] * len(height): #while height is not null matrix
              l = 0
              zeroCount = 0
              while l < len(height):
                  while l < len(height) and height[l] == 0:
                      l += 1
                  if l == len(height):
                      break #only walls until the end
                  #l points at a wall now
                  r = l + 1
                  while r < len(height) and height[r] != 0:
                      r += 1
                  if r == len(height):
                      break #no 0 found until the end
                  # r points at a 0 now
                  possibleZeroCount = 0 #in case water overflows we dont add to zeroCount
                  while r < len(height) and height[r] == 0:
                      if height[r] == 0:
                          possibleZeroCount += 1
                      r += 1
                  if r == len(height):
                      break #only 0s until the end => water overflows
                  zeroCount += possibleZeroCount
                  #r points at the next wall after finding at least one 0
                  l = r
              #we have scanned the entire ith floor
              totalZeroCount += zeroCount
              for i in range(len(height)):
                  height[i] = max(0, height[i] - 1)
              #remove the bottom layer
          return totalZeroCount
'''