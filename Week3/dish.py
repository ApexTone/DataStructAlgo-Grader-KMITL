class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return (999999999, 0)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return (999999999, 0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    dishes = input('Enter Input : ').split(',')  # weight freq,
    # print(dishes)
    s = Stack()
    for i in range(0, len(dishes)):
        weight, frequency = map(int, dishes[i].split())
        # print('peek:', s.peek()[0])
        if s.is_empty():
            s.push((weight, frequency))
        else:
            while weight > s.peek()[0]:
                dish = s.pop()
                print(dish[1])
            s.push((weight, frequency))
