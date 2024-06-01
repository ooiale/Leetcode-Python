'''
  first, lets create an adjacency list that will track the lexicographical
  order of all characters from the words list. (all characters we can logically
  deduce the order of course). We add them in a set to avoid duplicates.
  now, the hardest part is to validate this lexicographical order we got from the
  strings.
  to do so we will use a post order DFS (post order so to avoid an edge case)
  so for every node in the adjacency list, run a dfs in it. it will be invalid
  if we find a loop. otherwise we can append the chars to the res array.
  since we are doing a post order dfs, in the end, we will have appended all
  chars in reverse order, so we will un-reverse it and join all in a string.
  time is O(nodes) where nodes is the sum of all characters in the list.
'''

from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            smallest = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:smallest] == w2[:smallest]:
                return ""
            for j in range(smallest):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        #here, we have the graph with the nodes pointing to
        #the chars that are bigger then itself lexicographically

        visited = {} #false = already visited in a prev dfs
                     #true = visiting in the current dfs
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True #dfs failed
            
            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)