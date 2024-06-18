'''
  Honeslty, I don't know why it works. we do a post order DFS with the reverse
  order and it works... its called Hierholzer's algorithm
'''


from collections import defaultdict
from types import list


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        res = []
        for f, t in tickets:
            adj[f].append(t)

        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop()) #pops from smaller to bigger in lexi order
            res.append(node)
        dfs("JFK")
        res.reverse()
        return res