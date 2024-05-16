'''
  for every digit we can either decode it as a single digit and then decode the remaining string or decode it as a double digit number and then decode the remaining string (i + 2::). 
  so starting from the end of the array we will count how many ways we can decode
  starting from that position.
  so for example if we have "123", we can either say:
  decode 1 and see how many times we can decode the rest "23" OR
  decode 12 and see how many times we can decode the rest "3"
  by starting through the end of the string we can do it in a simple iteration.
  time is O(n)
  memory is O(n)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        hash = {len(s) : 1} 
        # we add this so that the last 2 digits of the number are not edge cases for the while loop

        for i in range (len(s) - 1, -1, -1):
            if s[i] == "0":
                hash[i] = 0
                continue
            
            hash[i] = hash[i + 1] #when the coded value was a single digit

            if i + 1 < len(s)  and int(s[i : i + 2]) in range(10, 27):
                #we want to avoid numbers that start with 0
                hash[i] = hash[i] + hash[i + 2] 
                #here we add the times when i is a single digit and when i is a double digit
        return hash[0] 