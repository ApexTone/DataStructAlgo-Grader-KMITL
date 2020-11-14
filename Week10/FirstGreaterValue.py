def first_greater_value(lst, key):
    lst = sorted(lst)
    for item in lst:
        if item > key:
            return item
    return "No First Greater Value"


if __name__ == '__main__':
    inp = input("Enter Input : ").split('/')
    lst, key_lst = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
    for key in key_lst:
        print(first_greater_value(lst.copy(), key))