'''
  to build a valid parentheses you can only close the parentheses if 
  you had previously opened it. 
  perform a backtracking algorithm and adding ( or ) when its valid
  if possible to do so, append it to the stack until you have placed all 2n parentheses.
  Alternatively, we could just pass a string while concatenating it with either parentheses instead of storing in a global stack.
  Efficiency is O(n) 
  Storage is O(n)
'''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(open, closed):
            if open == closed == n:
                res.append(''.join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if open > closed:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        backtrack(0, 0)
        return res