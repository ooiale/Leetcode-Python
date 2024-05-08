'''
we know that at maximum 10^4 opperations will be done 
so we will initialize an array with 10^4 dummy listNodes
using this array the hasing will be done by computing
key % 10^4. if keys are evenly distributed this will keep
the properties of add, remove and search opperations at O(1)
and space complexity of O(n)
'''


class ListNode:
    def __init__(self, key = -1, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode() for _ in range (10000)]

    def getSetIdx (self, key: int) -> int:
        return key % len(self.set)

    def add(self, key: int) -> None:
        idx = self.getSetIdx(key)
        prev = self.set[idx]
        cur = prev.next
        while cur:
            if cur.key == key:
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = self.getSetIdx(key)
        prev = self.set[idx]
        cur = prev.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def contains(self, key: int) -> bool:
        idx = self.getSetIdx(key)
        cur = self.set[idx].next #not dummy
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)