'''
  our numbers are in range [1, n] and the indices [0, n - 1]
  so we do the mapping number => idx: i => i - 1
  pass through the array once and all numbers that exist will have the element
  in their respective index negative.
  then pass through the array again and the missing numbers contain positive
  values in their respective index
  time is O(n)
'''


from typing import List



class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            idx = abs(nums[i]) - 1
            nums[idx] = - 1 * abs(nums[idx])
        
        res = []
        print(nums)
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i + 1)
        return res