'''
  this is a problem that gets reduced to a fibonacci sequence
  you could also imagine the final step to be a base case with value 1
  so you don't need to separate n = 1 as an edge case and start fibonacci
  from [1, 1]
  time is O(n)
  memory is O(1)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, cur = 1, 2
        for i in range(n - 2):
            prev, cur = cur, cur + prev

        return cur