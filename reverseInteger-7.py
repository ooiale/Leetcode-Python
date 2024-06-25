'''
  this solution involves reversing the integer with 
  base 10 manipulations.
  the issue comes in avoid number overflow while keeping
  our res variable within 32 bit integer representation.
  once our next iteration will introduce the res variable
  to the billions, we need to check if it will add an integer
  that will turn our value greater than 2^31 - 1 or -2^31
  the loop will run at most 10 times and on the 11th it will
  exceed the 9.999.999.999 aka overflow.
  so time is O(digits(x)) = O(1)
'''

import math


class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648 #-2^31 ~ -10^9
        MAX = 2147483647 #2^31 -1 ~ 10^9

        res = 0
        iteration = 1 #number of digits in res, overflow should only happen starting at iter 8
        while x:
            digit = int(math.fmod(x, 10)) #avoid issues with negative
            x = int(x / 10) #avoid issues with negative

            #check for overflow if we res might exceed 2 billion aka the 10th digit
            if iteration >= 9:
                if (res > MAX/10 or (res == MAX/10 and digit > 7) ):
                    return 0
                if (res < int(MIN / 10) or (res == int(MIN / 10) and digit < -8) ):
                    return 0
            
            res = (res * 10) + digit #add the digit and move to the next "decimal?"
            iteration += 1
        return res