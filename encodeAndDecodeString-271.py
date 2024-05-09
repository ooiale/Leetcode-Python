'''
  for encoding, before each string we add the length of the string followed by any type of delimiter character in this case #
  for decoding, we know the first character is one of the numbers we added so
  we read the chars of the string until we hit a # because this way we know we read the len of the encoded string. do the same until the end of the string.
  Time O(n)
'''

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        print(s)
        while i < len(s): 
            print(decoded)
            size = ''
            while s[i] != "#":
                size = size + s[i]
                i += 1
            size = int(size)
            decoded.append(s[i + 1: i + 1 + size])
            i = i + size + 1
        return decoded