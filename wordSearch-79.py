'''
  for each element in the matrix we will do a DFS to search for the target word
  to make sure we never check the same element twice, a set is created and after passing through each element we add its index (i,j) in the path
  for each iteration in the recursion we store the index of the char we are looking for.
  if the element visited is in bounds, not in the path and is at word[i] 
  we search all adjacent cells to find the rest of the word until we finish looking for all i = len(words) - 1 letters.
  time is O(n * m * dfs)
  dfs is O(4 ^ len(word)) -> easier to see if you think about the solution in a tree.
'''

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        path = set()

        def dfs (r, c, i):
            if (r, c) in path:
                return False
            if (r < 0 or r >= ROW \
                 or c < 0 or c >= COL \
                 or board[r][c] != word[i]):
                return False
            if i + 1 == len(word):
                return True
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) \
                    or dfs(r - 1, c, i + 1) \
                    or dfs(r, c + 1, i + 1) \
                    or dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
            

        