class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def reverse(self):
        self.newqueue = []
        while self.queue:
            self.newqueue.append(self.queue.pop())
        return self.newqueue


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.queue)
    print(q.reverse())


