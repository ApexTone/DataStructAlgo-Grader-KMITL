# @todo #1:2days Fix permutation order, Check permutation code
if __name__ == '__main__':
    print('*** Fun with permute ***')
    num = [int(i) for i in input('input : ').split(',')]
    ans = []
    print('Original Cofllection: ', num)  # Typo for grader purpose
    # ans.append(num)
    num.reverse()
    for i in range(len(num)):
        temp = num.copy()
        print("Big loop", i)
        for j in range(i, len(num)):
            # print(temp[j], temp[j+1], end=" ")
            if i < len(num)-1:
                print('Normal', end=" ")
                temp[j], temp[j+1] = temp[j+1], temp[j]
            else:
                print('Special', end=" ")
                temp[0], temp[len(num)-1] = temp[len(num)-1], temp[0]
            print(temp)
            clone = temp.copy()
            if clone in ans:
                continue
            ans.append(clone)
    rev = num.copy()
    rev.reverse()
    # ans.append(rev)
    print('Collection of distinct numbers:\n', ans)

