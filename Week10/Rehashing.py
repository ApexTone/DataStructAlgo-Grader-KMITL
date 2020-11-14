# Fix Hidden 7/7
import math


class Hash:
    def __init__(self, table_size, max_collision, threshold=70):
        self.threshold = threshold
        self.max_collision = max_collision
        self.table_size = table_size
        self.table = []
        for _ in range(table_size):
            self.table.append(None)

    def get_hash(self, key):
        return key % self.table_size

    def number_of_elements(self):
        sum = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                sum += 1
        return sum

    def is_full(self):
        return self.number_of_elements() == self.table_size

    def rehash(self, adding=None):
        lst = []
        for item in self.table:   # store new value
            if item is not None:
                lst.append(item)
        if adding is not None:
            lst.append(adding)

        self.table = []

        for possible_prime in range(self.table_size*2, 9999999999):  # get new prime table size
            for i in range(2, int(math.sqrt(self.table_size*2))+1):
                if possible_prime % i == 0:
                    break
            else:
                self.table_size = possible_prime
                break

        for i in range(self.table_size):
            self.table.append(None)
        for value in lst:
            retry = 0
            hashed_index = self.get_hash(value)
            while retry < self.max_collision:
                index = (hashed_index + retry ** 2) % self.table_size
                if self.table[index] is None:
                    # print(value, index)
                    self.table[index] = value
                    break
                retry += 1
                print(f'collision number {retry} at {index}')


    def insert(self, value):
        print("Add :", value)

        retry = 0
        hashed_index = self.get_hash(value)
        while retry < self.max_collision:
            index = (hashed_index + retry ** 2) % self.table_size
            if self.table[index] is None:
                if (self.number_of_elements()+1) * 100 / self.table_size > self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash(value)
                else:
                    self.table[index] = value
                return
            retry += 1
            print(f'collision number {retry} at {index}')

        print("****** Max collision - Rehash !!! ******")
        self.rehash(value)

    def __str__(self):
        out = ''
        for i in range(self.table_size):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '----------------------------------------'
        return out


if __name__ == '__main__':
    print(" ***** Rehashing *****")
    control, lst = input("Enter Input : ").split('/')
    table_size, max_collision, threshold = list(map(int, control.split()))
    lst = list(map(int, lst.split()))
    print("Initial Table :")
    hash = Hash(table_size, max_collision, threshold)
    print(hash)
    for item in lst:
        hash.insert(item)
        print(hash)
