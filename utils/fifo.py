class FifoQueue:
    def __init__(self, init):
        self.arr = init

    def enqueue(self, e):
        self.arr.insert(0, e)

    def dequeue(self):
        return self.arr.pop()

    def is_empty(self):
        return len(self.arr) == 0

    def top(self):
        return self.arr[len(self.arr) - 1]
