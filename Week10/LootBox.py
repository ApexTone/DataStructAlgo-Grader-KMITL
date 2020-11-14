if __name__ == '__main__':
    lst, box = input("Enter Input : ").split('/')
    box = int(box)
    lst = list(map(int, lst.split()))
    print(sorted(lst), sum(lst), box)
