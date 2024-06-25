'''
  just add in a set all nodes that have an edge coming out of it.
  then loop through all nodes that receives an edge and check if it 
  is in that set of nodes. if it doesnt it means that node has no 
  edges coming out of it
  time is O(n)
'''

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        unique = set()
        for a, b in paths:
            unique.add(a)
        for a,b in paths:
            if b not in unique:
                return b