'''
  lets use a double ended queue to run a BFS. to get the right most node
  of each level, first we append the left child then right child. so this way,
  the last node we visit in our queue is the right most child. 
  at the end of each level, we append the value of this last node to our result
  time is O(n) where n is number of nodes
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque([root])
        while queue:
            rightmost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightmost = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightmost:
                output.append(rightmost.val)

        return output