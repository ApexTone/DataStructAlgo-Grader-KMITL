"""
n = m = 0
E_num = []
E_list = []
D_num = []
D_list = 0

inpQ = input('Enter Input : ').split(',')
for i in range(len(inpQ)):
    # E number
    if len(inpQ[i].split()) == 2:
        x = inpQ[i].split()
        n = int(x[1])
        E_list.append(n)
        print(*E_list, sep=', ')
        D_list += 1
    # D
    else:
        if len(E_list) == 0:
            print('Empty')
        else:
            m = E_list.pop(0)
            D_num.append(m)
            E_num = E_list
            if len(E_list) == 0:
                print(m, '<- Empty')
            else:
                print(m, "<-", end=' ')
                print(*E_num, sep=', ')


if D_list == len(E_list):
    print(*E_list, sep=', ', end=' ')
    print(': Empty')
elif len(E_num) == 0:
    print(*D_num, sep=', ', end=' ')
    print(': Empty')
else:
    print(*D_num, sep=', ', end=' ')
    print(':', end=' ')
    print(*E_num, sep=', ')
"""


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


if __name__ == "__main__":
    pass
