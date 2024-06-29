'''
  an example is the best way to explain this example:
  suppose s: ]]][[[, keep a variable that will track the number of extra
  closing brackets. so in this case: 3. so we obvious solution is that 3
  is one of the solutions. But now, lets swap only 1 of the brackets for now:
  []][[]. Notice that we swapped a opening brackets with a closing brackets
  and now if we did the math, the first bracket is opening so add -1 to extraClosed and we would have the other two closing brackets so + 2, resulting in 1.
  so for every bracket we swap, we can reduce the extraClosed by 2. our goal
  is to have this value reach zero so just take the floor of extraClosed rounding up
  and that is the minimum number of swaps. 
  time is O(n)
  memory is O(1)
'''

class Solution:
    def minSwaps(self, s: str) -> int:
        extraClosed = 0
        res = 0
        for c in s:
            if c == ']':
                extraClosed += 1
                res = max(res, extraClosed)
            else:
                extraClosed -= 1
        return (res + 1) // 2
        