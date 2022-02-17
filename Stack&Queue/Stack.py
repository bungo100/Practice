class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(stack.stack)
    stack.push(2)
    print(stack.stack)
    stack.push(3)
    print(stack.stack)
    print(stack.pop())
    print(stack.stack)
