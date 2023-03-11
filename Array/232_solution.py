class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        res = []
        for i in range(1, len(self.queue)):
            res.append(self.queue[i])
        val = self.queue[0]
        self.queue = res
        return val

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if self.queue == []:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
