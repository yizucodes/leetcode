class MinStack:

    def __init__(self):
        self.stack = []
        # self.node = { val: None, mini: None }

    def push(self, val: int) -> None:
        newMini = None

        # if empty list, set minimum to val
        if len(self.stack) == 0:
            newMini = val
        # if not empty, check if val < previousNode min, if it is mini = val else mini remains the same
        else:
            prevMini = self.stack[-1]["mini"]
            newMini = None

            if val < prevMini:
                newMini = val
            else:
                newMini = prevMini

        node = { "value": val, "mini": newMini }
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]["value"]
        
    def getMin(self) -> int:
        return self.stack[-1]["mini"]

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()