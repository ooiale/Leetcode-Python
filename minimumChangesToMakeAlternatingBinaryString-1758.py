'''
  here is the code for an intuitive approach I guess. But
  this problem has a much clever solution:
  lets count how many swaps is needed if we start with a 0:
  this means that every odd index needs to be a 1 and
  every even index needs to be a 0 (arrs are 0-indexed)
  now to know how many swaps are needed if the arr started with a 1,
  just do len(s) - swaps_0. then return the minimum
  time is O(n)
'''

class Solution:
    def minOperations(self, s: str) -> int:
        alter = {"0": "1", "1": "0"}

        def helper(last, swap):
            i = 1
            while i < len(s):
                if s[i] == last:
                    swap += 1
                last = alter[last]
                i += 1
            return swap
        
        res1 = helper(s[0], 0)
        #res2 = helper(alter[s[0]], 1)
        #len(s) - res1 = res2
        return min(res1, len(s) - res1 )