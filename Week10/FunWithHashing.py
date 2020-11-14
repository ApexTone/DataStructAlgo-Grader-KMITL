class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = []
        for _ in range(table_size):
            self.table.append(None)

    def get_hash(self, key):
        index = 0
        for character in key:
            index += ord(character)
        return index % self.table_size

    def is_full(self):
        sum = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                sum += 1
        return sum == self.table_size

    def insert(self, data):
        if self.is_full():
            print("This table is full !!!!!!")
            quit()
        key, value = data.key, data.value
        retry = 0
        hashed_index = self.get_hash(key)
        while retry < self.max_collision:
            index = (hashed_index + retry ** 2) % self.table_size
            if self.table[index] is None:
                self.table[index] = data
                return
            retry += 1
            print(f'collision number {retry} at {index}')

        print("Max of collisionChain")

    def __str__(self):
        out = ''
        for i in range(self.table_size):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '---------------------------'
        return out


if __name__ == '__main__':
    print(" ***** Fun with hashing *****")
    control, lst = input("Enter Input : ").split('/')
    table_size, max_collision = list(map(int, control.split()))
    lst = lst.split(',')
    data_lst = []
    for item in lst:
        key, value = item.split()
        data_lst.append(Data(key, value))

    hash = Hash(table_size, max_collision)
    for data in data_lst:
        hash.insert(data)
        print(hash)