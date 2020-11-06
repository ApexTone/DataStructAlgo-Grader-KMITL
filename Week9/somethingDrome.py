def drome(lst):
    is_des = True
    is_asc = True
    is_unique = True
    is_same = True
    unique_lst = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            is_des = False
        if lst[i] > lst[i+1]:
            is_asc = False
        if lst[i] in unique_lst:
            is_unique = False
        if lst[i] != lst[i+1]:
            is_same = False
        unique_lst.append(lst[i])
    if lst[len(lst)-1] in unique_lst:
        is_unique = False

    # do in this order to prevent bug (can also change condition to fix this but i'm too lazy)
    if is_same:
        return "Repdrome"
    elif is_asc and is_unique:
        return "Metadrome"
    elif is_asc and not is_unique:
        return "Plaindrome"
    elif is_des and is_unique:
        return "Katadrome"
    elif is_des and not is_unique:
        return "Nialpdrome"
    else:
        return "Nondrome"

def test():
    test_lst = [("1357","Metadrome"), ("12344","Plaindrome"), ("7531","Katadrome"), ("9874441","Nialpdrome"), ("666","Repdrome"), ("1985","Nondrome")]
    for item in test_lst:
        res = drome(list(item[0]))
        if res != item[1]:
            print(f"Case {item[0]} failed: {res} != {item[1]}")
        else:
            print(f"Case {item[0]} success")

if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ")))
    print(drome(in_lst))
    #test()