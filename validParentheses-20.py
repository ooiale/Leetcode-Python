'''
  go through each char in the string. 
  if the char is opening a parenthesis then its safe to append it to the stack
  once we find a closing parenthesis, check if the char on the top of the stack (aka the last char) is opening this parenthesis. if so pop it from the stack otherwise return false
  at the end check if len(stack) == 0 to see if there are no opening parenthesis left there.
  time is O(n)
  memory is O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            '}': '{',
            ']': '[',
            ')': '('
        } 
        stack = []
        for c in s:
            if c in hash:
                if len(stack) > 0 and stack[-1] == hash[c]:
                    stack.pop()
                    continue
                return False
            stack.append(c)
        if len(stack) == 0:
            return True
        return False
