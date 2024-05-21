'''
  since we want a method to search for "parts" or prefixes of a word
  a trie is ideal. 
  for searching words, we will implement a recursive DFS that will go
  through each char of the given word and run down the trie.
  when a dot is found, we will run the DFS on all children.
  worst case scenario we will have to run through all nodes 
  of the tree because of the wildcards but this is an efficient 
  approach.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word) and node.endOfWord:
                return True
            elif idx == len(word):
                return False
            char = word[idx]
            if char in node.children:
                return dfs(node.children[char], idx + 1)
            if char == '.':
                for c in node.children.values():
                    if dfs(c, idx + 1):
                        return True
        return dfs(self.root, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)