'''
  at every node we always have two options:
  the biggest diameter is either the sum of the largest diameter from both branches
  or its the biggest diameter from one of the left or right branches added to
  parent nodes.
  to do so it was used a dfs.
  time is O(n) since we visit all n nodes once
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return 0
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            res[0] = max(res[0], maxLeft + maxRight)
            return 1 + max(maxLeft, maxRight)
        dfs(root)
        return res[0]