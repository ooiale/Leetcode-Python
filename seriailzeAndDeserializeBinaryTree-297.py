'''
  for encoding, we will append the nodes in a pre order DFS.
  and delimiter them using a ",". and we will append "N" for 
  null nodes.
  for decoding, we will split the string by ","s so we will 
  have an array, each element containing either a value or N.
  now we start a DFS. at each call if our array[i] != "N", then
  we create a TreeNode. increment i+= 1 and append the next value
  of the array to the TreeNode.left. then to the TreeNode.right.
  since when arr[i] == "N" we increment i already, we don't need to
  increment it before calling TreeNode.right = dfs().
  time is O(n) for both operations
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        output = []
        def dfs(node):
            if not node:
                output.append("N")
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(output)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        #1,2,N,N,3,4,N,N,5,N,N, looks like this
        data = data.split(",")
        self.i = 0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(data[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

            






