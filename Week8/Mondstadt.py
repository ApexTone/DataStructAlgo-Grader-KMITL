class ArrayBST:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def get_left_child_index(self, index):
        l_index = index*2+1
        return l_index if l_index < self.size() else -1

    def get_right_child_index(self, index):
        r_index = index*2+2
        return r_index if r_index < self.size() else -1

    def size(self):
        return len(self.items)

    def sum_power(self, init=0):  # bfs style
        queue = []
        value = 0
        queue.append(init)
        while len(queue) > 0:
            curr = queue.pop(0)
            # print(curr)
            if 0 <= curr < self.size():
                value += self.items[curr]
                l_child = self.get_left_child_index(curr)
                r_child = self.get_right_child_index(curr)
                # print(l_child, r_child)
                if l_child != -1:
                    queue.append(l_child)
                if r_child != -1:
                    queue.append(r_child)
                # print(queue)
            # print('-------------------------')
        return value

    def compare_power(self, root_a, root_b):
        a_power = self.sum_power(root_a)
        b_power = self.sum_power(root_b)
        if a_power > b_power:
            print(f'{root_a}>{root_b}')
        elif a_power < b_power:
            print(f'{root_a}<{root_b}')
        else:
            print(f'{root_a}={root_b}')

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    inp = input('Enter Input : ').split('/')
    initial_list = list(map(int, inp[0].split()))
    compare_list = inp[1].split(',')
    tree = ArrayBST(initial_list)
    print(tree.sum_power())
    for pair in compare_list:
        a, b = tuple(map(int, pair.split()))
        tree.compare_power(a, b)
