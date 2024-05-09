'''
  create a hashMap with the frequency of words in t,
  and the same hash but for the sliding window so the 
  frequencies start at 0.
  now run a sliding window from l = 0 and r going from 0 to the end of the string. keep incrementing r and updating the window Hash (in the code, until we have have == need) which means we fullfilled all requirements for the substring. now we see if its the smallest substring up to this point and start incrementing the l pointer to decrease the window size and try to find a smaller substring. do that until have != need (means we stopped fullfilling the requirement) and start incrementing the r pointer again.
  Time is O(n)
  Memory is O(n)
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowHash = {}
        tHash = {}
        for char in t:
            tHash[char] = 1 + tHash.get(char, 0)
            windowHash[char] = windowHash.get(char, 0)

        have = 0
        need = len(tHash)

        output = 0
        l = 0
        for r in range (len(s)):
            if s[r] in windowHash:
                windowHash[s[r]] += 1
                if windowHash[s[r]] == tHash[s[r]]:
                    have += 1
            while have == need:
                if output:
                    if output[1] - output[0] > r - l:
                        output = [l, r]
                else:
                    output = [l, r]
                if s[l] in windowHash:
                    windowHash[s[l]] -= 1
                    if windowHash[s[l]] < tHash[s[l]]:
                        have -= 1
                l += 1

            r += 1

        if output:
            return s[output[0]: output[1] + 1]
        else:
            return ""