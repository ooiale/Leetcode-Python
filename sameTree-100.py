'''
 Perform a recursive DFS on both trees.
 Base case: if p == None and q == None => return True
 Action: if p exits and q exits and p.val == q.val then check 
 if p.left == q.left and p.right == q.right. 
 if so then return True 
 Otherwise its False
 Efficiency and memory are O(n) where n is total number of nodes in p and q
'''


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False
