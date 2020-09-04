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
    inp = input('Enter Input : ').split('/')
    old_books = inp[0].split()
    actions = inp[1].split(',')
    # print(old_books, actions)
    q = Queue()
    for book in old_books:
        q.enqueue(book)
    # print(q)

    for cmd in actions:
        if len(cmd) == 1:
            if not q.is_empty():
                # print('pop')
                q.dequeue()
        else:
            # print('push')
            line = cmd.split()
            val = line[1]
            q.enqueue(val)
    # print(q)
    book_lst = []
    while not q.is_empty():
        book_lst.append(q.dequeue())
    book_set = set(book_lst)
    if len(book_set) != len(book_lst):
        print('Duplicate')
    else:
        print('NO Duplicate')