class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        count = len(self.queue)
        temp_queue = []

        for _ in range(count - 1):
            temp = self.queue.pop(0)
            temp_queue.append(temp)

        temp = self.queue[0]
        self.queue = temp_queue
        return temp

    def top(self) -> int:
        val = self.pop()
        self.queue.append(val)
        return val

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()