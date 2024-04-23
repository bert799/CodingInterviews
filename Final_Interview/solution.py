class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.start = Node(key = -1, val = -1)
        self.end = Node(key = -1, val = -1)
        self.start.next = self.end
        self.end.prev = self.start
    
    def appendStart(self, node):
        left, right = self.start, self.start.next
        node.next = right
        node.prev = left
        left.next = node
        right.prev = node
    
        return node
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

        return node

    def move_to_start(self, node):
        return self.appendStart(self.remove(node))

    def pop(self):
        return self.remove(self.end.prev)
    
    def peek(self):
        return self.end.prev.val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.dll.move_to_start(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.dll.remove(self.cache[key])
            node.val = value

        node = Node(key, value)
        self.cache[key] = node

        self.dll.appendStart(node)

        if len(self.cache) > self.capacity:
            self.cache.pop(self.dll.pop().key)