'''
  simulating the problem. there is a math solution in O(1) booring
  time is O(n)
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        amount = 0
        baseAmount = 0
        for i in range(n):
            if i % 7 == 0:
                baseAmount += 1
                amount = baseAmount
            res += amount
            amount +=1
        return res
            