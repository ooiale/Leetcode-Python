'''
  ok so look at the way our dp matrix is structured below in the function:
  the way it works is: suppose we are at index i in word1 and index j at word 2
  we have 4 choices:
  if both match we move i and j by 1.
  if they don't match we can replace the char with a new one and move i and j by 1 (with a cost of 1 extra operation)
  if they dont match we can add or delete the current char. if we add then we need to move j by 1 (pretend we added a new char so i remains still)
  if we remove. then we move i by 1 (by pretending we removed the i-index char)
  and at each element we store the minimum number of operations to get to this point.
  time is O(m*n)
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #make a dp 2d matrix and do a bottom up algorithm
        #base cases: either strings are empty.
        #number of operations is the length of the unempty string
        #  w o r d *
        #w         5
        #a         4
        #t         3
        #e         2    
        #r         1
        #* 4 3 2 1 0
        dp = [[float("inf") for _ in range(len(word1) + 1)] for _ in range (len(word2) + 1)]
        for i in range(len(word1)):
            dp[-1][i] = len(word1) - i
        for j in range(len(word2)):
            dp[j][-1] = len(word2) - j
        dp[len(word2)][len(word1)] = 0

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                #if chars are same
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                
                #if chars are different
                else:
                    #          min(adding,     replacing,        deleting)
                    decision = min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1])
                    dp[i][j] = 1 + decision
        return dp[0][0]