'''
  don't be tricked into using a Trie as iterating through the list is  quicker and simpler.
  since we want all products in lexographical order, we might as well start the algorithm by sorting the array.
  after that, iterate char by char of the searchWord and use a two pointer algorithm
  to determine the first and last elements in the list that shares the searchWord prefix in it. since our list is sorted, at each iteration our list of possible seaches will either stay the same or shrink so this is why this algorithm works.
  time is O(n logn + m*n) with n = len(products) and m = len(searchWord) which should be reduced to nlogn since n is most likely >> m
  memory is O(1) if ignoring the output.
'''

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() #n log(n) => number of products
        l = 0
        r = len(products) - 1
        output = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord): #m => length of searchWord
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1 #n 
            while r >= l and  (len(products[r]) <= i or products[r][i] != c):
                r -= 1 #n
            for j in range(l, r + 1):
                output[i].append(products[j])
                if len(output[i]) == 3:
                    break
        return output