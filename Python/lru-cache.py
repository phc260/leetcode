class LRUCache:
    class ListNode:
        def __init__(self, k, v):
            self.key = k
            self.val = v
            self.prev = self.next = None
            
    class DoubleLinkedList:
        def __init__(self):
            self.tail = self.head = None
        def add(self, node):
            if node:
                if self.tail==self.head==None:
                    self.tail = self.head = node
                else:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
        def remove(self, node):
            if self.head==self.tail==node:
                self.head = self.tail = None
                return
            if self.head==node:
                self.head = self.head.next
                self.head.prev = None
                return
            if self.tail==node:
                self.tail = self.tail.prev
                self.tail.next = None
                return
            node.next.prev = node.prev
            node.prev.next = node.next

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hashmap = {}
        self.dlink = self.DoubleLinkedList()
        self.capacity = capacity
        self.size = 0

    # @return an integer
    def get(self, key):
        if key not in self.hashmap: return -1
        node = self.hashmap[key]
        self.dlink.remove(node)
        self.dlink.add(node)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            self.dlink.remove(node)
            node.val = value
            self.dlink.add(node)
        else:
            node = self.ListNode(key, value)
            self.hashmap[key] = node
            self.dlink.add(node)
            self.size += 1
            if self.size>self.capacity:
                del self.hashmap[self.dlink.tail.key]
                self.dlink.remove(self.dlink.tail)
                self.size -= 1
