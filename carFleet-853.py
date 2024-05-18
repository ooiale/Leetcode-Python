'''
  really difficult problem. Can't really explain very well.
  but we want to sort the cars by position because we will traverse the array backwards. if we ever get a fleet, it means a car behind reached a car in front.
  we will check collisions by checking how long the car will take to reach the goal. if C1 reaches the goal in 3s then any car who reaches the goal in less than 3s and started behind that car will collide. Remember to let in the stack the slower car aka the car that was in front aka just don't append to the stack a car that collides.
  time is O(n)
  memory is O(n)
'''

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, t) for p, t in zip(position, speed)]
        stack = []
        for p, t in sorted(arr)[::-1]:
            if stack and stack[-1] >= (target - p)/t:
                continue
            stack.append((target - p)/t)
        return len(stack)