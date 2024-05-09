'''
  idea: Since all numbers in the array are bounded by the length of the array,
  we can create a new array with the same size, where its indexes are the frequency of the element (from original array) and the element is a list containing all numbers with that frequency.
  Firstly, start with a hash map to count the frequency of all numbers.
  then create that bucket sort array where array[frequency] = [n with frequency = frequency].
  then visit each element backwards and start filling the first k most frequent elements.
  Time is O(n)
  Memory is O(n)
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        list = [[] for i in range (len(nums) + 1)]
        res = []
        for number in nums:
            if number in hash:
                hash[number] += 1
            else:
                hash[number] = 1
        for key, value in hash.items():
            list[value].append(key)
        for i in range (len(list) - 1, 0, -1):
            for values in list[i]:
                res.append(values)
                if len(res) == k:
                    return res
