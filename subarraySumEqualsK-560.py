'''
  really hard to grasp:
  the main point here is:
  the sum of the subArray from idx 1: 3 is the same as 
  sum of subArray from 0: 3 - sum of subArray from 0 to 1 (last idx is exclusive)
  so in one pass we can compute the prefix sum which is the subArrays from 0: a
  and with this we can check whether the subArray from a: b sums to k with the formula
  sum Sub(0: b) - k = Sub(a: b) and check if it equals to k
  time is O(n)
'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Sliding window does not work because nums[i] may be negative
        #for this solution its important to know that:
        #Sum of subarray [a: b] = sum of subArray[0: b] - sum of subArray[0: a]
        #so we will keep track of the prefixSums for the entire array to "build" the sub arrays
        
        currentSum = 0 #just add all numbers forming the subArray [0: b]
        prefixMap = {0: 1} #prefixSum => count
        res = 0
        for n in nums:
            currentSum += n

            if currentSum - k in prefixMap: #looking for the subArray [0: a] to remove so [a: b] == k
                res += prefixMap[(currentSum - k)]
            
            prefixMap[currentSum] = 1 + prefixMap.get(currentSum, 0)
        return res