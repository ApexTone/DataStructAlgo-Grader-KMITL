'''
 * กลุ่มที่  : 20010101
 * 62010356 ธนพล วงศ์อาษา
 * chapter : 14	item : 5	ครั้งที่ : 0001
 * Assigned : Friday 9th of October 2020 02:11:55 PM --> Submission : Friday 9th of October 2020 02:53:45 PM
 * Elapsed time : 41 minutes.
 * filename : LinkedMode.py
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

    def push_front(self, data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data)
        else:
            p = self.Node(data, self.head)
            self.head = p
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

    def contentEquivalence(self, other):
        if len(self) != len(other):
            return False
        # cheese?
        s1 = set()
        s2 = set()
        for i in range(len(self)):
            s1.add(self.nodeAt(i).data)
        for i in range(len(other)):
            s2.add(other.nodeAt(i).data)
        return s1==s2

    def add(self, data):
        if self.isEmpty():
            self.append(data)
        else:
            new_node = self.Node(data)
            if new_node.data < self.head.data:
                self.push_front(data)
                return
            buffer = self.head
            prev = None
            while buffer is not None:  # not end of list
                if prev is not None:
                    if prev.data <= new_node.data <= buffer.data:
                        new_node.next = buffer
                        prev.next = new_node
                        #print('MIDDLE',self)
                        self.size+=1
                        return
                prev = buffer
                buffer = buffer.next
            self.append(data)
            #print('ANYWAY',self)

def findMode(list):
    mem = {}
    maxOcc = 0
    for i in range(len(list)):
        data = list.nodeAt(i).data
        if mem.get(data,0) == 0:
            mem[data]=1
        else:
            mem[data]+=1
        if mem.get(data,0) > maxOcc:
            maxOcc = mem.get(data,0)
    # print(mem,maxOcc)
    ans = LinkedList()
    for key in mem:
        if mem[key] == maxOcc:
            ans.append(key)
    if len(ans) > 3:
        print('Mode is not available.')
        return
    else:
        out = 'Mode = '
        for i in range(len(ans)):
            data = ans.nodeAt(i).data
            out += ' '+str(data)
        print(out)


if __name__ == '__main__':
    numbers = list(map(int,input('Enter numbers : ').split()))
    list = LinkedList()
    for item in numbers:
        # print(item)
        list.add(item)
    print('Output :')
    print(list)
    print(f'Amount of data = {len(list)}')
    findMode(list)
