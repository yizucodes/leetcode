class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # cache
        self.cache = {}

        # head and tail
        self.head = Node()
        self.tail = Node()
        # connect them
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def _add_to_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def get(self, key: int) -> int:
        # key does not exist return -1
        if key not in self.cache:
            return - 1
        
        node = self.cache[key]

        # remove the node of the key
        self._remove(node)

        # move to the front
        self._add_to_front(node)

        # return the value
        return node.val

    def put(self, key: int, value: int) -> None:
        # key exists
        if key in self.cache:

            node = self.cache[key]

            node.val = value
           
            # remove node 
            self._remove(node)
            
            # put to the fron
            self._add_to_front(node)
        # does not exist
        else:
            # create new node
            node = Node(key, value)

            # add to cache 
            self.cache[key] = node

            # put to front
            self._add_to_front(node)

            # check for capacity
            if len(self.cache) > self.capacity:

                lru_node = self.tail.prev
                # remove last node before tail
                self._remove(lru_node)
                
                # delete from cache
                del self.cache[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)