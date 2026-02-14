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
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        # add to front
    def _add_to_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

        
    def get(self, key: int) -> int:
        # if key not exists return -1
        if key not in self.cache:
            return -1

        # node
        node = self.cache[key]

        # remove node
        self._remove(node)

        # add node to the front
        self._add_to_front(node)

        # return node.val
        return node.val
        
    def put(self, key: int, value: int) -> None:
        # key exists
        if key in self.cache:

            # access node
            node = self.cache[key]
            # update value of the node
            node.val = value
            # remove node
            self._remove(node)

            # add to front
            self._add_to_front(node)

        # key does not exist
        else:

            # create node
            newNode = Node(key, value)
            # add to front
            self._add_to_front(newNode)

            # add to cache
            self.cache[key] = newNode

            if len(self.cache) > self.capacity:
                # lru_node is self.tail.prev
                lru_node = self.tail.prev

                # remove the node
                self._remove(lru_node)

                # del node from cache
                del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)