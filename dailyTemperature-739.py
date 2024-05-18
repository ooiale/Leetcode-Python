'''
  to achieve O(n) time, we can use a stack.
  iterate through each day. Once we find a day that is warmer than the previous,
  we start popping from the stack all values that are also colder than the current one. The reason we can do this is because we created a decreasing stack.
  make sure to store in the stack both value and index of each element.
  after making sure the stack still has the decreasing property, append to the stack.
  time is O(n)
  memory is O(n)
'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))
        return output

