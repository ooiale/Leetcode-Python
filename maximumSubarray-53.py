'''
  the idea here is to use a kind of sliding window technique. but since we only care
  about the maximum sum and not really the subarray itself we will only have one pointer iterating through each element.
  so we keep track of the currentSum of the subarray we are searching. as long as this sum is positive, we want to keep adding to this subarray but if at some point
  the curSum gets negative, it means we can just discard all numbers up to this point and start a new subarray. since not taking any values from the array is not an option, you should start curMax with either -inf or a random number of the array because there might be negative values
  time complexity is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        curSum = 0
        for n in nums:
            curSum += n
            curMax = max(curSum, curMax)
            if curSum < 0:
                curSum = 0
        return curMax