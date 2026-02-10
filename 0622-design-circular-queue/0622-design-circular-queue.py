class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.capacity = k
        self.size = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # check if full
        if self.size == self.capacity:
            return False

        # append to q[rear]
        self.q[self.rear] = value

        # shift rear by 1
        self.rear = (self.rear + 1) % self.capacity

        # increase size
        self.size += 1

        return True
        
    def deQueue(self) -> bool:
        # check if empty
        if self.size == 0:
            return False
        
        self.q[self.front] = None
        self.size -= 1
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1

        return self.q[self.front]
        
    def Rear(self) -> int:
        if self.size == 0:
            return -1

        return self.q[self.rear - 1]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()