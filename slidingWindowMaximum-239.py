'''
  *not sure how to explain this honestly*
  we will create our windows using l, r pointers (window)
  l and r will dictate the size of our window.
  we initialize a queue because we want to add and pop from both right and left so deque makes these in O(1)
  so we will append the index of the values of nums in the queue.
  but we want on the left side of the queue to have only the largest number
  so whenever we try to append a big number, we need to pop the values to its right.
  because a large value will tend to stay in the queue, once our l pointer
  passes the index of this large value, we will need to popleft() it.
  once our right pointer is >= k, it means we have already created our k-sized window so after each iteration we need to decided who to insert in our output array (aka queue[0] aka largest value)
'''

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() #store the index of the num in nums
        l, r = 0, 0
        output = []
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r+1) >= k: #we made our first window, time to append to output
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output
