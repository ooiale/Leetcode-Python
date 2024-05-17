'''
  let text1 = abcd, text2 = bd
  create a 2D grid n + 1 x m + 1 with n and m being length of strings:
  X b d X
  a 0 0 0
  b O 0 0
  c 0 0 0
  d 0 O 0
  X 0 0 0
  the extra rows and cols are to auxiliate the dynamic programming code:
  so running backwards bottom -> up, right -> left, we will compute
  the longest common subsequence up to this point. 
  if both chars match, we go to the cell on the diagonal because it means
  we are checking for a new char on the next char of the string.
  if chars don't match, we get the max of its right or bottom neighbors
  which means its max of searching for a new char or max of moving on to the next
  char of the string.
  time is O(n x m)
  memory is O(n x m)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        width, height = len(text1) + 1, len(text2) + 1
        grid = [[0] * width for _ in range(height)]
        for i in range(height - 2, -1, -1):
            for j in range(width - 2, -1, -1):
                if text1[j] == text2[i]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]