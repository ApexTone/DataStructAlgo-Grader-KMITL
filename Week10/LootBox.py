def binary_search(lst, key):
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def n_length_combo(lst, n):
    if n == 0:
        return [[]]
    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]
        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)
    return l


if __name__ == '__main__':
    lst, box = input("Enter Input : ").split('/')
    box = int(box)
    lst = sorted(list(map(int, lst.split())))
    if box == 1:
        print(f"Minimum weigth for {box} box(es) = {sum(lst)}")
        quit()
    elif box == len(lst):
        print(f"Minimum weigth for {box} box(es) = {max(lst)}")
        quit()

    # print(lst, sum(lst), box)
    combination_list = []
    for i in range(1, len(lst)):
        combination_list += n_length_combo(lst, i)
    print(combination_list)

    pick_box = []
    pick_box += n_length_combo(combination_list, box)
    print(pick_box)
    for value_set in pick_box:
        set_lst = []
        for item in value_set:
            for value in item:
                set_lst.append(value)
        if sorted(set_lst) == lst:
            print(set_lst)
