class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.size = 0
        self.front = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        # if at capacity --> return false
        if self.isFull():
            return False
        
        # add to q
        self.q[self.tail] = value

        # update tail
        self.tail = (self.tail + 1) % len(self.q)

        self.size += 1

        return True
        

    def deQueue(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False

        # remove front
        self.q[self.front] = None

        # wrap around
        self.front = (self.front + 1) % len(self.q)

        self.size -= 1

        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == len(self.q)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()