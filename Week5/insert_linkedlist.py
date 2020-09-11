class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.push_back(item)

    def is_empty(self):
        return self.head is None or self.tail is None  # inspect this clause and head/tail assignment

    def size(self):
        buffer = self.head
        count = 0
        while buffer is not None:
            count += 1
            buffer = buffer.next_node
        return count

    def __len__(self):
        return self.size()

    def push_front(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            buffer = Node(value, self.head)
            self.head.prev_node = buffer
            self.head = buffer

    def push_back(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            self.tail.next_node = Node(value, prev_node=self.tail)
            self.tail = self.tail.next_node

    def is_in(self, value):
        if self.is_empty():
            return False
        buffer = self.head
        while buffer is not None:
            if buffer.val == value:
                return True
            buffer = buffer.next_node
        return False

    def index(self):
        pass

    def pop_back(self):
        if self.is_empty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev_node
        if self.tail is not None:
            self.tail.next_node = None
        last.prev_node = None
        if self.tail is None:  # list is now empty
            self.head = None
        return last.val

    def pop_front(self):
        if self.is_empty():
            print('List is empty')
            return -1
        first = self.head
        self.head = self.head.next_node
        if self.head is not None:
            self.head.prev_node = None
        first.next_node = None
        return first.val

    def traverse(self, rev=False):
        if self.is_empty():
            print('Empty linked list')
        if rev:
            buffer = self.tail
            out = 'The reversed list contains :'
            while buffer is not None:
                out += ' ' + str(buffer.val)
                buffer = buffer.prev_node
            print(out)
        else:
            buffer = self.head
            out = 'The list contains :'
            while buffer is not None:
                out += ' ' + str(buffer.val)
                buffer = buffer.next_node
            print(out)

    def remove(self, value):
        if self.is_empty() or not self.is_in(value):
            print("Value not found in list")
            return -1
        else:
            buffer = self.head
            while buffer is not None:
                if buffer.val == value:
                    break
                buffer = buffer.next_node
            if buffer is self.head:
                return self.pop_front()
            elif buffer is self.tail:
                return self.pop_back()
            else:
                prev_node = buffer.prev_node
                next_node = buffer.next_node
                val = buffer.val
                buffer.prev_node = None
                buffer.next_node = None
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
                return val

    def insert(self, index, value):  # custom this
        if 0 <= index <= self.size():
            if index == 0:
                print(f"index = {index} and data = {value}")
                self.push_front(value)
            elif index == self.size():
                print(f"index = {index} and data = {value}")
                self.push_back(value)
            else:
                print(f"index = {index} and data = {value}")
                count = 0
                buffer = self.head
                while buffer is not None and count != index:
                    buffer = buffer.next_node
                    count += 1
                prev = buffer.prev_node
                new_node = Node(value, buffer, prev)
                prev.next_node = new_node
                buffer.prev_node = new_node
        else:
            print('Data cannot be added')

    def __str__(self):
        if self.is_empty():
            return 'List is empty'
        else:
            buffer = self.head
            out = 'link list : '
            while buffer is not None:
                out += str(buffer.value)
                if buffer.next_node is not None:
                    out += '->'
                buffer = buffer.next_node
            return out


if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')
    lst = inp[0].split()
    insertion = list(map(lambda text: text.strip(), inp[1:]))
    # print(lst, insertion)
    l = LinkedList(lst)
    print(l)
    for items in insertion:
        pos, val = items.split(':')
        pos = int(pos)
        val = int(val)

        l.insert(pos, val)
        print(l)


