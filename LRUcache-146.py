'''
  to achieve insertion and search in O(1), a hash map is the best alternative.
  the problem lies in keeping track of the least used key in the cache.
  to achieve this, we will create a double edged linked list, where the left
  most element will be the least used one. To do that, everytime we use a key,
  we will move it to the rightmost side of this linked list.
  to maintain the O(1) efficiency, store the Node as value in the hash map
  and have this node contain the value.
  Time is O(1)
'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        #key => Node
        self.cache = {}
        #left is the least used node, right is the most recent
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.right, self.right.left = self.right, self.left

    def insert(self, node):
        #insert a node on the right
        prev, nxt = self.right.left, self.right
        node.left, node.right = prev, nxt
        prev.right = node
        nxt.left = node
    
    def remove(self, node):
        #remove node
        prev, nxt = node.left, node.right
        prev.right, nxt.left = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.left.right
            self.remove(node)
            del self.cache[node.key]
