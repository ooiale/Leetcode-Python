'''
  starting from the end of the list, we want to find the longest subsequence starting from each index. the base case is the last index having longest length of 1.
  Time is O(n^2)
  storage is O(n)
  It is possible to do a O(n logn) solution using binary search  the code for it is at the bottom
  the explanation behind it is:
  we will sort the array using binary search. We will do so starting from the left to the right. so whenever we insert a value in the new sorted array, all values behind that one were positioned before it in the original array, therefore, the subsequence formed from 0: position inserted is the longest subsequence. since array is 0-indexed we store pos + 1.
'''

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums) ):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
        return max(cache)
    

'''
O(n logn) code below

def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [float('inf')] * len(nums)
    dp[0] = nums[0]
    length = 1

    def binarySearch(dp, target, length):
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    for i in range(1, len(nums)):
        pos = binarySearch(dp, nums[i], length)
        dp[pos] = nums[i]
        length = max(length, pos + 1)

    return length
'''