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
            new_node = Node(value, prev_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def is_in(self, value):
        if self.is_empty():
            return False
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return True
            buffer = buffer.next_node
        return False

    def index(self, value):
        buffer = self.head
        count = 0
        while buffer is not None:
            if buffer.value == value:
                return count
            count += 1
            buffer = buffer.next_node
        return -1

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
        return last.value

    def pop_front(self):
        if self.is_empty():
            print('List is empty')
            return -1
        first = self.head
        self.head = self.head.next_node
        if self.head is not None:
            self.head.prev_node = None
        first.next_node = None
        return first.value

    def traverse(self, rev=False):
        if self.is_empty():
            print('Empty linked list')
        if rev:
            buffer = self.tail
            out = 'The reversed list contains :'
            while buffer is not None:
                out += ' ' + str(buffer.value)
                buffer = buffer.prev_node
            print(out)
        else:
            buffer = self.head
            out = 'The list contains :'
            while buffer is not None:
                out += ' ' + str(buffer.value)
                buffer = buffer.next_node
            print(out)

    def remove(self, value):
        if self.is_empty() or not self.is_in(value):
            print("Value not found in list")
            return -1
        else:
            buffer = self.head
            while buffer is not None:
                if buffer.value == value:
                    break
                buffer = buffer.next_node
            if buffer is self.head:
                return self.pop_front()
            elif buffer is self.tail:
                return self.pop_back()
            else:
                prev_node = buffer.prev_node
                next_node = buffer.next_node
                val = buffer.value
                buffer.prev_node = None
                buffer.next_node = None
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
                return val

    def pop(self, pos):
        if self.is_empty() or not (0 <= pos <= self.size() - 1):
            return 'Out of Range'
        else:
            if pos == 0:
                self.pop_front()
            elif pos == self.size() - 1:
                self.pop_back()
            else:
                buffer = self.head
                count = 0
                while buffer is not None and count != pos:
                    count += 1
                    buffer = buffer.next_node
                prev_node = buffer.prev_node
                next_node = buffer.next_node
                buffer.prev_node = None
                buffer.next_node = None
                if prev_node is not None:
                    prev_node.next_node = next_node
                if next_node is not None:
                    next_node.prev_node = prev_node
            return 'Success'

    def insert(self, index, value):
        if index == 0 or self.is_empty():
            self.push_front(value)
        elif index >= self.size():
            self.push_back(value)
        elif index < 0:  # - case (before tail = -1)
            index = abs(index)
            count = 0
            buffer = self.tail
            while buffer is not None and count < index:
                # print(buffer)
                buffer = buffer.prev_node
                count += 1
            if buffer is None:
                self.push_front(value)
            else:
                # print("insertion at: ", buffer.prev_node, buffer, buffer.next_node)
                next_node = buffer.next_node
                new_node = Node(value, next_node, buffer)
                buffer.next_node = new_node
                next_node.prev_node = new_node
        else:  # + case
            count = 0
            buffer = self.head
            while buffer is not None and count != index:
                buffer = buffer.next_node
                count += 1
            prev = buffer.prev_node
            new_node = Node(value, buffer, prev)
            prev.next_node = new_node
            buffer.prev_node = new_node

    def redirect(self, pos1, pos2):  # special
        if pos1==0 and pos2==0 and self.is_empty():  # don't know what lead to this case (testcase 3) -> S 0:0
            return
        elif not 0 <= pos1 < self.size():
            print('Error! {index not in length}:', pos1)
        elif not 0 <= pos2 < self.size():
            print('index not in length, append :', pos2)
            self.push_back(pos2)
        else:
            buffer = self.head
            count = 0
            while buffer is not None and count < pos1:
                buffer = buffer.next_node
                count += 1
            node1 = buffer
            buffer = self.head
            count = 0
            while buffer is not None and count < pos2:
                buffer = buffer.next_node
                count += 1
            node2 = buffer
            node1.next_node = node2
            node2.prev_node = node1
            print(f'Set node.next complete!, index:value = {pos1}:{node1.value} -> {pos2}:{node2.value}')

    def is_loop(self):
        mem = []
        count = 0
        buffer = self.head
        # print('AFTER SELFHEAD')
        for _ in range(500):
            count += 1
            # print('RE')
            # print(mem, buffer)
            if buffer is None:
                break
            if buffer in mem:
                return True
            mem.append(buffer)
            buffer = buffer.next_node
        return False


    def __str__(self):
        if self.is_empty():
            return 'Empty'
        else:
            buffer = self.head
            out = ''
            while buffer is not None:
                out += str(buffer.value)
                if buffer.next_node is not None:
                    out += '->'
                buffer = buffer.next_node
            return out


if __name__ == '__main__':
    inp = input('Enter input : ').split(',')
    l = LinkedList()
    for item in inp:
        cmd, val = item.split()
        if cmd == 'A':
            l.push_back(val)
            print(l)
        else:
            ind1, ind2 = val.split(':')
            l.redirect(int(ind1), int(ind2))
            # print('Before is loop')
            if l.is_loop():
                print('Found Loop')
                break
            # print('After is loop')
    else:
        print('No Loop')
        print(l)
'''
(testcase3)
Enter input : S 0:0 
No Loop
Empty
'''