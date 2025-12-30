

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = k * [None]
        self.size = 0
        self.head = 0
        self.tail = 0
        self.capacity = k
        
    # constant time
    def enQueue(self, value: int) -> bool:
        # check if full
        if self.isFull(): return False

        # tail moves
        tail = (self.head + self.size) % self.capacity

        # insert at head
        self.q[tail] = value
        self.size += 1

        return True

    # constant time
    def deQueue(self) -> bool:

        # check if empty
        if self.isEmpty(): return False

        # head moves
        self.head = (self.head + 1) % self.capacity

        # decrease size
        self.size -= 1

        return True




    def Front(self) -> int:
        # empty
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        rear = (self.head + self.size - 1) % self.capacity
        return self.q[rear]
    
    def isEmpty(self) -> bool:
        if self.size == 0: return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.capacity: return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()