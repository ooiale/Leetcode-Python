'''
  initialize 2 hash maps, one with the chars and amount of it in the string 1
  and the other with the chars of string 1 but at 0 occurences
  now we scan index by index the string 2 using the sliding window technique.
  if we dont find a char from s1, we move both l and r pointers.
  once we find one of the desired chars, we will try to find the permutation of the word. keep adding the matching chars to the s1 Hash until we have found the permutation of s2. if we find a different char, reset everything. but if we get an surplus of desired chars, we start moving the left pointers until we fix the required amount of each char.
  time is O(n)
  memory is O(n)
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = {}
        s2Hash = {}
        for c in s1:
            s1Hash[c] = 1 + s1Hash.get(c, 0)
            s2Hash[c] = 0
        
        l = 0
        r = 0
        while r < len(s2):
            c = s2[r]
            if c in s1Hash:
                s2Hash[c] += 1
                if s2Hash == s1Hash:
                    return True
                while s2Hash[c] > s1Hash[c]:
                    if s2[l] in s2Hash:
                        s2Hash[s2[l]] -= 1
                    l += 1
                r += 1
            else:
                for k in s2Hash:
                    s2Hash[k] = 0
                r += 1
                l = r
        return False

        
            
        