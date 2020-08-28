class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0
