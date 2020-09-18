def rec_min(lst, acc_min=99999999):
    if len(lst) == 0:
        return acc_min
    else:
        num = lst.pop()
        if acc_min > num:
            acc_min = num
        return rec_min(lst, acc_min)

if __name__ == '__main__':
    lst = list(map(int, input("Enter Input : ").split()))
    print(f'Min : {rec_min(lst)}')