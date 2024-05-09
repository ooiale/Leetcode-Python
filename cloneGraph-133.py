'''
  starting from the initial node, run a DFS through every neighbor of this node
  while creating all of the copies.
  We also created a hash Map to see whether the new copy has already been made.
  this is possible because our graph is double edged and connected.
  this recursive DFS will create all nodes, then backtracking will append all the respective neighbors.
  Time is O(edge + nodes)
'''


#Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        return clone(node)
        