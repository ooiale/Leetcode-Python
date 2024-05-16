'''
  starting from the end, we will check whether starting from a specific substring,
  we can find that substring in the wordDict. We need to check, for every substring along the loop whether there is a word in the dict that matches with the desired string. If so, we store in the cache that if we ever reach that position in the original string, there are words in wordDict that satisfies the conditions.
  time is O(n^2 * m) where n is the length of the word and m is the length of wordDict.
  storage is O(n) for the cache.
'''

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    cache[i] = cache[i + len(word)]
                if cache[i]:
                    break
        return cache[0]