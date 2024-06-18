'''
  we will solve using bellman's ford algorithm.
  make an array that will keep track of the min cost up to the node idx
  now, iterating k + 1 times, we will check for every single edge given:
  does the source node have a computed cost? if so update the destiny cost
  as the minimum between the destiny price so far and the price from source
  plus the cost between src and dst.
  If the source node does not have a price it means we haven't computed it
  yet so just skip it.
  the trick part here is to only make changes in the copy of the array
  during the iterations to avoid computing multiple flights in a single
  iteration. after the iteration only then update the actual array.
  time is O(E * K)
'''

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            pricesCopy = prices.copy()

            for s, d, c in flights:
                if prices[s] != float("inf"):
                    pricesCopy[d] = min(pricesCopy[d], prices[s] + c)
            prices = pricesCopy

        return prices[dst] if prices[dst] != float("inf") else -1 



            
