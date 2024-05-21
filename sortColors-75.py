'''
  the most obvious solution is to do a two passing with constant memory by first iterating through the array once with two pointers and sorting the 0s and then
  one more time to sort the 1s.
  the trick to solving this in a single pass is to realize we could initialize 3 pointers instead. the left one will deal with organizing the 0s and the right one to deal with organizing the 2s.
  so we start a pointer that will run from 0 up to r (inclusive). if it points to a 0, we swap values with left pointer. if its a 2, swap with the right pointer.
  the tricky part here is realize that after we swap the middle pointer with the right pointer, we are only sorting the right portion of the array but might be messing with the middle portion so we don't increment m pointer here. instead,
  we will check this guy we swapped one more time.
  time efficiency is O(n) 1 passing
  memory is O(1)
'''

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #sort array [0, 0, 1, 1, 2, 2]
        l = 0
        m = 0
        r = len(nums) - 1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                
            elif  nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
                continue
            m += 1
        