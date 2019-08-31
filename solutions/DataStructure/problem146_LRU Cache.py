# 思路：（双向）链表 + 字典 ~140ms
class Node:
    def __init__(self, k=0, v=0):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.dummy = Node()
        self.tail = Node()
        self.dummy.next = self.tail
        self.tail.prev = self.dummy

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node) # add to tail, which is most recently visited
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.dummy.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        'Remove node from current dual-linked-list'
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        # for safety
        node.prev = None
        node.next = None
        # cannot delete node, because it will be used later

    def _add(self, node):
        'Add new node to the tail'
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# A pythonic solution, use orderedDict, Slower ~260ms
from collections import OrderedDict
class LRUCache2(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest, which at head of OrderDict
            k = list(self.array.keys())[0]
            del self.array[k]
        self.array[key] = value
