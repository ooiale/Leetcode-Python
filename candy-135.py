'''
  pass once through the array to make sure all students with higher rating than its left neighbor gets 1 candy more than the left neighbor. since we initialize the candies array with all 1's we can just add the amount of candies the left neighbor has.
  now pass through the array backwards making sure that all students get more candies than its right neighbor if he has higher rating but here we bump into some edge cases
  it is possible that the right neighbor has less or more candies than the one in the left regardless of its rating. so update the student's candies only if the right neighbor has >= candies
  time is O(n)
'''

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        #make sure all stdents get more candies than left neighbor if feasible
        for i in range(1, n):
            if ratings[i] > ratings [i - 1]:
                candies[i] += candies[i - 1]
        
        #make sure all students get more candies than right neighbor if feasible
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)