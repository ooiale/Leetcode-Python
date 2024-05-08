'''
  to find common ancestor we need to have the root.value
  being a number in between the value of the other nodes.
  if the nodes are smaller than we go to the left tree
  if the nodes are bigger we go to the right tree.
  efficiency is O(log(n)) since we walk by layers through the tree
  so we check at most the height of the tree.
  memory is also O(log(n)) because we have at most the height of the
  tree of callbacks
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #root value is between (inclusive) p and q
        if p.val <= root.val and root.val <= q.val:
            return root
        if q.val <= root.val and root.val <= p.val:
            return root

        #p.val and q.val are smaller than root so ancestor is on the left side
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #p.val and q.val are bigger than root so ancestor is on the right side
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
    