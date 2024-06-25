'''
  the r pointer will be good to make this code re-usable in case you want to
  modify the 3 digit length hard requirement of the problem.
  time is O(n)
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        r = 0
        res = ""
        while l < len(num):
            r = 0
            while l + 1 < len(num) and  num[l + 1] == num[l]:
                r += 1
                l += 1
                if r == 2:
                    res = max(res, (num[l - r: l + 1]))
                    break
            l += 1
        return res