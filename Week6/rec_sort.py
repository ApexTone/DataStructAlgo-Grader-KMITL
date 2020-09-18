def rec_max(lst, acc_max=-99999999999):
    if len(lst) == 0:
        return acc_max
    else:
        num = lst.pop()
        if acc_max < num:
            acc_max = num
        return rec_max(lst, acc_max)


def rec_sort(lst, out, length):
    if len(out) < length:
        to_append = rec_max(lst.copy())
        # print(to_append)
        out.append(to_append)
        lst.remove(to_append)
        rec_sort(lst, out, length)
        if len(out) == length:
            return out
    else:
        return out


if __name__ == '__main__':
    lst = list(map(int, input('Enter your List : ').split(',')))
    lst = rec_sort(lst, [], len(lst))
    print(f"List after Sorted : {lst}")