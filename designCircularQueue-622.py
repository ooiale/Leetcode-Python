'''
  queue designed using a double edged linked list
'''

class ListNode:
    def __init__ (self, val = -1, prev = None, next = None):
        self.prev = prev
        self.next = next
        self.val = val
class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode()
        self.right =ListNode()
        self.left.next = self.right
        self.right.prev = self.left

        self.nodes = 0
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        prev = self.right.prev
        newNode = ListNode(val = value, prev = prev, next = self.right)
        self.right.prev = newNode
        prev.next = newNode
        self.nodes += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        nxt = self.left.next.next
        self.left.next = nxt
        nxt.prev = self.left
        self.nodes -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.nodes == 0

    def isFull(self) -> bool:
        return self.nodes == self.max


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()