class Queue:
    def __init__(self):
        self.items = list()

    def enqueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return -1

    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output


if __name__ == '__main__':
    inputs = input('Enter Input : ').split(',')
    q = Queue()
    for cmd in inputs:
        if len(cmd) == 1:
            if not q.is_empty():  # not a cool way to do but it works
                print(q.dequeue(), 0)
            else:
                print(-1)
        else:
            line = cmd.split()
            val = line[1]
            q.enqueue(val)
            print(q.size())
    print(q)