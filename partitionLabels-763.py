'''
  once we add a char to the partition, we need to include all occurences
  of this char so creating a hashMap to keep track of the last idx of each
  char is a good idea.
  now iterate through the string and keep adding chars until you have added
  the lastIdx of each character added to the partition.
  time is O(n)
'''

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {} #char => last idx
        for i, v in enumerate(s):
            count[v] = i
        
        i = 0
        lastIdx = -1
        size = 1
        res = []
        while i < len(s):
            lastIdx = max(lastIdx, count[s[i]])
            if i == lastIdx:
                res.append(size)
                size = 0
                lastIdx = -1
            i += 1
            size += 1
        return res

