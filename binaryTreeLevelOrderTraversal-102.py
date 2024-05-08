'''
  We will use BFS to visit each node of the tree by implementing
  a queue. so starting from the root, append to the queue its children
  nodes. then remove these nodes while appending to the queue their children nodes.
  time complexity O(n)
  space complexity O(n)
  where n is the number of nodes.
'''

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            output.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                output[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output
