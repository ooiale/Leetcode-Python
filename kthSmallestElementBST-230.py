'''
 Method 1: Recursive DFS: Perform a DFS in order to build
 an array with the k smallest elements from the binary tree.
 then return arr[k-1]
 Efficiency complexity O(n)
 Storage complexity O(n)

 Method 2: Iterative DFS: Using a stack, we can use a while loop
 to get to the left most node of the tree while stacking the previous
 nodes on the stack. after reaching the end, pop from the stack and
 that is the n-th smallest element. increment n by 1 and once n == k
 that is the k-th smallest node. Remember to go to the right node once you reach the left most one.
 Efficiency complexity O(n)
 Storage complexity O(n)
 where n here is the number of nodes in the tree.
'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted = []
        self.DFS(root, k, sorted)
        return sorted[k-1]
    def DFS(self, root, k, sorted):
        if not root:
            return
        if root.left:
            self.DFS(root.left, k, sorted)
        if len(sorted) == k:
            return
        sorted.append(root.val)
        if root.right:
            self.DFS(root.right, k, sorted)


    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or root: #infinite loop since its said that there is an answer
            while cur: #lets go to the left most part of the tree
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


