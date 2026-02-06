class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()   
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # access node cache[key]
        node = self.cache[key]

        # remove
        self._remove(node)

        # add node to the front
        self._add_to_front(node)

        # return the value of the node
        return node.value

    def put(self, key: int, value: int) -> None:
        # key in cache
        if key in self.cache:

            # update the key and value
            node = self.cache[key]

            # update node value
            node.value = value

            # remove node
            self._remove(node)

            # add to the front of the list
            self._add_to_front(node)

        # else: key not cache
        else:
            # create new node
            node = Node(key, value)
            # add to cache
            self.cache[key] = node
            # add to front
            self._add_to_front(node)

            # if capacity exceeded
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                # remove the lru key which is the last node before tail
                self._remove(lru_node)
                # remove from cache
                del self.cache[lru_node.key]
    
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)