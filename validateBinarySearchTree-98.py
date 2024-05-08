'''
  using DFS to visit all nodes. All values to the left of a parent node must be upper bounded by the parent's value so the DFS will run passing the appropriate boundaries to the child nodes. To the right of a parent node, all values must be lower bounded by it so same thing is applied here.
  Efficiency complexity is O(n) 
  Storage complexity is O(n)
  since we run through the recursion through all nodes. 
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isCorrectBounded(root, -float('infinity'), float('infinity'))
    def isCorrectBounded(self, root, lower, upper):
        if not root:
            return True
        if lower < root.val and root.val < upper:
            if self.isCorrectBounded(root.left, lower, root.val) and self.isCorrectBounded(root.right, root.val, upper):
                return True
        return False