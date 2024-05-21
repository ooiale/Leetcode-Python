'''
  iterate through the email chars, and append each char to the result email address.
  if you find "+" just skip until you find the "@"
  if you find "@" just append the rest of the email to the email address
  time is O(n) to build each email so O(n*m) for the entire algorithm
  and O(m) for memory to store the m different emails.
  it can be made faster by using .split() to divide the string since
  appending a char to a string is O(n) since strings are immutable
  class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)
'''

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            mail = ""
            i = 0
            while i < len(email):
                if email[i] == '@':
                    mail += email[i::]
                    break
                elif email[i] == '.':
                    i += 1
                elif email[i] == '+':
                    while  email[i] != "@":
                        i += 1
                else:
                    mail += email[i]
                    i += 1
            unique.add(mail)
        return len(unique)
                    
                    