def is_sort(lst):
    if len(lst) == 1:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True


if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    res = is_sort(in_lst)
    if res:
        print("Yes")
    else:
        print("No")