'''
  instead of multiplying x n times we can do a divide and conquer approach to achieve a O(log n) time.
  so the main idea is that x^n = (x^n/2)^2 which means that we can group up the
  factors of x in groups of 2 and then raise it to the power of n/2. but we can keep doing this iteratively (or recursively) until we are raising it to the power of 1.
  time is O(log n)

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        surplus = 1
        wasNeg = n
        n = abs(n)
        while n > 1:
            if n % 2 != 0:
                surplus = surplus * x
            x = x * x
            n = n // 2
        if wasNeg < 0:
            return 1 / (x * surplus)
        return x * surplus
