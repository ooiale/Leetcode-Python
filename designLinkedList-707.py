'''
  double edged linked list
'''

class ListNode:
    def __init__ (self, val = -1, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left
        while cur and index >= 0:
            cur = cur.next
            index -= 1
        if cur and cur.val != -1:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        right = self.left.next
        newNode = ListNode(val = val, next = right, prev = self.left)
        right.prev = newNode
        self.left.next = newNode

    def addAtTail(self, val: int) -> None:
        left = self.right.prev
        newNode = ListNode(val = val, next = self.right, prev = left)
        self.right.prev = newNode
        left.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left
        while cur and index >= 0:
            cur = cur.next
            index -= 1
        if not cur:
            return
        
        right = cur
        left = right.prev
        newNode = ListNode(val = val, next = right , prev = left)
        right.prev = newNode
        left.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left
        while cur and index >= 0:
            cur = cur.next
            index -= 1
        if cur and cur.val != -1:
            left = cur.prev
            right = cur.next
            left.next = right
            right.prev = left


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)