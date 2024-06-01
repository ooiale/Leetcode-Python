'''
  a tree is balanced if both its subtrees are also balanced and the diffence
  in height between them are at most 1
  so we will run a dfs and check bottom up, node by node if they are balanced
  or not. if all nodes are balanced, the left and right branches from the root
  have ~ same height then the tree is balanced
  time is O(n) since we run through all nodes
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
            