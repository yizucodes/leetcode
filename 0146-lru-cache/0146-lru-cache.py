class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove
    def _remove_(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    # add to front
    def _add_to_front(self, node):
        temp = self.head.next
        self.head.next = node
        temp.prev = node
        node.next = temp
        node.prev = self.head
        
    def get(self, key: int) -> int:
        # if not key return -1
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # remove node
        self._remove_(node)

        # add to front
        self._add_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # key exists case
        if key in self.cache:
            # update value of key
            node = self.cache[key]
            node.val = value
            self._remove_(node)
            self._add_to_front(node)

        # key not exists
        else:
            # add key value pair
            newNode = Node(key, value)

            # add to front
            self._add_to_front(newNode)

            self.cache[key] = newNode

            if len(self.cache) > self.capacity:
                # evict lru node --> self.tail.prev 
                lru_node = self.tail.prev

                # remove from ll
                self._remove_(lru_node)

                # del from cache
                del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)