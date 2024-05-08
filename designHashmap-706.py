'''
it is given that we will do at most 10^4 opperations so
I initialized an initial array with this size. 
the hashing will be done by computing key % 10^4
if all values added are evenly distributed then each index
in the array will contain one listNode so operations like
add, del, search are O(1)
the reason we use a linked list is in the case two keys hash 
to the same value (eg: 100 % 1000 = 100 and 1100 % 1000 = 100)
memory wise this algo is O(n) -> map array and linked lists.

https://leetcode.com/problems/design-hashmap/description/
'''


class ListNode:
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range (10000)]

    def getMapIdx(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        idx = self.getMapIdx(key) 
        prev = self.map[idx] #dummy node
        cur = prev.next
        while cur:
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self.getMapIdx(key)
        cur = self.map[idx].next #next from dummy
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = self.getMapIdx(key)
        prev = self.map[idx]
        cur = prev.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)