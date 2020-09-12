import math

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

    def element_at(self, pos):
        if self.is_empty():
            return None
        else:
            buffer = self.head
            count = 0
            while buffer is not None:
                if count == pos:
                    return buffer.value
                count += 1
                buffer = buffer.next_node
            return None

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
            return -1
        else:
            if pos == 0:
                return self.pop_front()
            elif pos == self.size() - 1:
                return self.pop_back()
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
            return buffer.value

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

    def __str__(self):
        if self.is_empty():
            return 'Empty'
        else:
            buffer = self.head
            out = ''
            while buffer is not None:
                out += str(buffer.value)+' '
                buffer = buffer.next_node
            return out


class Scramble:
    def __init__(self, lst=None):
        self.data = LinkedList()
        if lst is not None:
            for item in lst:
                self.data.push_back(item)
        self.shuffle_card = 0
        self.bottom_up_card = 0
        self.shuffle_percent = 0
        self.bottom_up_percent = 0

    def split_pack(self, number):  # change to pass as an exact number
        list1 = LinkedList()
        list2 = LinkedList()

        for i in range(number):  # first n elements
            x = self.data.pop_front()
            list1.push_back(x)
            self.data.push_back(x)
        for i in range(self.data.size() - number):  # the rest of list
            x = self.data.pop_front()
            list2.push_back(x)
            self.data.push_back(x)
        # print(f'List1: {list1}\t\tList2: {list2}')
        return list1, list2

    def shuffle(self, percent):
        self.shuffle_card = math.floor(self.data.size()*percent/100)
        self.shuffle_percent = percent
        main_pack, insert_pack = self.split_pack(self.shuffle_card)
        # print(main_pack, '\t', insert_pack)
        # insertion at 1, 3, 5, ...
        to_loop = insert_pack.size()  # self.data.size() - self.shuffle_card
        for i in range(1, to_loop+1):
            # print("insert pos:", i*2-1)
            main_pack.insert(i*2-1, insert_pack.pop_front())
        print(f'Riffle {percent:.3f} % :', main_pack)
        self.data = main_pack

    def bottom_up(self, percent):  # cut
        self.bottom_up_percent = percent
        self.bottom_up_card = math.floor(self.data.size()*percent/100)
        top, bottom = self.split_pack(self.bottom_up_card)
        while not top.is_empty():
            bottom.push_back(top.pop_front())
        print(f'BottomUp {percent:.3f} % :', bottom)
        self.data = bottom

    def de_shuffle(self):  # fix this
        a_list = LinkedList()
        b_list = LinkedList()
        count = 0
        # print(self.shuffle_card)
        if self.shuffle_card >= 5:
            for i in range(self.data.size()):
                if i % 2 == 1 and count < self.data.size() - self.shuffle_card:
                    a_list.push_back(self.data.element_at(i))
                    count += 1
                else:
                    b_list.push_back(self.data.element_at(i))
            # print(a_list, '\t', b_list)
            while not self.data.is_empty():
                self.data.pop_front()
            while not b_list.is_empty():
                self.data.push_back(b_list.pop_front())
            while not a_list.is_empty():
                self.data.push_back(a_list.pop_front())
        else:
            for i in range(self.data.size()):
                if i % 2 == 0 and count < self.shuffle_card:
                    a_list.push_back(self.data.element_at(i))
                    count += 1
                else:
                    b_list.push_back(self.data.element_at(i))
            # print(a_list, '\t', b_list)
            while not self.data.is_empty():
                self.data.pop_front()
            while not a_list.is_empty():
                self.data.push_back(a_list.pop_front())
            while not b_list.is_empty():
                self.data.push_back(b_list.pop_front())
        print(f'Deriffle {self.shuffle_percent:.3f} % :', self.data)

    def de_bottom_up(self):
        top, bottom = self.split_pack(self.data.size()-self.bottom_up_card)
        # print(top, "\t", bottom)
        while not top.is_empty():
            bottom.push_back(top.pop_front())
        print(f'Debottomup {self.bottom_up_percent:.3f} % :', bottom)
        self.data = bottom

    def __str__(self):
        return str(self.data)


def test():
    sc = Scramble([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    sc.bottom_up(30)
    sc.shuffle(60)
    print('------------------------------')
    sc.de_shuffle()
    sc.de_bottom_up()


if __name__ == '__main__':
    inp = input('Enter Input : ').split('/')
    initial = list(map(int, inp[0].split()))
    scramble_list = inp[1].split('|')
    # print(initial)
    # print(scramble_list)
    order = LinkedList()
    for i in range(len(scramble_list)):
        cmd = scramble_list[i].split(',')
        sc = Scramble(initial)
        print('--------------------------------------------------')
        print(f'Start : {sc}')
        if i < len(scramble_list) / 2:
            for j in range(len(cmd)):
                method, percent = cmd[j].split()
                percent = float(percent)
                order.push_back(method)
                if method == 'B':
                    sc.bottom_up(percent)
                else:
                    sc.shuffle(percent)

            while not order.is_empty():
                method = order.pop_back()
                if method == 'B':
                    sc.de_bottom_up()
                else:
                    sc.de_shuffle()
        else:
            for j in range(len(cmd)-1, -1, -1):
                method, percent = cmd[j].split()
                percent = float(percent)
                order.push_back(method)
                if method == 'B':
                    sc.bottom_up(percent)
                else:
                    sc.shuffle(percent)

            while not order.is_empty():
                method = order.pop_back()
                if method == 'B':
                    sc.de_bottom_up()
                else:
                    sc.de_shuffle()
    print('--------------------------------------------------')

'''
Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 23.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 62.000 % : 3 9 4 10 5 1 6 2 7 8
Deriffle 62.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 23.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------



Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 16.98,B 68.42|R 26.9257,B 57
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 68.420 % : 7 8 9 10 1 2 3 4 5 6
Riffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Deriffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Debottomup 68.420 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 57.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 26.926 % : 6 8 7 9 10 1 2 3 4 5
Deriffle 26.926 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 57.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------


Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20/B 32.4367,R 49.5484863|B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 32.437 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Riffle 49.548 % : 7 16 8 17 9 18 10 19 11 20 12 1 13 2 14 3 15 4 5 6
Deriffle 49.548 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Debottomup 32.437 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 89.464 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Riffle 12.896 % : 18 20 19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Deriffle 12.896 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 20.779 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Riffle 11.547 % : 5 7 6 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Deriffle 11.547 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 93.757 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Riffle 40.560 % : 19 7 20 8 1 9 2 10 3 11 4 12 5 13 6 14 15 16 17 18
Deriffle 40.560 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
'''