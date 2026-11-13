class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Initialize dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        # Connect them
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
            

        



    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        node.next = nxt

        prev.next = node
        nxt.prev = node

        
