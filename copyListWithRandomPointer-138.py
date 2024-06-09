'''
  the trick part is to create a map that maps the original node to the copy
  and that we need to create all copies prior to adding the random pointer
  of our copied nodes.
  This can be done iteratively with 2 while loops, one for creating the nodes
  and the second to add the pointers. or recursively like its done here
  passing through each node once and then adding the random pointers.
  Time is O(n)
'''



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = {} #original node => copied node

        def dfs(original):
            if not original:
                return None
            
            node = Node(original.val)
            old2new[original] = node
            node.next = dfs(original.next)
            node.random = old2new.get(original.random, None)

            return node
        
        return dfs(head)