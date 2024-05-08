'''
Solution 1:
  Depth First Search (DFS) with a pre order recursive algorithm:
  base case: root = None => return 0
  action: return 1 + maximum between left and right nodes.
  Efficiency and storage wise are O(n) because we run through all
  nodes and at worst we store n callbacks

Solution 2:
  Breadth first search (BFS) with pre order iterative algorithm:
  we will initialize a queue and add all nodes from the current level
  since a new level exits we increment depth by 1. now we will pop all
  theses nodes who are on the leftside of the queue and append on the right side of the queue the child nodes from each popped node.
  Efficiency and storage are O(n) since we visit all nodes and store a queue which in worst case contains all nodes

Solution 3:
  DFS with pre order iterative algorithm:
    Add the root to a stack and its current Depth level = 1. 
    now we pop from the stack this node and append to the top of the stack its children nodes which we known has depth = ParentNode's Depth + 1
    try to update the maximum value seen for depth.
    Efficiency and storage are O(n)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque #for BFS

class Solution:
    #Recursive DFS
    def maxDepth(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return 0
        leftSize =  self.maxDepth(root.left)
        rightSize = self.maxDepth(root.right)
        return 1 + max(leftSize, rightSize) 
    
    #Iterative BFS
    def maxDepth2(self, root: Optional[TreeNode], count = 0) -> int:
        
        if not root:
            return 0
        level = 0
        currentLevel = deque([root])

        while currentLevel:
            for i in range (len(currentLevel)):
                node = currentLevel.popleft()
                if node.left:
                    currentLevel.append(node.left)
                if node.right:
                    currentLevel.append(node.right)
            level += 1
        return level
    
    def maxDepth3(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]] #node and depth
        maxDepth = 1

        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return maxDepth