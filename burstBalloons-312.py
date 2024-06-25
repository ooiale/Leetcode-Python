'''
  lets define a Left and Right boundaries for the balloons we are going to pop.
  now for each balloon within this boundary we will choose to pop it last.
  which means that at the last iteration of popping the balloons we will have
  nums[L - 1] * nums[i] * nums[R + 1], aka the balloon we left for last and the
  two other balloons outside of the boundary. and then we proceed to pop the group
  of balloos that remained to the left of the ith balloon and to the right.
  Because our cache is a 2D tuple with values l and r ranging from 1 - n
  and for each of these tuples we iterate through at most n values (the balloons we leave for last) the time complexity is O(n^3) with n = len(nums)
'''

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  #never touch these [1]'s
        cache = {} # (l ,r ) => max number of coins
        def dfs(l, r):
            if l > r :
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            #for this bound (l, r) compute the max number of coins obtained
            #if we let the ith balloon be popped last
            cache[(l, r)] = 0
            for i in range(l, r + 1): #i = [l, r]
                coins = 0
                coins += nums[l - 1] * nums[i] * nums[r + 1] 
                #on the last iteration these 3 are the last balloons left

                #dfs on balloons to the left + dfs on balloons to the right
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                cache[ (l, r) ] = max ( cache[(l, r)], coins )
            return cache[(l, r)]

        return dfs(1, len(nums) - 2)
        