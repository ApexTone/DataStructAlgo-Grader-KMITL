'''
 * กลุ่มที่  : 20010101
 * 62010356 ธนพล วงศ์อาษา
 * chapter : 14	item : 3	ครั้งที่ : 0001
 * Assigned : Friday 9th of October 2020 01:59:01 PM --> Submission : Friday 9th of October 2020 02:09:05 PM
 * Elapsed time : 10 minutes.
 * filename : NoDup.py
'''
class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next

        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail =p
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self) :
        return self.size == 0

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def removeDup(self):
        if not self.isEmpty():
            mem = {}
            prev = None
            buffer = self.head
            while buffer is not None:
                # print(buffer)
                if mem.get(buffer.data,0) == 0:
                    mem[buffer.data] = 1
                    prev = buffer
                    buffer = buffer.next
                else:  # delete
                    if buffer.next is not None:  # if not tail
                        prev.next = buffer.next
                        buffer.next = None
                        buffer = prev.next  # move to next node
                    else:
                        prev.next = None
                        buffer = None


if __name__ == '__main__':
    inputlist = [int(e) for e in input('Enter numbers : ').split()]

    l = LinkedList()
    for item in inputlist:
        l.append(item)
    print("Linkedlist Before removeDuplicate")
    print(l)
    print("Linkedlist After removeDuplicate")
    l.removeDup()
    print(l)
