'''
  the idea is to use the properties of the inorder and preorder to
  partition the elements that make the left side and right side of the
  tree. Preorder[0] = root. everything before the root value in inorder
  is to the left and the rest is to the right.
  do a DFS recursion to build the tree.
  Efficiency and storage are complexity of O(n) 
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0]) #ideally use a data strucutre for this to be O(1) like a hashMap.
        root.left = self.buildTree(preorder[1:middle + 1], inorder[0:middle])
        root.right = self.buildTree(preorder[middle + 1::], inorder[middle + 1::])
        return root
        