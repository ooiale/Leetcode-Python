'''
  we are always intereted in knowing the minimum value in the hand. so a minHeap would work as well. but in this case sort the array. we know that there is only
  1 possible sequence to be formed with the lowest value: i, i + 1, i + 2.
  so make this sequence until the count of i = 0. then move to the next lowest
  card in your hand. 
  time is O(n log(n)) for sorting.
'''

from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = {} #card => qtnty
        for i in sorted(hand):
            cards[i] = 1 + cards.get(i, 0)
        
        for key in cards.keys():
            while cards[key] > 0:
                aux = key
                for _ in range(groupSize):
                    if aux in cards and cards[aux] > 0:
                        cards[aux] -= 1
                    else:
                        return False
                    aux += 1
        return True

