'''
  the easiest solution would be to store in an array or set the index of all rows and columns that need to be zeroed. 
  the O(1) memory solution involves noticing that since we scan through the matrix from left to right, top to bottom, we can actualy update the first row and first colum inplace to say we want to zero that row or column.
  in this algorithm we will zero every column where the 0th row ith index == 0
  and every row starting from the row 1 where row[i][0] == 0.
  we will use another variable to store whether the 0th row should be zeroed since coordinates 0, 0 overlaps.
  make sure to zero the rows first then the columns since if you zero the column 0, we will end up making the null matrix.
  time is O(n^2)
  memory is O(1)
'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #we will run through the matrix left -> right, bottom -> down
        #we will store if a column needs to be zeroed at matrix[0][i]
        #same will be dome for rows at matrix[j][0]
        #(0, 0) is edge case. the var rowZero will tell if we need to zero the 0th col
        rowZero = False
        n = len(matrix)
        m = len(matrix[0])
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True


        for j in range(1, len(matrix)):
            if matrix[j][0] == 0:
                for i in range(len(matrix[0])):
                    matrix[j][i] = 0


        for i in range(0, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        


        if rowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        