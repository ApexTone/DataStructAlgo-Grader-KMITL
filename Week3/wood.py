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


if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')
    trees = []
    for i in range(len(inp)):
        if len(inp[i].split()) == 2:  # A -> tree
            sp = inp[i].split()
            h = int(sp[1])
            trees.append(h)
        else:  # B -> look back
            # print("Trees:", trees)
            count = 0
            highest = -1
            for j in range(len(trees)-1, -1, -1):
                if trees[j] > highest:  # must taller than the highest tree
                    highest = trees[j]
                    count += 1
                # print(highest)
            print(count)
