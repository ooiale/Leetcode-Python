'''
  keep track of all chars from chars in a hashMap and create a hashMap
  for all words too. now if its a good word just add the len of the word
  time is O(len(chars) + len(words) * avgsize(words))
'''

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = Counter(chars)
        res = 0
        for word in words:
            cur = Counter(word)
            for c in word:
                if c not in charsMap or cur[c] > charsMap[c]:
                    res -= len(word)
                    break
            res += len(word)
        return res