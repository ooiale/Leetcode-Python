'''
  use a hashMap to store the frequency of each char in the substring
  start a l and r pointer at the start of the string and now increase
  r while updating the frequency hashMap. 
  the number of wild cards we need to use is given by the length of substring minus the most recurrent character and if this is greater than k, we need
  to start sliding our left pointer until that is fixed. doing so will update the frequency hash and size of the window.
  However, a tricky detail is that we don't need to be updating the frequency of the most recurrent character unless we find a bigger value than before.
  because the more this frequency the bigger the substring. so if we have a case with a m < M max frequency of a char then this substring is smaller than the one where M was the frequency of the most recurrent char.
  By doing this trick we don't need to run through the hash every time reducing the time complexity from O(26 * n) to O(n) since search in a hashMap is O(1).
  the 26 comes from the fact that we are only using 26 unique chars in the strings.
  storage complexity is O(1) for the hash map.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hash = {} #occurences of each char
        windowLength = 0
        output = 0
        max_occurence = 0
        while r < len(s):
            windowLength = r - l + 1
            hash[s[r]] = 1 + hash.get(s[r], 0)
            max_occurence = max(max(hash.values()), max_occurence)
            #here we could always update to just max(hash.values())
            while windowLength - max_occurence > k:
                hash[s[l]] -= 1
                #max_occurence = max(hash.values()) 
                #not necessary since big max_occurence 
                #implies bigger window length
                #so instead of always updating we only find max prior
                l += 1
                windowLength = r - l + 1
            r += 1
            output = max(output, windowLength)
            
        return output