'''
  we will create an adjacency list where the keys are the patterns possible
  by changing exactly 1 char from the curWord so for ex: dog => *og, d*g, do*
  Since we want the shortest path until the endWord, we will use a BFS until
  we find the word because once we do we know thats the shortest path.
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        if endWord not in wordList:
            return 0

        adj = defaultdict(list) # pattern => [words]

        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i + 1::]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                #add all neighbors to the queue
                for i in range(len(word)):
                    pattern = word[0:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                
            res += 1
        return 0
