def selection_sort_rec(lst, left=0, sorted_lst=None):
    if sorted_lst is None:
        sorted_lst = []
    if left >= len(lst):
        return sorted_lst
    min_value = 999999999999
    min_index = -1
    for i in range(left, len(lst)):
        if min_value > lst[i]:
            min_value = lst[i]
            min_index = i
    lst[left], lst[min_index] = lst[min_index], lst[left]
    sorted_lst.append(lst[left])
    return selection_sort_rec(lst, left+1, sorted_lst)


if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    ans = selection_sort_rec(in_lst)
    print(ans)