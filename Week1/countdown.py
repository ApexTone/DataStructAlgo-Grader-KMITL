if __name__ == '__main__':
    print("*** Fun with countdown ***")
    lst = list(map(int, input("Enter List : ").split()))
    temp = list()
    countdown = list()
    for i in range(len(lst)):
        if i < len(lst)-1 and lst[i] != 1:
            if lst[i] - lst[i+1] == 1:
                temp.append(lst[i])
            else:
                temp = list()

        if lst[i] == 1:
            temp.append(lst[i])
            countdown.append(temp)
            temp = list()  # don't use .clear(), .append(temp) will use temp as pointer
    ans = list()
    ans.append(len(countdown))
    ans.append(countdown)
    print(ans)
