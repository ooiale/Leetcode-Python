'''
  using recursive DFS, we will check whether the subRoot is
  a subtree for each node from the original tree. 
  time is O(n*m) where n and m are the number of nodes of the 
  original tree and the subtree respectively. 
  memory is O(n) since we will have at most n recursion callbacks
'''

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        isSubtree = False
        if root.val == subRoot.val:
            isSubtree = self.sameTree(root, subRoot)
            if isSubtree:
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right) 
        return False