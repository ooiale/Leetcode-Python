'''
  through recursion, divide the array in half each time until
  the base case where there is only 1 element.
  the left side will be the slice arr[l: m] and the right the slice arr[m+1: r]
  then merge the left and right partition of the array.
  the merging part is done inplace to minimize memory usage.
  to do so, we use 3 pointers and make two copies of the original array that represents each slice that we are merging.
  time complexity O(n logn)
  memory complexity O(n) from the temporary arrays
'''

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            idx, idx_l, idx_r = l, 0, 0
            left, right = arr[l:m + 1], arr[m+1: r+1]
            while idx_l < len(left) and idx_r < len(right):
                if left[idx_l] <= right[idx_r]:
                    arr[idx] = left[idx_l]
                    idx_l += 1
                else:
                    arr[idx] = right[idx_r]
                    idx_r += 1
                idx += 1
            while idx_l < len(left):
                arr[idx] = left[idx_l]
                idx += 1
                idx_l += 1
            while idx_r < len(right):
                arr[idx] = right[idx_r]
                idx += 1
                idx_r += 1
        def mergeSort(arr, l, r):
            if l == r:
                return 
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
        mergeSort(nums, 0, len(nums) - 1)
        return nums