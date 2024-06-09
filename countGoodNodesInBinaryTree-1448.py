'''
  run through the tree using a dfs and always storing the max value seen
  so far. in this case I used an ascending value queue. 
  It is possible to compact this code a little more by passing the max
  value seem so far as a param instead of storing in a queue.
  we could also be returning the number of good nodes instead of updating
  a global variable for ex: res = 1 if node.val >= max, res = res + dfs(left) + dfs(node) and in the end return res.
  time is O(n) regardless
  memory is O(log(n)) height of tree

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0 
            res = 0 
            if node.val >= maxSoFar:
                res += 1
            maxSoFar = max(node.val, maxSoFar)
            res += dfs(node.left, maxSoFar)
            res += dfs(node.right, maxSoFar)
            return res
        return dfs(root, root.val)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #do a dfs while filling a ascending only queue
        queue = [-101] #just so root is always good
        res = [0]
        def dfs(node):
            if not node:
                return
            if node.val >= queue[-1]:
                res[0] += 1
                queue.append(node.val)
            dfs(node.left)
            dfs(node.right)
            if node.val >= queue[-1]:
                queue.pop()
        dfs(root)
        return res[0]