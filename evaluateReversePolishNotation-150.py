'''
  use a stack and do the operation when a operation symbol appears.
  use the 2 numbers on the top of the stack for the operation then append the result back in the stack
  else append the number to the stack
'''

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif t == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif t == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            elif t == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            else:
                stack.append(int(t))
        return stack[0]