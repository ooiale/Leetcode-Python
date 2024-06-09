'''
  it is much easier to detect if a tile is uncapturable as opposed to capturing the possible tiles:
    1- it is either a O on the edge or
    2- it is an O with a path to an O on the edge
  
  so we will detect all O on the edges, run a Dfs on all of them
  to detect all uncapturable tiles and then capture everything else

  time is O(n*m)
'''

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #lets find all circles that are not capturable
        ROWS, COLS = len(board), len(board[0])

        uncapturable = set() #[(x, y)]
        for r in range (ROWS):
            if board[r][0] == 'O':
                uncapturable.add((r, 0))
            if board[r][COLS - 1] == 'O':
                uncapturable.add((r, COLS - 1))
        for c in range(COLS):
            if board[0][c] == 'O':
                uncapturable.add((0, c))
            if board[ROWS - 1][c] == 'O':
                uncapturable.add((ROWS - 1, c))
        
        #for every 'O' lets go inwards to the board
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] == 'X' or (i, j) in uncapturable:
                return
            uncapturable.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        aux = list(uncapturable)
        for i, j in aux:
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in uncapturable:
                    board[r][c] = 'X'
        