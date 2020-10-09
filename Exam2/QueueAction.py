'''
 * กลุ่มที่  : 20010101
 * 62010356 ธนพล วงศ์อาษา
 * chapter : 14	item : 2	ครั้งที่ : 0001
 * Assigned : Friday 9th of October 2020 01:51:17 PM --> Submission : Friday 9th of October 2020 01:58:56 PM
 * Elapsed time : 7 minutes.
 * filename : LinkedQueue.py
'''


class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = 'Linked data : '
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p


"""
 __str__():  ใช้สำหรับแสดงข้อมูลในคิว

    __len__():  ใช้สำหรับบอกจำนวนข้อมูลภายในคิว

    enQueue(data):  ใช้สำหรับเพิ่มข้อมูลเข้าคิว

    deQueue():  ใช้สำหรับนำข้อมูลออกจากคิว

    isEmpty():  ตรวจสอบว่าคิวว่างหรือไม่ ถ้าว่าจะแสดงค่า True ถ้าไม่ใช้ แสดง False
"""


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.removeHead()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.is_empty():
            out = 'Queue data : '
            for i in range(len(self.items)):
                val = self.items.nodeAt(i).data
                out += str(val) + ' '
            return out
        return 'Empty Queue'


if __name__ == '__main__':
    choice = int(input('Enter choice : '))
    if choice == 1:
        q1 = Queue()
        q1.enqueue(10)
        q1.enqueue(20)
        q1.enqueue(30)
        print(q1)
        q1.dequeue()
        q1.enqueue(40)
        print("Size of Queue :", len(q1))
        print(q1)
    elif choice == 2:
        q1 = Queue()
        q1.enqueue(100)
        q1.enqueue(200)
        q1.enqueue(300)
        q1.dequeue()
        print(q1)
        print("Queue is Empty :", q1.is_empty())
    elif choice == 3:
        q1 = Queue()
        q1.enqueue(11)
        q1.enqueue(22)
        q1.enqueue(33)
        q1.dequeue()
        q1.dequeue()
        q1.dequeue()
        print(q1)
        print("Size of Queue :", len(q1))
        print("Queue is Empty :", q1.is_empty())
