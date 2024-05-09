'''
  idea: track the maximum number of open parenthesis possible 
  as well as the minimum number through the entire string.
  but let the minimum be lower bounded by 0. 
  if the string is invalid, the max number will be negative so
  in the case the minimum is negative, it means we could have chosen
  better the symbol of the previous asterisks.
  the interval [min, max] will represent the possible amount of opening
  parenthesis remanining at the end of the string. and if 0 is in this interval then the string is valid.
  efficiency is O(n)
  memory is O(1)
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        minleft = 0
        maxleft = 0
        for c in s:
            if c == "(":
                minleft += 1
                maxleft += 1
            elif c == ")":
                minleft = max(0, minleft - 1)
                maxleft -= 1
            if maxleft < 0:
                return False
            if c == "*":
                minleft = max(0, minleft - 1)
                maxleft += 1
        if minleft == 0 and 0 <= maxleft:
            return True
        return False
            