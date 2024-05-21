from typing import List
'''
  first solution: 
  create a hashmap with the values of nums1 mapping to their index. we will need
  these values to fill in the output array.
  now to find the next greater element: loop through every element n  in nums2:
  if there are any elements smaller than n, pop them from the array and update
  the output array because n is the next greater element from the number we just 
  popped. repeat this process.
  now, if n is in nums1, add it to the stack otherwise just skip it.
  the reason this works is because the arrays are always valid and the numbers
  in it are all unique.
  time is O(len(nums1) + len(nums2))
  memory is O(len(nums1) + len(nums2))
  
  the second solution is my first solution which was O(m * n) but was on the
  direction of the optimal solution so I'll leave it here too
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {v:i for i, v in enumerate(nums1)}
        stack = []
        output = [-1] * len(nums1)
        for n in nums2:
            while stack and n > stack[-1]:
                val = stack.pop()
                output[hash[val]] = n
            if n not in hash:
                continue
            stack.append(n)
        return output
            



'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #starting at nums2 going backwards:
        #lets make a decreasing stack to keep track of big elements to the right in the array
        #grab a number in nums2, remove all elements in the stack that are smaller.
        #check if its num 1
        #if so, append to the array the rightmost element in the stack or -1 if not found
        #append to the stack the number
        #[let n = len(nums1), m = len(nums2), m > n]
        stack = []
        output = [-1] * len(nums1)
        nums1Set = set(nums1) #O(n)
        for n in nums2[::-1]: #O(m)
            while stack and n > stack[-1]:
                stack.pop()
            if n not in nums1Set:
                stack.append(n)
                continue
            if stack: #Yabe O(n)
                output[nums1.index(n)] = stack[-1]
            stack.append(n)
        return output
'''