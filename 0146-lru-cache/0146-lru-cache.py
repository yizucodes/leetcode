class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        if capacity < 1:
            print("Capacity must be at least 1")
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        # remove node from the list
        tempPrev = node.prev
        tempNext = node.next

        node.prev.next = tempNext
        node.next.prev = tempPrev
    
    def _add_to_front(self, node):
        # insert node into the list
        
        # Save next item
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # IF key exists: get node, update value, move to front
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        # ELSE: create new node, add to cache dict, add to front, check capacity
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_to_front(newNode)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]
            



        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)