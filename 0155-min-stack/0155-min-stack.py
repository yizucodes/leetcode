class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
       

        # empty case or
        # if val < mini then mini = val
        if len(self.stack) == 0 or val < self.stack[-1]["mini"]:
            self.stack.append({ "value": val, "mini": val })
        else:
            self.stack.append({ "value": val, "mini": self.stack[-1]["mini"] })

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]["value"]
        # empty stack
        else:
            return []
        
    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]["mini"]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()