'''
  create a stack where each element has its value
  and the minimum value seen so far in the stack
'''

class MinStack:

    def __init__(self):
        self.stack = [] #tuples (value, min so far)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        minSoFar = min(self.stack[-1][1], val)
        self.stack.append((val, minSoFar))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()