def get_max_index(lst):
    right = len(lst)-1

    if lst[right] != max(lst) and right-1 >= 0:
        return get_max_index(lst[:right])
    else:
        return right


def selection_sort_rec(lst, right=None):
    if right is None:
        right = len(lst)-1
    if right < 0:
        return lst

    max_index = get_max_index(lst[:right+1])
    if max_index != right:  # if not in correct position
        lst[right], lst[max_index] = lst[max_index], lst[right]
        print(f'swap {lst[max_index]} <-> {lst[right]} : {lst}')
    return selection_sort_rec(lst, right-1)


if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    ans = selection_sort_rec(in_lst)
    print(in_lst)
