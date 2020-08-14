def sum0(lst):
    if len(lst) <= 2:
        return 'Array Input Length Must More Than 2'
    output = list()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i]+lst[j]+lst[k] == 0 and [lst[i], lst[j], lst[k]] not in output:
                    output.append([lst[i], lst[j], lst[k]])
    return output


if __name__ == '__main__':
    arr = list(map(int, input('Enter Your List : ').split()))
    # print(arr)
    print(sum0(arr))

