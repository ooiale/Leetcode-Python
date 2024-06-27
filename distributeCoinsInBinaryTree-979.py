'''
  Honestly, really difficult and not intuitive...
  do a post order dfs. then compute how many moves are needed for a node with excess of coins to pass all of it to the parent node. Or if a node has deficit of coins
  how many moves (1) it needs to receive the needed coins from the parent node.
  time is O(n)
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return [0, 0] #size of subtree, coins in the subtree
            
            l_size, l_coins = dfs(node.left)
            r_size, r_coins = dfs(node.right)

            size = 1 + l_size + r_size #size of current subtree
            coins = node.val + l_coins + r_coins #number of coins in current subtree

            self.res += abs(coins - size) #moves needed to pass all extra coins to the parent node
                                    #or if its negative it means tihs node needs 1 move to receive coin
            
            return[size, coins]
        dfs(root)
        return self.res