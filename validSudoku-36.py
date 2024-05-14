'''
  Store all the rows, cols and squares in a hashMap
  loop through all cells in the board and fill the hashMaps
  once a duplicate is found the sudoku is invalid.
  Time is O(n) loop once through all cells
  Storage is O(n) we store the board 3 times in the hashMaps
'''

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(set) #key i => row i
        colHash = defaultdict(set) #key j => col j
        squareHash = defaultdict(set) #key (i // 3, j // 3) => square 
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue

                if val in rowHash[i] or val in colHash[j] or val in squareHash[(i//3, j//3)]:
                    return False
                rowHash[i].add(val)
                colHash[j].add(val)
                squareHash[(i//3, j//3)].add(val)
        return True
    