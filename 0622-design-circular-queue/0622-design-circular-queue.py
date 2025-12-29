class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.q = []

    def enQueue(self, value: int) -> bool:
        # can't insert past len(q)
        if len(self.q) == self.length:
            return False
        self.q.append(value)
        return True     

    def deQueue(self) -> bool:
        # empty
        if len(self.q) == 0:
            return False

        # deq the front el
        self.q.pop(0)
        return True
        
    def Front(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q[0] 

    def Rear(self) -> int:
        if len(self.q) == 0:
            return -1

        return self.q[len(self.q) - 1] 

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if len(self.q) == self.length:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()