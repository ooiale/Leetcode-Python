'''
  define a set of the input given, since duplicates don't matter in this case
  and sets have search in O(1)
  so for each number in the input, lets try to see if they are in the middle of a sequence or at the start. we only care if its at the start of a sequence.
  once we find this number, we try to look for the number n + i, while increasing i += 1 after each successfull search. the longest sequence is the longest i found.
  Time O(n)
  Memory O(n)
'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numsSet:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest