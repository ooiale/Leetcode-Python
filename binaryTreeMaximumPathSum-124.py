'''
  the most simple case is when we have a node with just a left and right child.
  in this case we want to take the maximum of either just adding the node itself, the node with either child or the node with both children. to make this easier we will always do maxRight = max(0, dfs(right)) so in case the children's value is negative, we make it 0.
  however, once we add one more layer of nodes, we will have to choose between picking the child node with either left or right tree. we cant form a path by picking both children. So we will return the max between picking left or right child.
  time is O(n) since we visit each node once.
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(0, leftMax) #incase its negative
            rightMax = max(0, rightMax)

            #only if we are on the current node, we can take
            #the path adding both left and right paths
            res[0] = max(res[0], node.val + leftMax + rightMax)

            #the parent of the current node may only pick the left or
            #right branch from the current node
            return max(node.val + leftMax, node.val + rightMax)
        dfs(root)
        return res[0]