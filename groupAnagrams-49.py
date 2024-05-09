'''
  storing the words in alphabetical order in a hasp map
  since all anagrams are the same sorted string.
  Time O(n * m ln(m)) 
  with n being number of words and m the average size of the words 
  memory O(n)
'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in hash:
                hash[key].append(string)
            else:
                hash[key] = [string]
        groups = []
        for keys in hash:
            groups.append(hash[keys])
        return groups