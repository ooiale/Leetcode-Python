'''
  a Trie is a tree where each node (except root) will have a value being
  a character. and by following a root in this tree we can form words.
  the special detail in this data structure is that we can easily search
  for prefixes in words.
  we used a hashMap to store the children. and each value in this map will be a new node. 
  also a variable endOfWord is placed at the node that delimiters the end of a word so if two words overlaps with each other we can still have both of them in the trie.
  the methods in this class are all O(n) with n being the length of the word.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self, value = None, end = False):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        return

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)