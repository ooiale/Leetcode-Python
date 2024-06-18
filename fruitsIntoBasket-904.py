'''
  this problem reduces to finding the biggest window containing at most 2 different numbers.
  so just start a sliding window and slide it to the right. We can check
  the validity of our window with a hash map. whenever the window is invalid
  do a while loop sliding the left pointer until the window is valid again.
  time is O(n)
'''


from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #we want to find the longest sequence containing at most 2 different types of tree
        l, r = 0, 0
        res = 0
        fruitCount = 0
        basket = {} #fruit => count
        while r < len(fruits):

            fruit = fruits[r]
            basket[fruit] = 1 + basket.get(fruit, 0)
            fruitCount += 1
            r += 1

            while len(basket) > 2:
                fruit = fruits[l]
                basket[fruit] -= 1
                fruitCount -= 1
                if basket[fruit] == 0:
                    del basket[fruit]
                l += 1
            
            res = max(res, fruitCount)

        return res
            
                