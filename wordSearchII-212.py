'''
  the efficiency issue we run here is having to run a dfs
  through every cell for each word. so we will be searching
  for all words at the same time during all dfs calls.
  to know if we are on the track for a possible word, we will
  use a Trie because it is very efficient to search for word
  prefix using this data structure.
  so the trick here is to create a trie with all words we want to search.
  then perform a DFS on each cell looking for the valid words.
  creating the trie is O(w) where w are the number of words we want to search
  and looking if the prefix is valid is O(1) 
  the total time complexity is O(m * n * dfs)
'''

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)

        output, path = set(), set()

        def dfs(i, j, node, word): 
            #node is one cell behind the index so we search (i,j) in node.children
            #word is the word we are forming in the dfs
            if (i < 0 or i >= ROW or j < 0 or j >= COL or 
                (i, j) in path or board[i][j] not in node.children):
                return

            char = board[i][j]

            path.add((i, j)) #visit the cell
            word += char #update forming word
            node = node.children[char] #update node

            if node.isWord:
                output.add(word)

            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            path.remove((i, j)) #unvisitting the node
            #note: we don't need to remove the char's last char because char
            #is a local variable at each callBack
        
        for i in range(ROW):
            for j in range(COL):
                dfs(i, j, trie.root, "")
        
        return list(output) #we started output as a set to avoid duplicates
