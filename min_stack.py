class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return self.stack

    def pop(self) -> None:
        self.stack.pop()
        return self.stack

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(1)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

print(obj)
