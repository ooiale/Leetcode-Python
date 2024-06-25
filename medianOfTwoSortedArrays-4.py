'''
  we want to create the left half of the array such that the element to
  the right of it is the middle one. 
  to do so, perform binary search on one of the arrays  in order to find the
  partition that will contain exactly 'half' elements from arrays A and B
  To check if these partitions form the left half of the merged arr, you can compare their biggest values with the other's next element outside of the partition range.
  we set the values OoB to -inf and inf to simplify some edge cases
  if the partitions don't form the left half of the array, reduce or increase
  the amount of numbers taken from arr A.
  The line where we want arr A to be the one containing the smallest amount of numbers, AFAIK is for both efficiency but to pass the edge case where A has 1 element and B has 0 elements because in this case middleB = -2 => mB + 1 is OoB but is not = inf
  all we do is a binary search on the shorted list so time is O(log(min(m, n)))
'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #[n values, median, n values]
        #use binary search to find the n values on the left partition
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(nums1) + len(nums2) 
        half = total // 2 
        leftA, rightA = 0, len(A) - 1
        while True:
            mA = (leftA + rightA) // 2 #idx of the middle rounded down. contains mA + 1 elements
            mB = half - (mA + 1) - 1 #this idx on arr b such that the number of elements 
                    #in A[0: mA] + B[0: mB] = half. the -1 is because arr is 0-indexed

            #check if merginging all elements up until mA and mB from A and B result the left half
            #of the merged array:
            aLeft = A[mA] if mA >= 0 else -float("inf")
            aRight = A[mA + 1] if mA + 1 < len(A) else float("inf")
            bLeft = B[mB] if mB >= 0 else -float("inf")
            bRight = B[mB + 1] if mB + 1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                #we have the left half of the array return the median
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                #we need to include less elements in A
                rightA = mA - 1
            elif aRight < bLeft:
                #we need to include more elements in A
                leftA = mA + 1
                